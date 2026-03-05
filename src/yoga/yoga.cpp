#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <yoga/Yoga.h>
#include <yoga/node/Node.h>
#include <yoga/config/Config.h>
#include <yoga/event/event.h>

namespace py = pybind11;
namespace yoga = facebook::yoga;

static int yogaLogger(
    YGConfigConstRef config,
    YGNodeConstRef node,
    YGLogLevel level,
    const char* format,
    va_list args) {
    return 0;
}

// Helper to convert C++ YGValue to Python - return actual YGValue object
static YGValue YGValueToYGValue(YGValue v) {
    return v;
}

// Helper to set a dimension value from Python object (float or YGValue)
static void SetDimension(
    void (*setPoint)(YGNodeRef, float),
    void (*setPercent)(YGNodeRef, float),
    void (*setAuto)(YGNodeRef),
    YGNodeRef node,
    py::object value
) {
    if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
        // Plain number - treat as point
        float f = py::float_(value).cast<float>();
        setPoint(node, f);
    } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
        // YGValue-like object
        auto unit_py = value.attr("unit");
        auto value_py = value.attr("value");
        int unit_int = py::int_(unit_py).cast<int>();
        float f = py::float_(value_py).cast<float>();
        
        if (unit_int == YGUnitPercent) {
            setPercent(node, f);
        } else if (unit_int == YGUnitAuto) {
            if (setAuto) setAuto(node);
        } else {
            setPoint(node, f);
        }
    } else {
        // Try to convert to float
        float f = py::float_(value).cast<float>();
        setPoint(node, f);
    }
}

// Helper to handle edge/gutter parameter
static int GetEdgeOrGutter(py::object edge_or_gutter) {
    return py::int_(edge_or_gutter).cast<int>();
}

// ============================================================================
// Trampoline classes for callbacks
// ============================================================================

// Context structure to store Python callback and node reference
struct MeasureContext {
    py::object callback;  // Python callback function
    yoga::Node* node;     // Pointer to the node
};

struct BaselineContext {
    py::object callback;  // Python callback function
    yoga::Node* node;    // Pointer to the node
};

// Measure callback - trampoline that calls Python function
static YGSize MeasureTrampoline(
    YGNodeConstRef nodeRef,
    float width,
    YGMeasureMode widthMode,
    float height,
    YGMeasureMode heightMode
) {
    // Get the context we stored
    void* context = YGNodeGetContext(nodeRef);
    if (!context) {
        return YGSize{0, 0};
    }
    
    auto* ctx = static_cast<MeasureContext*>(context);
    
    // Check if callback exists
    if (ctx->callback.is_none()) {
        return YGSize{0, 0};
    }
    
    try {
        // Acquire GIL for Python call
        py::gil_scoped_acquire acquire;
        
        // Call Python callback with all parameters
        // Signature: measure(node, width, width_mode, height, height_mode) -> {"width": float, "height": float}
        py::object result = ctx->callback(
            py::cast(ctx->node),  // Pass node as user data
            py::float_(width),
            py::cast(widthMode),   // Pass enum value directly as int
            py::float_(height),
            py::cast(heightMode)   // Pass enum value directly as int
        );
        
        // Extract width and height from result dict
        float resultWidth = 0.0f;
        float resultHeight = 0.0f;
        
        if (py::isinstance<py::dict>(result)) {
            py::dict d = result.cast<py::dict>();
            if (d.contains("width")) {
                resultWidth = py::float_(d["width"]).cast<float>();
            }
            if (d.contains("height")) {
                resultHeight = py::float_(d["height"]).cast<float>();
            }
        } else if (py::isinstance<py::tuple>(result)) {
            // Also support returning tuple (width, height)
            py::tuple t = result.cast<py::tuple>();
            if (py::len(t) >= 2) {
                resultWidth = py::float_(t[0]).cast<float>();
                resultHeight = py::float_(t[1]).cast<float>();
            }
        }
        
        return YGSize{resultWidth, resultHeight};
        
    } catch (const py::error_already_set& e) {
        // Log error using py::print to avoid crash
        py::print("Yoga callback error:", e.what());
        return YGSize{0, 0};
    } catch (const std::exception& e) {
        // Log other errors
        py::print("Yoga callback error:", e.what());
        return YGSize{0, 0};
    }
}

// Baseline callback - trampoline that calls Python function
static float BaselineTrampoline(
    YGNodeConstRef nodeRef,
    float width,
    float height
) {
    // Get the context we stored
    void* context = YGNodeGetContext(nodeRef);
    if (!context) {
        return 0.0f;
    }
    
    auto* ctx = static_cast<BaselineContext*>(context);
    
    // Check if callback exists
    if (ctx->callback.is_none()) {
        return 0.0f;
    }
    
    try {
        // Acquire GIL for Python call
        py::gil_scoped_acquire acquire;
        
        // Call Python callback
        // Signature: baseline(node, width, height) -> float (baseline offset)
        py::object result = ctx->callback(
            py::cast(ctx->node),  // Pass node as user data
            py::float_(width),
            py::float_(height)
        );
        
        return py::float_(result).cast<float>();
        
    } catch (const py::error_already_set& e) {
        // Log error using py::print to avoid crash
        py::print("Yoga baseline callback error:", e.what());
        return 0.0f;
    } catch (const std::exception& e) {
        // Log other errors
        py::print("Yoga baseline callback error:", e.what());
        return 0.0f;
    }
}

PYBIND11_MODULE(yoga, m) {
    m.doc() = "Python binding for Facebook Yoga layout engine";

    // Enums - Fixed Display to use None_ instead of None
    py::enum_<YGDirection>(m, "Direction")
        .value("Inherit", YGDirectionInherit)
        .value("LTR", YGDirectionLTR)
        .value("RTL", YGDirectionRTL);

    py::enum_<YGUnit>(m, "Unit")
        .value("Undefined", YGUnitUndefined)
        .value("Point", YGUnitPoint)
        .value("Percent", YGUnitPercent)
        .value("Auto", YGUnitAuto)
        .value("MaxContent", YGUnitMaxContent)
        .value("FitContent", YGUnitFitContent)
        .value("Stretch", YGUnitStretch);

    py::enum_<YGFlexDirection>(m, "FlexDirection")
        .value("Column", YGFlexDirectionColumn)
        .value("ColumnReverse", YGFlexDirectionColumnReverse)
        .value("Row", YGFlexDirectionRow)
        .value("RowReverse", YGFlexDirectionRowReverse);

    py::enum_<YGJustify>(m, "Justify")
        .value("FlexStart", YGJustifyFlexStart)
        .value("Center", YGJustifyCenter)
        .value("FlexEnd", YGJustifyFlexEnd)
        .value("SpaceBetween", YGJustifySpaceBetween)
        .value("SpaceAround", YGJustifySpaceAround)
        .value("SpaceEvenly", YGJustifySpaceEvenly);

    py::enum_<YGOverflow>(m, "Overflow")
        .value("Visible", YGOverflowVisible)
        .value("Hidden", YGOverflowHidden)
        .value("Scroll", YGOverflowScroll);

    py::enum_<YGAlign>(m, "Align")
        .value("Auto", YGAlignAuto)
        .value("FlexStart", YGAlignFlexStart)
        .value("Center", YGAlignCenter)
        .value("FlexEnd", YGAlignFlexEnd)
        .value("Stretch", YGAlignStretch)
        .value("Baseline", YGAlignBaseline)
        .value("SpaceBetween", YGAlignSpaceBetween)
        .value("SpaceAround", YGAlignSpaceAround)
        .value("SpaceEvenly", YGAlignSpaceEvenly);

    py::enum_<YGPositionType>(m, "PositionType")
        .value("Static", YGPositionTypeStatic)
        .value("Relative", YGPositionTypeRelative)
        .value("Absolute", YGPositionTypeAbsolute);

    py::enum_<YGDisplay>(m, "Display")
        .value("Flex", YGDisplayFlex)
        .value("None_", YGDisplayNone)  // Note: None is Python keyword
        .value("Contents", YGDisplayContents);

    py::enum_<YGWrap>(m, "Wrap")
        .value("NoWrap", YGWrapNoWrap)
        .value("Wrap", YGWrapWrap)
        .value("WrapReverse", YGWrapWrapReverse);

    py::enum_<YGBoxSizing>(m, "BoxSizing")
        .value("BorderBox", YGBoxSizingBorderBox)
        .value("ContentBox", YGBoxSizingContentBox);

    py::enum_<YGMeasureMode>(m, "MeasureMode")
        .value("Undefined", YGMeasureModeUndefined)
        .value("Exactly", YGMeasureModeExactly)
        .value("AtMost", YGMeasureModeAtMost);

    py::enum_<YGDimension>(m, "Dimension")
        .value("Width", YGDimensionWidth)
        .value("Height", YGDimensionHeight);

    py::enum_<YGEdge>(m, "Edge")
        .value("Left", YGEdgeLeft)
        .value("Top", YGEdgeTop)
        .value("Right", YGEdgeRight)
        .value("Bottom", YGEdgeBottom)
        .value("Start", YGEdgeStart)
        .value("End", YGEdgeEnd)
        .value("Horizontal", YGEdgeHorizontal)
        .value("Vertical", YGEdgeVertical)
        .value("All", YGEdgeAll);

    py::enum_<YGNodeType>(m, "NodeType")
        .value("Default", YGNodeTypeDefault)
        .value("Text", YGNodeTypeText);

    py::enum_<YGLogLevel>(m, "LogLevel")
        .value("Error", YGLogLevelError)
        .value("Warn", YGLogLevelWarn)
        .value("Info", YGLogLevelInfo)
        .value("Debug", YGLogLevelDebug)
        .value("Verbose", YGLogLevelVerbose)
        .value("Fatal", YGLogLevelFatal);

    py::enum_<YGExperimentalFeature>(m, "ExperimentalFeature")
        .value("WebFlexBasis", YGExperimentalFeatureWebFlexBasis);

    py::enum_<YGGutter>(m, "Gutter")
        .value("Column", YGGutterColumn)
        .value("Row", YGGutterRow)
        .value("All", YGGutterAll);

    py::enum_<YGErrata>(m, "Errata")
        .value("None_", YGErrataNone)
        .value("StretchFlexBasis", YGErrataStretchFlexBasis)
        .value("AbsolutePositionWithoutInsetsExcludesPadding", YGErrataAbsolutePositionWithoutInsetsExcludesPadding)
        .value("AbsolutePercentAgainstInnerSize", YGErrataAbsolutePercentAgainstInnerSize)
        .value("All", YGErrataAll)
        .value("Classic", YGErrataClassic);

    // YGValue struct
    py::class_<YGValue>(m, "YGValue")
        .def(py::init<float, YGUnit>())
        .def(py::init([](float value) { return YGValue(value, YGUnitPoint); }))
        .def_readwrite("value", &YGValue::value)
        .def_readwrite("unit", &YGValue::unit)
        .def("__repr__", [](const YGValue& v) {
            std::string unit_str;
            switch(v.unit) {
                case YGUnitUndefined: unit_str = "Undefined"; break;
                case YGUnitPoint: unit_str = "Point"; break;
                case YGUnitPercent: unit_str = "Percent"; break;
                case YGUnitAuto: unit_str = "Auto"; break;
                case YGUnitMaxContent: unit_str = "MaxContent"; break;
                case YGUnitFitContent: unit_str = "FitContent"; break;
                case YGUnitStretch: unit_str = "Stretch"; break;
                default: unit_str = "Unknown"; break;
            }
            return "YGValue(" + std::to_string(v.value) + ", " + unit_str + ")";
        })
        .def("__eq__", [](const YGValue& a, const YGValue& b) {
            if (a.unit != b.unit) return false;
            if (a.unit == YGUnitUndefined || a.unit == YGUnitAuto || 
                a.unit == YGUnitMaxContent || a.unit == YGUnitFitContent || 
                a.unit == YGUnitStretch) return true;
            return a.value == b.value;
        })
        .def("__neg__", [](const YGValue& v) {
            return YGValue(-v.value, v.unit);
        });

    // YGValue helper functions - expose as module-level constants
    m.attr("YGValueAuto") = YGValue(0, YGUnitAuto);
    m.attr("YGValueUndefined") = YGValue(0, YGUnitUndefined);
    m.attr("YGValueZero") = YGValue(0, YGUnitPoint);
    m.attr("YGValueFitContent") = YGValue(0, YGUnitFitContent);
    m.def("YGValuePoint", [](float v) { return YGValue(v, YGUnitPoint); });
    m.def("YGValuePercent", [](float v) { return YGValue(v, YGUnitPercent); });
    m.def("YGFloatIsUndefined", [](float v) { return std::isnan(v); });
    m.def("round_value_to_pixel_grid", [](double value, double pointScaleFactor, bool ceil, bool floor) {
        return (float)YGRoundValueToPixelGrid(value, pointScaleFactor, ceil, floor);
    }, py::arg("value"), py::arg("point_scale_factor"), py::arg("ceil") = false, py::arg("floor") = false);

    // Event types
    py::enum_<yoga::Event::Type>(m, "EventType")
        .value("NodeAllocation", yoga::Event::Type::NodeAllocation)
        .value("NodeDeallocation", yoga::Event::Type::NodeDeallocation)
        .value("NodeLayout", yoga::Event::Type::NodeLayout)
        .value("LayoutPassStart", yoga::Event::Type::LayoutPassStart)
        .value("LayoutPassEnd", yoga::Event::Type::LayoutPassEnd)
        .value("MeasureCallbackStart", yoga::Event::Type::MeasureCallbackStart)
        .value("MeasureCallbackEnd", yoga::Event::Type::MeasureCallbackEnd)
        .value("NodeBaselineStart", yoga::Event::Type::NodeBaselineStart)
        .value("NodeBaselineEnd", yoga::Event::Type::NodeBaselineEnd)
        .export_values();

    // Layout data structure
    py::class_<yoga::LayoutData>(m, "LayoutData")
        .def(py::init<>())
        .def_readwrite("layouts", &yoga::LayoutData::layouts)
        .def_readwrite("measures", &yoga::LayoutData::measures)
        .def_readwrite("maxMeasureCache", &yoga::LayoutData::maxMeasureCache)
        .def_readwrite("cachedLayouts", &yoga::LayoutData::cachedLayouts)
        .def_readwrite("cachedMeasures", &yoga::LayoutData::cachedMeasures)
        .def_readwrite("measureCallbacks", &yoga::LayoutData::measureCallbacks);


    // Event subscription system
    m.def("event_reset", []() { yoga::Event::reset(); });
    m.def("event_subscribe", [](py::object callback) {
        yoga::Event::subscribe([callback](YGNodeConstRef node, yoga::Event::Type type, const yoga::Event::Data& data) {
            py::gil_scoped_acquire acquire;
            try {
                // Get node's pointer address as identifier
                uintptr_t node_id = reinterpret_cast<uintptr_t>(node);
                
                if (type == yoga::Event::Type::LayoutPassEnd) {
                    auto& eventData = data.get<yoga::Event::Type::LayoutPassEnd>();
                    auto* layoutData = eventData.layoutData;
                    callback(node_id, py::int_((int)type), 
                        layoutData ? py::cast(*layoutData) : py::none());
                } else {
                    callback(node_id, py::int_((int)type), py::none());
                }
            } catch (py::error_already_set& e) {
                fprintf(stderr, "Event callback Python error: %s\n", e.what());
            } catch (std::exception& e) {
                fprintf(stderr, "Event callback C++ error: %s\n", e.what());
            } catch (...) {
                fprintf(stderr, "Event callback unknown error\n");
            }
        });
    });

    // Config class
    py::class_<yoga::Config, std::unique_ptr<yoga::Config, py::nodelete>>(m, "Config")
        .def(py::init([](){ 
            auto config = new yoga::Config(yogaLogger);
            return config; 
        }))
        .def_property("use_web_defaults", 
            [](yoga::Config& self) { return self.useWebDefaults(); },
            [](yoga::Config& self, bool value) { self.setUseWebDefaults(value); })
        .def_property("point_scale_factor",
            [](yoga::Config& self) { return self.getPointScaleFactor(); },
            [](yoga::Config& self, float value) { self.setPointScaleFactor(value); })
        .def_property("errata",
            [](yoga::Config& self) { return (int)self.getErrata(); },
            [](yoga::Config& self, int value) { self.setErrata((yoga::Errata)value); })
        .def("set_experimental_feature_enabled", 
            [](yoga::Config& self, int feature, bool enabled) {
                self.setExperimentalFeatureEnabled(
                    facebook::yoga::scopedEnum(static_cast<YGExperimentalFeature>(feature)), enabled);
            })
        .def("is_experimental_feature_enabled",
            [](yoga::Config& self, int feature) {
                return self.isExperimentalFeatureEnabled(
                    facebook::yoga::scopedEnum(static_cast<YGExperimentalFeature>(feature)));
            })
        .def("__enter__", [](yoga::Config& self) { return &self; })
        .def("__exit__", [](yoga::Config& self, const py::object&, const py::object&, const py::object&) { })
        .def("set_logger", [](yoga::Config& self, py::object logger) {
            if (logger.is_none()) {
                YGConfigSetLogger(&self, nullptr);
            } else {
                YGConfigSetLogger(&self, yogaLogger);
            }
        })
        .def("set_clone_node_callback", [](yoga::Config& self, py::object func) {
            if (func.is_none()) {
                self.setCloneNodeCallback(nullptr);
                return;
            }
            auto* callback_ctx = new py::object(func);
            self.setCloneNodeCallback([](YGNodeConstRef oldNode, YGNodeConstRef owner, size_t childIndex) -> YGNodeRef {
                void* ctx = YGConfigGetContext(YGNodeGetConfig(const_cast<YGNodeRef>(oldNode)));
                if (!ctx) return nullptr;
                auto* py_ctx = static_cast<py::object*>(ctx);
                if (py_ctx->is_none()) return nullptr;
                
                py::gil_scoped_acquire acquire;
                try {
                    yoga::Node* oldNodePtr = const_cast<yoga::Node*>(static_cast<const yoga::Node*>(oldNode));
                    yoga::Node* ownerPtr = const_cast<yoga::Node*>(static_cast<const yoga::Node*>(owner));
                    py::object result = (*py_ctx)(
                        py::cast(oldNodePtr),
                        py::cast(ownerPtr),
                        py::cast(childIndex)
                    );
                    if (result.is_none()) return nullptr;
                    return static_cast<yoga::Node*>(result.cast<yoga::Node*>());
                } catch (...) {
                    return nullptr;
                }
            });
            YGConfigSetContext(&self, callback_ctx);
        })
        .def("clone_node", [](yoga::Config& self, const yoga::Node& node, const yoga::Node& owner, size_t childIndex) -> yoga::Node* {
            return static_cast<yoga::Node*>(self.cloneNode(&node, &owner, childIndex));
        });

    // Node class
    py::class_<yoga::Node, std::unique_ptr<yoga::Node, py::nodelete>>(m, "Node")
        .def(py::init([](){ return static_cast<yoga::Node*>(YGNodeNew()); }))
        .def(py::init([](yoga::Config& config){ return static_cast<yoga::Node*>(YGNodeNewWithConfig(&config)); }), py::arg("config"))
        .def("__len__", [](yoga::Node& self) { return YGNodeGetChildCount(&self); })
        .def("__getitem__", [](yoga::Node& self, size_t index) -> yoga::Node* { 
            return static_cast<yoga::Node*>(YGNodeGetChild(&self, index)); 
        }, py::return_value_policy::reference_internal)
        .def("__enter__", [](yoga::Node& self) { return &self; })
        .def("__exit__", [](yoga::Node& self, const py::object&, const py::object&, const py::object&) { 
            YGNodeFree(&self); 
        })

        // Lifecycle
        .def("free", [](yoga::Node& self) { YGNodeFree(&self); })
        .def("free_recursive", [](yoga::Node& self) { YGNodeFreeRecursive(&self); })
        .def("reset", [](yoga::Node& self) { YGNodeReset(&self); })
        .def("clone", [](yoga::Node& self) -> yoga::Node* { 
            return static_cast<yoga::Node*>(YGNodeClone(&self)); 
        })

        // Layout calculation
        .def("calculate_layout", [](yoga::Node& self, float availableWidth, float availableHeight, YGDirection direction) {
            YGNodeCalculateLayout(&self, availableWidth, availableHeight, direction);
        }, py::arg("available_width") = YGUndefined, py::arg("available_height") = YGUndefined, 
           py::arg("direction") = YGDirectionLTR)

        // Dirty state
        .def_property("has_new_layout", 
            [](yoga::Node& self) { return YGNodeGetHasNewLayout(&self); },
            [](yoga::Node& self, bool value) { YGNodeSetHasNewLayout(&self, value); })
        .def_property_readonly("is_dirty", 
            [](yoga::Node& self) { return YGNodeIsDirty(&self); })
        .def("mark_dirty", [](yoga::Node& self) { YGNodeMarkDirty(&self); })
        .def("set_dirty", [](yoga::Node& self, bool dirty) { self.setDirty(dirty); })
        .def("mark_dirty_and_propagate", [](yoga::Node& self) { self.markDirtyAndPropagate(); })

        // Context
        .def("set_context", [](yoga::Node& self, py::object context) {
            auto* ctx = new py::object(context);
            YGNodeSetContext(&self, ctx);
        })

        // Config
        .def("set_config", [](yoga::Node& self, yoga::Config& config) {
            YGNodeSetConfig(&self, &config);
        })
        .def("get_config", [](yoga::Node& self) -> yoga::Config* {
            return static_cast<yoga::Config*>(const_cast<YGConfigRef>(YGNodeGetConfig(&self)));
        })

        // Dirtied callback
        .def("set_dirtied_func", [](yoga::Node& self, py::object func) {
            if (func.is_none()) {
                YGNodeSetDirtiedFunc(&self, nullptr);
                void* ctx = YGNodeGetContext(&self);
                if (ctx) {
                    delete static_cast<py::object*>(ctx);
                    YGNodeSetContext(&self, nullptr);
                }
                return;
            }
            auto* ctx = new py::object(func);
            YGNodeSetDirtiedFunc(&self, [](YGNodeConstRef node) {
                void* ctx = YGNodeGetContext(node);
                if (!ctx) return;
                auto* py_ctx = static_cast<py::object*>(ctx);
                if (py_ctx->is_none()) return;
                py::gil_scoped_acquire acquire;
                try {
                    (*py_ctx)();
                } catch (...) {}
            });
            YGNodeSetContext(&self, ctx);
        })

        // Child management
        .def("insert_child", [](yoga::Node& self, yoga::Node& child, size_t index) { 
            YGNodeInsertChild(&self, &child, index); 
        }, py::arg("child"), py::arg("index"))
        .def("swap_child", [](yoga::Node& self, yoga::Node& child, size_t index) {
            YGNodeSwapChild(&self, &child, index);
        }, py::arg("child"), py::arg("index"))
        .def("remove_child", [](yoga::Node& self, yoga::Node& child) {
            YGNodeRemoveChild(&self, &child);
        }, py::arg("child"))
        .def("remove_all_children", [](yoga::Node& self) {
            YGNodeRemoveAllChildren(&self);
        })
        .def("set_children", [](yoga::Node& self, std::vector<yoga::Node*> children) {
            auto currentChildren = self.getChildren();
            for (auto* oldChild : currentChildren) {
                if (std::find(children.begin(), children.end(), oldChild) == children.end()) {
                    oldChild->setOwner(nullptr);
                }
            }
            for (yoga::Node* child : children) {
                if (child->getOwner() == nullptr || child->getOwner() == &self) {
                    child->setOwner(&self);
                }
            }
            self.setChildren(children);
            self.markDirtyAndPropagate();
        }, py::arg("children"))
        .def("get_layout_children", [](yoga::Node& self) {
            auto children = self.getLayoutChildren();
            std::vector<yoga::Node*> result;
            for (auto* child : children) {
                result.push_back(child);
            }
            return result;
        })
        .def_property_readonly("child_count", [](yoga::Node& self) {
            return YGNodeGetChildCount(&self);
        })
        .def_property_readonly("owner", [](yoga::Node& self) -> yoga::Node* {
            return static_cast<yoga::Node*>(YGNodeGetOwner(&self));
        })
        .def_property_readonly("parent", [](yoga::Node& self) -> yoga::Node* {
            return static_cast<yoga::Node*>(YGNodeGetParent(&self));
        })

        // Style - Direction
        .def_property("direction",
            [](yoga::Node& self) { return YGNodeStyleGetDirection(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetDirection(&self, (YGDirection)value); })

        // Style - Flex
        .def_property("flex_direction",
            [](yoga::Node& self) { return YGNodeStyleGetFlexDirection(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetFlexDirection(&self, (YGFlexDirection)value); })
        .def_property("justify_content",
            [](yoga::Node& self) { return YGNodeStyleGetJustifyContent(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetJustifyContent(&self, (YGJustify)value); })
        .def_property("align_content",
            [](yoga::Node& self) { return YGNodeStyleGetAlignContent(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetAlignContent(&self, (YGAlign)value); })
        .def_property("align_items",
            [](yoga::Node& self) { return YGNodeStyleGetAlignItems(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetAlignItems(&self, (YGAlign)value); })
        .def_property("align_self",
            [](yoga::Node& self) { return YGNodeStyleGetAlignSelf(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetAlignSelf(&self, (YGAlign)value); })
        .def_property("position_type",
            [](yoga::Node& self) { return YGNodeStyleGetPositionType(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetPositionType(&self, (YGPositionType)value); })
        .def_property("flex_wrap",
            [](yoga::Node& self) { return YGNodeStyleGetFlexWrap(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetFlexWrap(&self, (YGWrap)value); })
        .def_property("overflow",
            [](yoga::Node& self) { return YGNodeStyleGetOverflow(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetOverflow(&self, (YGOverflow)value); })
        .def_property("display",
            [](yoga::Node& self) { return YGNodeStyleGetDisplay(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetDisplay(&self, (YGDisplay)value); })

        // Style - Flex properties
        .def_property("flex",
            [](yoga::Node& self) { return YGNodeStyleGetFlex(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetFlex(&self, value); })
        .def_property("flex_grow",
            [](yoga::Node& self) { return YGNodeStyleGetFlexGrow(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetFlexGrow(&self, value); })
        .def_property("flex_shrink",
            [](yoga::Node& self) { return YGNodeStyleGetFlexShrink(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetFlexShrink(&self, value); })
        .def_property("flex_basis",
            [](yoga::Node& self) { return YGNodeStyleGetFlexBasis(&self); },
            [](yoga::Node& self, py::object value) { 
                SetDimension(
                    YGNodeStyleSetFlexBasis,
                    YGNodeStyleSetFlexBasisPercent,
                    YGNodeStyleSetFlexBasisAuto,
                    &self, value
                );
            })

        // Style - Position (returns YGValue, accepts float or YGValue)
        .def("get_position", [](yoga::Node& self, int edge) { 
            return YGValueToYGValue(YGNodeStyleGetPosition(&self, (YGEdge)edge)); 
        }, py::arg("edge"))
        .def("set_position", [](yoga::Node& self, int edge, py::object value) {
            if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetPosition(&self, (YGEdge)edge, f);
            } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
                auto unit_py = value.attr("unit");
                auto value_py = value.attr("value");
                int unit_int = py::int_(unit_py).cast<int>();
                float f = py::float_(value_py).cast<float>();
                if (unit_int == YGUnitPercent) {
                    YGNodeStyleSetPositionPercent(&self, (YGEdge)edge, f);
                } else {
                    YGNodeStyleSetPosition(&self, (YGEdge)edge, f);
                }
            } else {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetPosition(&self, (YGEdge)edge, f);
            }
        }, py::arg("edge"), py::arg("value"))
        .def("set_position_percent", [](yoga::Node& self, int edge, float value) {
            YGNodeStyleSetPositionPercent(&self, (YGEdge)edge, value);
        }, py::arg("edge"), py::arg("value"))
        .def("set_position_auto", [](yoga::Node& self, int edge) {
            YGNodeStyleSetPositionAuto(&self, (YGEdge)edge);
        }, py::arg("edge"))

        // Style - Margin
        .def("get_margin", [](yoga::Node& self, int edge) { 
            return YGValueToYGValue(YGNodeStyleGetMargin(&self, (YGEdge)edge)); 
        }, py::arg("edge"))
        .def("set_margin", [](yoga::Node& self, int edge, py::object value) {
            if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetMargin(&self, (YGEdge)edge, f);
            } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
                auto unit_py = value.attr("unit");
                auto value_py = value.attr("value");
                int unit_int = py::int_(unit_py).cast<int>();
                float f = py::float_(value_py).cast<float>();
                if (unit_int == YGUnitPercent) {
                    YGNodeStyleSetMarginPercent(&self, (YGEdge)edge, f);
                } else if (unit_int == YGUnitAuto) {
                    YGNodeStyleSetMarginAuto(&self, (YGEdge)edge);
                } else {
                    YGNodeStyleSetMargin(&self, (YGEdge)edge, f);
                }
            } else {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetMargin(&self, (YGEdge)edge, f);
            }
        }, py::arg("edge"), py::arg("value"))
        .def("set_margin_percent", [](yoga::Node& self, int edge, float value) {
            YGNodeStyleSetMarginPercent(&self, (YGEdge)edge, value);
        }, py::arg("edge"), py::arg("value"))
        .def("set_margin_auto", [](yoga::Node& self, int edge) {
            YGNodeStyleSetMarginAuto(&self, (YGEdge)edge);
        }, py::arg("edge"))

        // Style - Padding
        .def("get_padding", [](yoga::Node& self, int edge) { 
            return YGValueToYGValue(YGNodeStyleGetPadding(&self, (YGEdge)edge)); 
        }, py::arg("edge"))
        .def("set_padding", [](yoga::Node& self, int edge, py::object value) {
            if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetPadding(&self, (YGEdge)edge, f);
            } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
                auto unit_py = value.attr("unit");
                auto value_py = value.attr("value");
                int unit_int = py::int_(unit_py).cast<int>();
                float f = py::float_(value_py).cast<float>();
                if (unit_int == YGUnitPercent) {
                    YGNodeStyleSetPaddingPercent(&self, (YGEdge)edge, f);
                } else {
                    YGNodeStyleSetPadding(&self, (YGEdge)edge, f);
                }
            } else {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetPadding(&self, (YGEdge)edge, f);
            }
        }, py::arg("edge"), py::arg("value"))
        .def("set_padding_percent", [](yoga::Node& self, int edge, float value) {
            YGNodeStyleSetPaddingPercent(&self, (YGEdge)edge, value);
        }, py::arg("edge"), py::arg("value"))

        // Style - Border - returns float directly
        .def("get_border", [](yoga::Node& self, int edge) { 
            return YGNodeStyleGetBorder(&self, (YGEdge)edge);
        }, py::arg("edge"))
        .def("set_border", [](yoga::Node& self, int edge, py::object value) {
            float f;
            if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                f = py::float_(value).cast<float>();
            } else if (py::hasattr(value, "value")) {
                f = py::float_(value.attr("value")).cast<float>();
            } else {
                f = py::float_(value).cast<float>();
            }
            YGNodeStyleSetBorder(&self, (YGEdge)edge, f);
        }, py::arg("edge"), py::arg("value"))

        // Style - Gap (accepts both Edge and Gutter)
        .def("get_gap", [](yoga::Node& self, int gutter) { 
            return YGValueToYGValue(YGNodeStyleGetGap(&self, (YGGutter)gutter)); 
        }, py::arg("gutter"))
        .def("set_gap", [](yoga::Node& self, int gutter, py::object value) {
            if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetGap(&self, (YGGutter)gutter, f);
            } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
                auto unit_py = value.attr("unit");
                auto value_py = value.attr("value");
                int unit_int = py::int_(unit_py).cast<int>();
                float f = py::float_(value_py).cast<float>();
                if (unit_int == YGUnitPercent) {
                    YGNodeStyleSetGapPercent(&self, (YGGutter)gutter, f);
                } else {
                    YGNodeStyleSetGap(&self, (YGGutter)gutter, f);
                }
            } else {
                float f = py::float_(value).cast<float>();
                YGNodeStyleSetGap(&self, (YGGutter)gutter, f);
            }
        }, py::arg("gutter"), py::arg("value"))
        .def("set_gap_percent", [](yoga::Node& self, int gutter, float value) {
            YGNodeStyleSetGapPercent(&self, (YGGutter)gutter, value);
        }, py::arg("gutter"), py::arg("value"))

        // Style - Box sizing
        .def_property("box_sizing",
            [](yoga::Node& self) { return YGNodeStyleGetBoxSizing(&self); },
            [](yoga::Node& self, int value) { YGNodeStyleSetBoxSizing(&self, (YGBoxSizing)value); })

        // Style - Dimensions (width, height)
        .def_property("width",
            [](yoga::Node& self) { return YGNodeStyleGetWidth(&self); },
            [](yoga::Node& self, py::object value) { 
                if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                    float f = py::float_(value).cast<float>();
                    YGNodeStyleSetWidth(&self, f);
                } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
                    auto unit_py = value.attr("unit");
                    auto value_py = value.attr("value");
                    int unit_int = py::int_(unit_py).cast<int>();
                    float f = py::float_(value_py).cast<float>();
                    if (unit_int == YGUnitPercent) {
                        YGNodeStyleSetWidthPercent(&self, f);
                    } else if (unit_int == YGUnitAuto) {
                        YGNodeStyleSetWidthAuto(&self);
                    } else {
                        YGNodeStyleSetWidth(&self, f);
                    }
                } else {
                    float f = py::float_(value).cast<float>();
                    YGNodeStyleSetWidth(&self, f);
                }
            })
        .def_property("height",
            [](yoga::Node& self) { return YGNodeStyleGetHeight(&self); },
            [](yoga::Node& self, py::object value) { 
                if (py::isinstance<py::int_>(value) || py::isinstance<py::float_>(value)) {
                    float f = py::float_(value).cast<float>();
                    YGNodeStyleSetHeight(&self, f);
                } else if (py::hasattr(value, "unit") && py::hasattr(value, "value")) {
                    auto unit_py = value.attr("unit");
                    auto value_py = value.attr("value");
                    int unit_int = py::int_(unit_py).cast<int>();
                    float f = py::float_(value_py).cast<float>();
                    if (unit_int == YGUnitPercent) {
                        YGNodeStyleSetHeightPercent(&self, f);
                    } else if (unit_int == YGUnitAuto) {
                        YGNodeStyleSetHeightAuto(&self);
                    } else {
                        YGNodeStyleSetHeight(&self, f);
                    }
                } else {
                    float f = py::float_(value).cast<float>();
                    YGNodeStyleSetHeight(&self, f);
                }
            })
        .def("set_width_percent", [](yoga::Node& self, float value) {
            YGNodeStyleSetWidthPercent(&self, value);
        })
        .def("set_width_auto", [](yoga::Node& self) {
            YGNodeStyleSetWidthAuto(&self);
        })
        .def("set_width_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetWidthFitContent(&self);
        })
        .def("set_width_max_content", [](yoga::Node& self) {
            YGNodeStyleSetWidthMaxContent(&self);
        })
        .def("set_width_stretch", [](yoga::Node& self) {
            YGNodeStyleSetWidthStretch(&self);
        })
        .def("set_height_percent", [](yoga::Node& self, float value) {
            YGNodeStyleSetHeightPercent(&self, value);
        })
        .def("set_height_auto", [](yoga::Node& self) {
            YGNodeStyleSetHeightAuto(&self);
        })
        .def("set_height_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetHeightFitContent(&self);
        })
        .def("set_height_max_content", [](yoga::Node& self) {
            YGNodeStyleSetHeightMaxContent(&self);
        })
        .def("set_height_stretch", [](yoga::Node& self) {
            YGNodeStyleSetHeightStretch(&self);
        })
        .def("set_flex_basis_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetFlexBasisFitContent(&self);
        })
        .def("set_flex_basis_max_content", [](yoga::Node& self) {
            YGNodeStyleSetFlexBasisMaxContent(&self);
        })
        .def("set_flex_basis_stretch", [](yoga::Node& self) {
            YGNodeStyleSetFlexBasisStretch(&self);
        })
        .def("set_min_width_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetMinWidthFitContent(&self);
        })
        .def("set_min_width_max_content", [](yoga::Node& self) {
            YGNodeStyleSetMinWidthMaxContent(&self);
        })
        .def("set_min_width_stretch", [](yoga::Node& self) {
            YGNodeStyleSetMinWidthStretch(&self);
        })
        .def("set_min_width_percent", [](yoga::Node& self, float value) {
            YGNodeStyleSetMinWidthPercent(&self, value);
        })
        .def("set_min_height_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetMinHeightFitContent(&self);
        })
        .def("set_min_height_max_content", [](yoga::Node& self) {
            YGNodeStyleSetMinHeightMaxContent(&self);
        })
        .def("set_min_height_stretch", [](yoga::Node& self) {
            YGNodeStyleSetMinHeightStretch(&self);
        })
        .def("set_min_height_percent", [](yoga::Node& self, float value) {
            YGNodeStyleSetMinHeightPercent(&self, value);
        })
        .def("set_max_width_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetMaxWidthFitContent(&self);
        })
        .def("set_max_width_max_content", [](yoga::Node& self) {
            YGNodeStyleSetMaxWidthMaxContent(&self);
        })
        .def("set_max_width_stretch", [](yoga::Node& self) {
            YGNodeStyleSetMaxWidthStretch(&self);
        })
        .def("set_max_width_percent", [](yoga::Node& self, float value) {
            YGNodeStyleSetMaxWidthPercent(&self, value);
        })
        .def("set_max_height_fit_content", [](yoga::Node& self) {
            YGNodeStyleSetMaxHeightFitContent(&self);
        })
        .def("set_max_height_max_content", [](yoga::Node& self) {
            YGNodeStyleSetMaxHeightMaxContent(&self);
        })
        .def("set_max_height_stretch", [](yoga::Node& self) {
            YGNodeStyleSetMaxHeightStretch(&self);
        })
        .def("set_max_height_percent", [](yoga::Node& self, float value) {
            YGNodeStyleSetMaxHeightPercent(&self, value);
        })

        // Style - Min/Max dimensions
        .def_property("min_width",
            [](yoga::Node& self) { return YGNodeStyleGetMinWidth(&self); },
            [](yoga::Node& self, py::object value) { 
                SetDimension(
                    YGNodeStyleSetMinWidth,
                    YGNodeStyleSetMinWidthPercent,
                    nullptr,
                    &self, value
                );
            })
        .def_property("min_height",
            [](yoga::Node& self) { return YGNodeStyleGetMinHeight(&self); },
            [](yoga::Node& self, py::object value) { 
                SetDimension(
                    YGNodeStyleSetMinHeight,
                    YGNodeStyleSetMinHeightPercent,
                    nullptr,
                    &self, value
                );
            })
        .def_property("max_width",
            [](yoga::Node& self) { return YGNodeStyleGetMaxWidth(&self); },
            [](yoga::Node& self, py::object value) { 
                SetDimension(
                    YGNodeStyleSetMaxWidth,
                    YGNodeStyleSetMaxWidthPercent,
                    nullptr,
                    &self, value
                );
            })
        .def_property("max_height",
            [](yoga::Node& self) { return YGNodeStyleGetMaxHeight(&self); },
            [](yoga::Node& self, py::object value) { 
                SetDimension(
                    YGNodeStyleSetMaxHeight,
                    YGNodeStyleSetMaxHeightPercent,
                    nullptr,
                    &self, value
                );
            })

        // Style - Aspect ratio
        .def_property("aspect_ratio",
            [](yoga::Node& self) { return YGNodeStyleGetAspectRatio(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetAspectRatio(&self, value); })

        // Layout getters
        .def_property_readonly("layout_left", [](yoga::Node& self) { 
            return YGNodeLayoutGetLeft(&self); 
        })
        .def_property_readonly("layout_top", [](yoga::Node& self) { 
            return YGNodeLayoutGetTop(&self); 
        })
        .def_property_readonly("layout_right", [](yoga::Node& self) { 
            return YGNodeLayoutGetRight(&self); 
        })
        .def_property_readonly("layout_bottom", [](yoga::Node& self) { 
            return YGNodeLayoutGetBottom(&self); 
        })
        .def_property_readonly("layout_width", [](yoga::Node& self) { 
            return YGNodeLayoutGetWidth(&self); 
        })
        .def_property_readonly("layout_height", [](yoga::Node& self) { 
            return YGNodeLayoutGetHeight(&self); 
        })
        .def_property_readonly("layout_direction", [](yoga::Node& self) { 
            return YGNodeLayoutGetDirection(&self); 
        })
        .def_property_readonly("layout_had_overflow", [](yoga::Node& self) { 
            return YGNodeLayoutGetHadOverflow(&self); 
        })
        .def_property_readonly("layout_raw_width", [](yoga::Node& self) { 
            return YGNodeLayoutGetRawWidth(&self); 
        })
        .def_property_readonly("layout_raw_height", [](yoga::Node& self) { 
            return YGNodeLayoutGetRawHeight(&self); 
        })

        .def("layout_margin", [](yoga::Node& self, int edge) {
            return YGNodeLayoutGetMargin(&self, (YGEdge)edge);
        }, py::arg("edge"))
        .def("layout_border", [](yoga::Node& self, int edge) {
            return YGNodeLayoutGetBorder(&self, (YGEdge)edge);
        }, py::arg("edge"))
        .def("layout_padding", [](yoga::Node& self, int edge) {
            return YGNodeLayoutGetPadding(&self, (YGEdge)edge);
        }, py::arg("edge"))

        // Copy style
        .def("copy_style", [](yoga::Node& self, yoga::Node& src) {
            YGNodeCopyStyle(&self, &src);
        }, py::arg("src"))

        // Node type
        .def_property("node_type",
            [](yoga::Node& self) { return YGNodeGetNodeType(&self); },
            [](yoga::Node& self, int value) { YGNodeSetNodeType(&self, (YGNodeType)value); })

        // Reference baseline
        .def_property("is_reference_baseline",
            [](yoga::Node& self) { return YGNodeIsReferenceBaseline(&self); },
            [](yoga::Node& self, bool value) { YGNodeSetIsReferenceBaseline(&self, value); })

        // Always forms containing block
        .def_property("always_forms_containing_block",
            [](yoga::Node& self) { return YGNodeGetAlwaysFormsContainingBlock(&self); },
            [](yoga::Node& self, bool value) { YGNodeSetAlwaysFormsContainingBlock(&self, value); })

        .def("_node_id", [](yoga::Node& self) -> uintptr_t {
            return reinterpret_cast<uintptr_t>(&self);
        })

        // Measure callback
        .def("has_measure_func", [](yoga::Node& self) { 
            return YGNodeHasMeasureFunc(&self); 
        })
        .def("measure", [](yoga::Node& self, float width, int widthMode, float height, int heightMode) {
            auto result = self.measure(width, static_cast<yoga::MeasureMode>(widthMode), height, static_cast<yoga::MeasureMode>(heightMode));
            return py::make_tuple(result.width, result.height);
        })
        .def("set_measure_func", [](yoga::Node& self, py::object func) {
            if (func.is_none()) {
                // Remove existing context
                void* ctx = YGNodeGetContext(&self);
                if (ctx) {
                    delete static_cast<MeasureContext*>(ctx);
                }
                YGNodeSetMeasureFunc(&self, nullptr);
            } else {
                // Create new context with callback
                auto* ctx = new MeasureContext();
                ctx->callback = func;
                ctx->node = &self;
                
                // Store context and set trampoline
                YGNodeSetContext(&self, ctx);
                YGNodeSetMeasureFunc(&self, MeasureTrampoline);
            }
        })
        
        // Baseline callback
        .def("has_baseline_func", [](yoga::Node& self) { 
            return YGNodeHasBaselineFunc(&self); 
        })
        .def("baseline", [](yoga::Node& self, float width, float height) {
            return self.baseline(width, height);
        })
        .def("set_baseline_func", [](yoga::Node& self, py::object func) {
            if (func.is_none()) {
                // Remove existing context
                void* ctx = YGNodeGetContext(&self);
                if (ctx) {
                    delete static_cast<BaselineContext*>(ctx);
                }
                YGNodeSetBaselineFunc(&self, nullptr);
            } else {
                // Create new context with callback
                auto* ctx = new BaselineContext();
                ctx->callback = func;
                ctx->node = &self;
                
                // Store context and set trampoline
                // Reuse the context for baseline - Yoga allows this
                YGNodeSetContext(&self, ctx);
                YGNodeSetBaselineFunc(&self, BaselineTrampoline);
            }
        });
}
