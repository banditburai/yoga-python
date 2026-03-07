#include <nanobind/nanobind.h>
#include <nanobind/stl/vector.h>

#include <string>
#include <unordered_set>

#include <yoga/Yoga.h>
#include <yoga/node/Node.h>
#include <yoga/config/Config.h>
#include <yoga/event/event.h>

namespace nb = nanobind;
namespace yoga = facebook::yoga;

// Unified context for all node callbacks + user context.
// Stored in node->getContext() as a single allocation.
struct NodeContext {
    nb::object user_context;
    nb::object measure_callback;
    nb::object baseline_callback;
    nb::object dirtied_callback;
};

// Separate context for Config's clone callback (stored in config context).
struct CloneContext {
    nb::object callback;
};

// Track nodes created by nanobind (via Python Node() constructor).
// Nodes NOT in this set were allocated by YGNodeClone (system new) and
// must be delete'd manually in free()/free_recursive().
static std::unordered_set<yoga::Node*> nanobindManagedNodes;

// Track all allocated NodeContexts and CloneContexts for module cleanup.
// nanobind doesn't reliably call __del__ during interpreter shutdown,
// so we clean up all remaining contexts in the module cleanup capsule.
static std::unordered_set<NodeContext*> allNodeContexts;
static std::unordered_set<CloneContext*> allCloneContexts;

// --- NodeContext helpers ---

static NodeContext* getNodeContext(yoga::Node* node) {
    return static_cast<NodeContext*>(node->getContext());
}

static NodeContext* getOrCreateNodeContext(yoga::Node* node) {
    auto* ctx = getNodeContext(node);
    if (!ctx) {
        ctx = new NodeContext();
        allNodeContexts.insert(ctx);
        node->setContext(ctx);
    }
    return ctx;
}

static void cleanupNodeContext(yoga::Node* node) {
    auto* ctx = getNodeContext(node);
    if (ctx) {
        allNodeContexts.erase(ctx);
        delete ctx;
        node->setContext(nullptr);
    }
}

static void cleanupCloneContext(yoga::Config& config) {
    auto* ctx = static_cast<CloneContext*>(YGConfigGetContext(&config));
    if (ctx) {
        allCloneContexts.erase(ctx);
        delete ctx;
        YGConfigSetContext(&config, nullptr);
    }
}

// --- Safe free functions ---

static void safeNodeFree(yoga::Node& self) {
    // Clean up Python context
    cleanupNodeContext(&self);

    // Remove from owner (mirrors YGNodeFree)
    if (auto* owner = self.getOwner()) {
        owner->removeChild(&self);
        self.setOwner(nullptr);
    }

    // Orphan all children (mirrors YGNodeFree)
    const size_t childCount = self.getChildCount();
    for (size_t i = 0; i < childCount; i++) {
        self.getChild(i)->setOwner(nullptr);
    }
    self.clearChildren();

    // Publish deallocation event (mirrors YGNodeFree)
    yoga::Event::publish<yoga::Event::NodeDeallocation>(
        &self, {YGNodeGetConfig(&self)});

    // If this node was NOT created by nanobind (i.e. it was allocated via
    // YGNodeClone using system new), we must delete it ourselves.
    // nanobind-managed nodes are freed by nanobind's GC.
    if (nanobindManagedNodes.count(&self)) {
        nanobindManagedNodes.erase(&self);
        // Don't delete - nanobind owns this memory
    } else {
        delete &self;
    }
}

static void safeNodeFreeRecursive(yoga::Node& self) {
    // Mirrors YGNodeFreeRecursive: recursively free owned children
    size_t skipped = 0;
    while (self.getChildCount() > skipped) {
        auto* child = self.getChild(skipped);
        if (child->getOwner() != &self) {
            skipped += 1;
        } else {
            YGNodeRemoveChild(&self, child);
            safeNodeFreeRecursive(*child);
        }
    }
    safeNodeFree(self);
}

// --- Callbacks ---

static YGNodeRef yogaCloneNodeCallback(
    YGNodeConstRef oldNode,
    YGNodeConstRef owner,
    size_t childIndex) {
    YGConfigConstRef config = YGNodeGetConfig(const_cast<YGNodeRef>(oldNode));
    if (!config) return nullptr;

    void* ctx = YGConfigGetContext(const_cast<YGConfigRef>(config));
    if (!ctx) return nullptr;

    auto* context = static_cast<CloneContext*>(ctx);
    if (context->callback.is_none()) return nullptr;

    nb::gil_scoped_acquire acquire;
    try {
        yoga::Node* oldNodePtr = const_cast<yoga::Node*>(reinterpret_cast<const yoga::Node*>(oldNode));
        yoga::Node* ownerPtr = const_cast<yoga::Node*>(reinterpret_cast<const yoga::Node*>(owner));
        nb::object result = context->callback(oldNodePtr, ownerPtr, childIndex);
        if (result.is_none()) return nullptr;
        return static_cast<yoga::Node*>(nb::cast<yoga::Node*>(result));
    } catch (...) {
        return nullptr;
    }
}

static int yogaLogger(
    YGConfigConstRef config,
    YGNodeConstRef node,
    YGLogLevel level,
    const char* format,
    va_list args) {
    return 0;
}

static YGSize yogaMeasureCallback(
    YGNodeConstRef node,
    float width,
    YGMeasureMode widthMode,
    float height,
    YGMeasureMode heightMode) {
    yoga::Node* nodePtr = const_cast<yoga::Node*>(reinterpret_cast<const yoga::Node*>(node));
    auto* ctx = getNodeContext(nodePtr);
    if (!ctx || ctx->measure_callback.is_none()) {
        return YGSize{YGUndefined, YGUndefined};
    }
    nb::gil_scoped_acquire acquire;
    try {
        nb::object result = ctx->measure_callback(
            nodePtr,
            width,
            nb::cast(widthMode),
            height,
            nb::cast(heightMode)
        );
        if (nb::isinstance<nb::dict>(result)) {
            nb::dict d = nb::cast<nb::dict>(result);
            float w = nb::cast<float>(d["width"]);
            float h = nb::cast<float>(d["height"]);
            return YGSize{w, h};
        } else if (nb::isinstance<nb::tuple>(result)) {
            nb::tuple t = nb::cast<nb::tuple>(result);
            if (nb::len(t) >= 2) {
                float w = nb::cast<float>(t[0]);
                float h = nb::cast<float>(t[1]);
                return YGSize{w, h};
            }
        }
    } catch (...) {
    }
    return YGSize{YGUndefined, YGUndefined};
}

static float yogaBaselineCallback(
    YGNodeConstRef node,
    float width,
    float height) {
    yoga::Node* nodePtr = const_cast<yoga::Node*>(reinterpret_cast<const yoga::Node*>(node));
    auto* ctx = getNodeContext(nodePtr);
    if (!ctx || ctx->baseline_callback.is_none()) {
        return height;
    }
    nb::gil_scoped_acquire acquire;
    try {
        return nb::cast<float>(ctx->baseline_callback(nodePtr, width, height));
    } catch (...) {
    }
    return height;
}

static void yogaDirtiedCallback(YGNodeConstRef node) {
    yoga::Node* nodePtr = const_cast<yoga::Node*>(reinterpret_cast<const yoga::Node*>(node));
    auto* ctx = getNodeContext(nodePtr);
    if (!ctx || ctx->dirtied_callback.is_none()) {
        return;
    }
    nb::gil_scoped_acquire acquire;
    try {
        ctx->dirtied_callback();
    } catch (...) {
    }
}

NB_MODULE(yoga, m) {
    m.doc() = "Python binding for Facebook Yoga layout engine (using nanobind)";

    nb::enum_<YGDirection>(m, "Direction")
        .value("Inherit", YGDirectionInherit)
        .value("LTR", YGDirectionLTR)
        .value("RTL", YGDirectionRTL);

    nb::enum_<YGUnit>(m, "Unit")
        .value("Undefined", YGUnitUndefined)
        .value("Point", YGUnitPoint)
        .value("Percent", YGUnitPercent)
        .value("Auto", YGUnitAuto)
        .value("MaxContent", YGUnitMaxContent)
        .value("FitContent", YGUnitFitContent)
        .export_values();

    nb::enum_<YGErrata>(m, "Errata")
        .value("None_", YGErrataNone)
        .value("StretchFlexBasis", YGErrataStretchFlexBasis)
        .value("AbsolutePositionWithoutInsetsExcludesPadding", YGErrataAbsolutePositionWithoutInsetsExcludesPadding)
        .value("AbsolutePercentAgainstInnerSize", YGErrataAbsolutePercentAgainstInnerSize)
        .value("All", YGErrataAll)
        .value("Classic", YGErrataClassic)
        .export_values();

    nb::enum_<YGExperimentalFeature>(m, "ExperimentalFeature")
        .value("WebFlexBasis", YGExperimentalFeatureWebFlexBasis)
        .export_values();

    nb::enum_<yoga::Event::Type>(m, "EventType")
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

    nb::enum_<YGMeasureMode>(m, "MeasureMode")
        .value("Undefined", YGMeasureModeUndefined)
        .value("Exactly", YGMeasureModeExactly)
        .value("AtMost", YGMeasureModeAtMost)
        .export_values();

    nb::enum_<YGFlexDirection>(m, "FlexDirection")
        .value("Row", YGFlexDirectionRow)
        .value("RowReverse", YGFlexDirectionRowReverse)
        .value("Column", YGFlexDirectionColumn)
        .value("ColumnReverse", YGFlexDirectionColumnReverse)
        .export_values();

    nb::enum_<YGJustify>(m, "Justify")
        .value("FlexStart", YGJustifyFlexStart)
        .value("Center", YGJustifyCenter)
        .value("FlexEnd", YGJustifyFlexEnd)
        .value("SpaceBetween", YGJustifySpaceBetween)
        .value("SpaceAround", YGJustifySpaceAround)
        .value("SpaceEvenly", YGJustifySpaceEvenly)
        .export_values();

    nb::enum_<YGAlign>(m, "Align")
        .value("Auto", YGAlignAuto)
        .value("FlexStart", YGAlignFlexStart)
        .value("Center", YGAlignCenter)
        .value("FlexEnd", YGAlignFlexEnd)
        .value("Stretch", YGAlignStretch)
        .value("Baseline", YGAlignBaseline)
        .value("SpaceBetween", YGAlignSpaceBetween)
        .value("SpaceAround", YGAlignSpaceAround)
        .value("SpaceEvenly", YGAlignSpaceEvenly)
        .export_values();

    nb::enum_<YGPositionType>(m, "PositionType")
        .value("Static", YGPositionTypeStatic)
        .value("Relative", YGPositionTypeRelative)
        .value("Absolute", YGPositionTypeAbsolute)
        .export_values();

    nb::enum_<YGWrap>(m, "Wrap")
        .value("NoWrap", YGWrapNoWrap)
        .value("Wrap", YGWrapWrap)
        .value("WrapReverse", YGWrapWrapReverse)
        .export_values();

    nb::enum_<YGOverflow>(m, "Overflow")
        .value("Visible", YGOverflowVisible)
        .value("Hidden", YGOverflowHidden)
        .value("Scroll", YGOverflowScroll)
        .export_values();

    nb::enum_<YGDisplay>(m, "Display")
        .value("Flex", YGDisplayFlex)
        .value("None_", YGDisplayNone)
        .value("Contents", YGDisplayContents)
        .export_values();

    nb::enum_<YGBoxSizing>(m, "BoxSizing")
        .value("BorderBox", YGBoxSizingBorderBox)
        .value("ContentBox", YGBoxSizingContentBox)
        .export_values();

    nb::enum_<YGEdge>(m, "Edge")
        .value("Left", YGEdgeLeft)
        .value("Top", YGEdgeTop)
        .value("Right", YGEdgeRight)
        .value("Bottom", YGEdgeBottom)
        .value("Start", YGEdgeStart)
        .value("End", YGEdgeEnd)
        .value("Horizontal", YGEdgeHorizontal)
        .value("Vertical", YGEdgeVertical)
        .value("All", YGEdgeAll)
        .export_values();

    nb::enum_<YGGutter>(m, "Gutter")
        .value("All", YGGutterAll)
        .value("Row", YGGutterRow)
        .value("Column", YGGutterColumn)
        .export_values();

    nb::enum_<YGDimension>(m, "Dimension")
        .value("Width", YGDimensionWidth)
        .value("Height", YGDimensionHeight)
        .export_values();

    nb::enum_<YGNodeType>(m, "NodeType")
        .value("Default", YGNodeTypeDefault)
        .value("Text", YGNodeTypeText)
        .export_values();

    nb::enum_<YGLogLevel>(m, "LogLevel")
        .value("Error", YGLogLevelError)
        .value("Warn", YGLogLevelWarn)
        .value("Info", YGLogLevelInfo)
        .value("Debug", YGLogLevelDebug)
        .value("Verbose", YGLogLevelVerbose)
        .value("Fatal", YGLogLevelFatal)
        .export_values();

    nb::class_<YGValue>(m, "YGValue")
        .def(nb::init<float, YGUnit>())
        .def_prop_rw("value", [](YGValue& self) { return self.value; },
                       [](YGValue& self, float v) { self.value = v; })
        .def_prop_rw("unit", [](YGValue& self) { return self.unit; },
                       [](YGValue& self, YGUnit u) { self.unit = u; })
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

    m.attr("YGValueAuto") = YGValue(0, YGUnitAuto);
    m.attr("YGValueUndefined") = YGValue(0, YGUnitUndefined);
    m.attr("YGValueZero") = YGValue(0, YGUnitPoint);
    m.attr("YGValueFitContent") = YGValue(0, YGUnitFitContent);
    m.def("YGValuePoint", [](float v) { return YGValue(v, YGUnitPoint); });
    m.def("YGValuePercent", [](float v) { return YGValue(v, YGUnitPercent); });
    m.def("YGFloatIsUndefined", [](float v) { return std::isnan(v); });
    m.def("round_value_to_pixel_grid", [](double value, double pointScaleFactor, bool ceil, bool floor) {
        return (float)YGRoundValueToPixelGrid(value, pointScaleFactor, ceil, floor);
    }, nb::arg("value"), nb::arg("point_scale_factor"), nb::arg("ceil") = false, nb::arg("floor") = false);

    // LayoutData binding (for event system)
    nb::class_<yoga::LayoutData>(m, "LayoutData")
        .def_ro("layouts", &yoga::LayoutData::layouts)
        .def_ro("measures", &yoga::LayoutData::measures)
        .def_ro("maxMeasureCache", &yoga::LayoutData::maxMeasureCache)
        .def_ro("cachedLayouts", &yoga::LayoutData::cachedLayouts)
        .def_ro("cachedMeasures", &yoga::LayoutData::cachedMeasures)
        .def_ro("measureCallbacks", &yoga::LayoutData::measureCallbacks);

    m.def("event_reset", []() { yoga::Event::reset(); });
    m.def("event_subscribe", [](nb::object callback) {
        yoga::Event::subscribe([callback](YGNodeConstRef node, yoga::Event::Type type, const yoga::Event::Data& data) {
            nb::gil_scoped_acquire acquire;
            try {
                uintptr_t node_id = reinterpret_cast<uintptr_t>(node);
                if (type == yoga::Event::Type::LayoutPassEnd) {
                    auto& eventData = data.get<yoga::Event::Type::LayoutPassEnd>();
                    auto* layoutData = eventData.layoutData;
                    callback(node_id, nb::cast(type),
                        layoutData ? nb::cast(*layoutData) : nb::none());
                } else {
                    callback(node_id, nb::cast(type), nb::none());
                }
            } catch (...) {
            }
        });
        return 0;
    });

    nb::class_<yoga::Config>(m, "Config")
        .def("__init__", [](yoga::Config *t) { new (t) yoga::Config(yogaLogger); })
        .def_prop_rw("use_web_defaults",
            [](yoga::Config& self) { return self.useWebDefaults(); },
            [](yoga::Config& self, bool value) { self.setUseWebDefaults(value); })
        .def_prop_rw("point_scale_factor",
            [](yoga::Config& self) { return self.getPointScaleFactor(); },
            [](yoga::Config& self, float value) { self.setPointScaleFactor(value); })
        .def_prop_rw("errata",
            [](yoga::Config& self) { return YGConfigGetErrata(&self); },
            [](yoga::Config& self, YGErrata value) { YGConfigSetErrata(&self, value); })
        .def("set_clone_node_callback", [](yoga::Config& self, nb::object callback) {
            cleanupCloneContext(self);
            if (callback.is_none()) {
                self.setCloneNodeCallback(nullptr);
            } else {
                auto* context = new CloneContext{callback};
                allCloneContexts.insert(context);
                self.setCloneNodeCallback(yogaCloneNodeCallback);
                YGConfigSetContext(&self, context);
            }
        })
        .def("clone_node", [](yoga::Config& self, yoga::Node& node, yoga::Node* owner, size_t childIndex) -> yoga::Node* {
            return static_cast<yoga::Node*>(self.cloneNode(&node, owner, childIndex));
        }, nb::arg("node"), nb::arg("owner") = nullptr, nb::arg("child_index") = 0,
           nb::rv_policy::reference)
        .def("set_logger", [](yoga::Config& self, nb::object logger) {
            if (logger.is_none()) {
                YGConfigSetLogger(&self, nullptr);
            } else {
                YGConfigSetLogger(&self, yogaLogger);
            }
        })
        .def("set_experimental_feature_enabled", [](yoga::Config& self, YGExperimentalFeature feature, bool enabled) {
            self.setExperimentalFeatureEnabled(static_cast<yoga::ExperimentalFeature>(feature), enabled);
        }, nb::arg("feature"), nb::arg("enabled"))
        .def("is_experimental_feature_enabled", [](yoga::Config& self, YGExperimentalFeature feature) {
            return self.isExperimentalFeatureEnabled(static_cast<yoga::ExperimentalFeature>(feature));
        }, nb::arg("feature"))
        .def("__enter__", [](yoga::Config& self) -> yoga::Config& { return self; },
            nb::rv_policy::reference)
        .def("__exit__", [](yoga::Config& self, const nb::object&, const nb::object&, const nb::object&) {
            cleanupCloneContext(self);
        });

    nb::class_<yoga::Node>(m, "Node")
        .def("__init__", [](yoga::Node *t) {
            new (t) yoga::Node();
            nanobindManagedNodes.insert(t);
            yoga::Event::publish<yoga::Event::NodeAllocation>(t, {YGNodeGetConfig(t)});
        })
        .def("__init__", [](yoga::Node *t, yoga::Config* config) {
            new (t) yoga::Node(config);
            nanobindManagedNodes.insert(t);
            yoga::Event::publish<yoga::Event::NodeAllocation>(t, {YGNodeGetConfig(t)});
        }, nb::arg("config"))
        .def("__len__", [](yoga::Node& self) { return YGNodeGetChildCount(&self); })
        .def("__getitem__", [](yoga::Node& self, size_t index) -> yoga::Node* {
            return static_cast<yoga::Node*>(YGNodeGetChild(&self, index));
        }, nb::rv_policy::reference_internal)
        .def("__enter__", [](yoga::Node& self) -> yoga::Node& { return self; },
            nb::rv_policy::reference)
        .def("__exit__", [](yoga::Node& self, const nb::object&, const nb::object&, const nb::object&) {
            safeNodeFree(self);
        })
        .def("free", [](yoga::Node& self) { safeNodeFree(self); })
        .def("free_recursive", [](yoga::Node& self) { safeNodeFreeRecursive(self); })
        .def("reset", [](yoga::Node& self) { YGNodeReset(&self); })
        .def("copy_style", [](yoga::Node& self, const yoga::Node& src) { YGNodeCopyStyle(&self, &src); })
        .def("set_context", [](yoga::Node& self, nb::object context) {
            if (context.is_none()) {
                auto* ctx = getNodeContext(&self);
                if (ctx) {
                    ctx->user_context = nb::none();
                }
            } else {
                auto* ctx = getOrCreateNodeContext(&self);
                ctx->user_context = context;
            }
        })
        .def("get_context", [](yoga::Node& self) -> nb::object {
            auto* ctx = getNodeContext(&self);
            if (ctx && !ctx->user_context.is_none()) {
                return ctx->user_context;
            }
            return nb::none();
        })
        .def("get_config", [](yoga::Node& self) -> yoga::Config* {
            return static_cast<yoga::Config*>(const_cast<YGConfigRef>(YGNodeGetConfig(&self)));
        }, nb::rv_policy::reference)
        .def("set_config", [](yoga::Node& self, yoga::Config& config) {
            YGNodeSetConfig(&self, &config);
        })
        .def("swap_child", [](yoga::Node& self, yoga::Node& child, size_t index) {
            YGNodeSwapChild(&self, &child, index);
        }, nb::arg("child"), nb::arg("index"))
        .def("clone", [](yoga::Node& self) -> yoga::Node* {
            return static_cast<yoga::Node*>(YGNodeClone(&self));
        }, nb::rv_policy::reference)
        .def("calculate_layout", [](yoga::Node& self, float availableWidth, float availableHeight, YGDirection direction) {
            YGNodeCalculateLayout(&self, availableWidth, availableHeight, direction);
        }, nb::arg("available_width") = YGUndefined, nb::arg("available_height") = YGUndefined,
           nb::arg("direction") = YGDirectionLTR)
        .def_prop_rw("has_new_layout",
            [](yoga::Node& self) { return YGNodeGetHasNewLayout(&self); },
            [](yoga::Node& self, bool value) { YGNodeSetHasNewLayout(&self, value); })
        .def_prop_ro("is_dirty", [](yoga::Node& self) { return YGNodeIsDirty(&self); })
        .def("mark_dirty", [](yoga::Node& self) { YGNodeMarkDirty(&self); })
        .def("mark_dirty_and_propagate", [](yoga::Node& self) { self.markDirtyAndPropagate(); })
        .def("set_dirty", [](yoga::Node& self, bool value) {
            self.setDirty(value);
            YGNodeSetHasNewLayout(&self, value);
        })
        .def_prop_ro("child_count", [](yoga::Node& self) { return YGNodeGetChildCount(&self); })
        .def("get_layout_children", [](yoga::Node& self) {
            auto children = self.getLayoutChildren();
            std::vector<yoga::Node*> result;
            for (auto* child : children) {
                result.push_back(child);
            }
            return result;
        })
        .def_prop_ro("owner", [](yoga::Node& self) -> yoga::Node* {
            return static_cast<yoga::Node*>(YGNodeGetOwner(&self));
        }, nb::rv_policy::reference)
        .def_prop_ro("parent", [](yoga::Node& self) -> yoga::Node* {
            return static_cast<yoga::Node*>(YGNodeGetParent(&self));
        }, nb::rv_policy::reference)
        .def_prop_rw("direction",
            [](yoga::Node& self) { return YGNodeStyleGetDirection(&self); },
            [](yoga::Node& self, YGDirection value) { YGNodeStyleSetDirection(&self, value); })
        .def_prop_rw("flex_direction",
            [](yoga::Node& self) { return YGNodeStyleGetFlexDirection(&self); },
            [](yoga::Node& self, YGFlexDirection value) { YGNodeStyleSetFlexDirection(&self, value); })
        .def_prop_rw("justify_content",
            [](yoga::Node& self) { return YGNodeStyleGetJustifyContent(&self); },
            [](yoga::Node& self, YGJustify value) { YGNodeStyleSetJustifyContent(&self, value); })
        .def_prop_rw("align_content",
            [](yoga::Node& self) { return YGNodeStyleGetAlignContent(&self); },
            [](yoga::Node& self, YGAlign value) { YGNodeStyleSetAlignContent(&self, value); })
        .def_prop_rw("align_items",
            [](yoga::Node& self) { return YGNodeStyleGetAlignItems(&self); },
            [](yoga::Node& self, YGAlign value) { YGNodeStyleSetAlignItems(&self, value); })
        .def_prop_rw("align_self",
            [](yoga::Node& self) { return YGNodeStyleGetAlignSelf(&self); },
            [](yoga::Node& self, YGAlign value) { YGNodeStyleSetAlignSelf(&self, value); })
        .def_prop_rw("position_type",
            [](yoga::Node& self) { return YGNodeStyleGetPositionType(&self); },
            [](yoga::Node& self, YGPositionType value) { YGNodeStyleSetPositionType(&self, value); })
        .def_prop_rw("flex_wrap",
            [](yoga::Node& self) { return YGNodeStyleGetFlexWrap(&self); },
            [](yoga::Node& self, YGWrap value) { YGNodeStyleSetFlexWrap(&self, value); })
        .def_prop_rw("overflow",
            [](yoga::Node& self) { return YGNodeStyleGetOverflow(&self); },
            [](yoga::Node& self, YGOverflow value) { YGNodeStyleSetOverflow(&self, value); })
        .def_prop_rw("display",
            [](yoga::Node& self) { return YGNodeStyleGetDisplay(&self); },
            [](yoga::Node& self, YGDisplay value) { YGNodeStyleSetDisplay(&self, value); })
        .def_prop_rw("box_sizing",
            [](yoga::Node& self) { return YGNodeStyleGetBoxSizing(&self); },
            [](yoga::Node& self, YGBoxSizing value) { YGNodeStyleSetBoxSizing(&self, value); })
        .def_prop_rw("flex",
            [](yoga::Node& self) { return YGNodeStyleGetFlex(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetFlex(&self, value); })
        .def_prop_rw("flex_grow",
            [](yoga::Node& self) { return YGNodeStyleGetFlexGrow(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetFlexGrow(&self, value); })
        .def_prop_rw("flex_shrink",
            [](yoga::Node& self) { return YGNodeStyleGetFlexShrink(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetFlexShrink(&self, value); })
        .def_prop_rw("flex_basis",
            [](yoga::Node& self) { return YGNodeStyleGetFlexBasis(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetFlexBasis(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetFlexBasisPercent(&self, ygv.value);
                    } else {
                        YGNodeStyleSetFlexBasis(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetFlexBasis(&self, nb::cast<float>(value));
                }
            })
        .def_prop_rw("width",
            [](yoga::Node& self) { return YGNodeStyleGetWidth(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetWidth(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetWidthPercent(&self, ygv.value);
                    } else if (ygv.unit == YGUnitAuto) {
                        YGNodeStyleSetWidthAuto(&self);
                    } else {
                        YGNodeStyleSetWidth(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetWidth(&self, nb::cast<float>(value));
                }
            })
        .def_prop_rw("height",
            [](yoga::Node& self) { return YGNodeStyleGetHeight(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetHeight(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetHeightPercent(&self, ygv.value);
                    } else if (ygv.unit == YGUnitAuto) {
                        YGNodeStyleSetHeightAuto(&self);
                    } else {
                        YGNodeStyleSetHeight(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetHeight(&self, nb::cast<float>(value));
                }
            })
        .def("set_margin_auto", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            YGNodeStyleSetMarginAuto(&self, (YGEdge)edge);
        })
        .def("set_position_auto", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            YGNodeStyleSetPositionAuto(&self, (YGEdge)edge);
        })
        .def_prop_rw("min_width",
            [](yoga::Node& self) { return YGNodeStyleGetMinWidth(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetMinWidth(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetMinWidthPercent(&self, ygv.value);
                    } else {
                        YGNodeStyleSetMinWidth(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetMinWidth(&self, nb::cast<float>(value));
                }
            })
        .def_prop_rw("min_height",
            [](yoga::Node& self) { return YGNodeStyleGetMinHeight(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetMinHeight(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetMinHeightPercent(&self, ygv.value);
                    } else {
                        YGNodeStyleSetMinHeight(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetMinHeight(&self, nb::cast<float>(value));
                }
            })
        .def_prop_rw("max_width",
            [](yoga::Node& self) { return YGNodeStyleGetMaxWidth(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetMaxWidth(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetMaxWidthPercent(&self, ygv.value);
                    } else {
                        YGNodeStyleSetMaxWidth(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetMaxWidth(&self, nb::cast<float>(value));
                }
            })
        .def_prop_rw("max_height",
            [](yoga::Node& self) { return YGNodeStyleGetMaxHeight(&self); },
            [](yoga::Node& self, nb::object value) {
                if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                    YGNodeStyleSetMaxHeight(&self, nb::cast<float>(value));
                } else if (nb::isinstance<YGValue>(value)) {
                    const YGValue& ygv = nb::cast<const YGValue&>(value);
                    if (ygv.unit == YGUnitPercent) {
                        YGNodeStyleSetMaxHeightPercent(&self, ygv.value);
                    } else {
                        YGNodeStyleSetMaxHeight(&self, ygv.value);
                    }
                } else {
                    YGNodeStyleSetMaxHeight(&self, nb::cast<float>(value));
                }
            })
        .def_prop_rw("aspect_ratio",
            [](yoga::Node& self) { return YGNodeStyleGetAspectRatio(&self); },
            [](yoga::Node& self, float value) { YGNodeStyleSetAspectRatio(&self, value); })
        .def_prop_ro("layout_left", [](yoga::Node& self) { return YGNodeLayoutGetLeft(&self); })
        .def_prop_ro("layout_top", [](yoga::Node& self) { return YGNodeLayoutGetTop(&self); })
        .def_prop_ro("layout_right", [](yoga::Node& self) { return YGNodeLayoutGetRight(&self); })
        .def_prop_ro("layout_bottom", [](yoga::Node& self) { return YGNodeLayoutGetBottom(&self); })
        .def_prop_ro("layout_width", [](yoga::Node& self) { return YGNodeLayoutGetWidth(&self); })
        .def_prop_ro("layout_height", [](yoga::Node& self) { return YGNodeLayoutGetHeight(&self); })
        .def_prop_ro("layout_direction", [](yoga::Node& self) { return YGNodeLayoutGetDirection(&self); })
        .def_prop_ro("layout_had_overflow", [](yoga::Node& self) { return YGNodeLayoutGetHadOverflow(&self); })
        .def_prop_ro("layout_raw_width", [](yoga::Node& self) { return YGNodeLayoutGetRawWidth(&self); })
        .def_prop_ro("layout_raw_height", [](yoga::Node& self) { return YGNodeLayoutGetRawHeight(&self); })
        .def("get_margin", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeStyleGetMargin(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("get_padding", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeStyleGetPadding(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("get_border", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeStyleGetBorder(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("get_position", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeStyleGetPosition(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("set_position", [](yoga::Node& self, nb::object edge_obj, nb::object value) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                YGNodeStyleSetPosition(&self, (YGEdge)edge, nb::cast<float>(value));
            } else if (nb::isinstance<YGValue>(value)) {
                const YGValue& ygv = nb::cast<const YGValue&>(value);
                if (ygv.unit == YGUnitPercent) {
                    YGNodeStyleSetPositionPercent(&self, (YGEdge)edge, ygv.value);
                } else {
                    YGNodeStyleSetPosition(&self, (YGEdge)edge, ygv.value);
                }
            } else {
                YGNodeStyleSetPosition(&self, (YGEdge)edge, nb::cast<float>(value));
            }
        }, nb::arg("edge"), nb::arg("value"))
        .def("set_margin", [](yoga::Node& self, nb::object edge_obj, nb::object value) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                YGNodeStyleSetMargin(&self, (YGEdge)edge, nb::cast<float>(value));
            } else if (nb::isinstance<YGValue>(value)) {
                const YGValue& ygv = nb::cast<const YGValue&>(value);
                if (ygv.unit == YGUnitPercent) {
                    YGNodeStyleSetMarginPercent(&self, (YGEdge)edge, ygv.value);
                } else if (ygv.unit == YGUnitAuto) {
                    YGNodeStyleSetMarginAuto(&self, (YGEdge)edge);
                } else {
                    YGNodeStyleSetMargin(&self, (YGEdge)edge, ygv.value);
                }
            } else {
                YGNodeStyleSetMargin(&self, (YGEdge)edge, nb::cast<float>(value));
            }
        }, nb::arg("edge"), nb::arg("value"))
        .def("set_padding", [](yoga::Node& self, nb::object edge_obj, nb::object value) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                YGNodeStyleSetPadding(&self, (YGEdge)edge, nb::cast<float>(value));
            } else if (nb::isinstance<YGValue>(value)) {
                const YGValue& ygv = nb::cast<const YGValue&>(value);
                if (ygv.unit == YGUnitPercent) {
                    YGNodeStyleSetPaddingPercent(&self, (YGEdge)edge, ygv.value);
                } else {
                    YGNodeStyleSetPadding(&self, (YGEdge)edge, ygv.value);
                }
            } else {
                YGNodeStyleSetPadding(&self, (YGEdge)edge, nb::cast<float>(value));
            }
        }, nb::arg("edge"), nb::arg("value"))
        .def("set_border", [](yoga::Node& self, nb::object edge_obj, nb::object value) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                YGNodeStyleSetBorder(&self, (YGEdge)edge, nb::cast<float>(value));
            } else if (nb::isinstance<YGValue>(value)) {
                const YGValue& ygv = nb::cast<const YGValue&>(value);
                YGNodeStyleSetBorder(&self, (YGEdge)edge, ygv.value);
            } else {
                YGNodeStyleSetBorder(&self, (YGEdge)edge, nb::cast<float>(value));
            }
        }, nb::arg("edge"), nb::arg("value"))
        .def("set_gap", [](yoga::Node& self, nb::object gutter_obj, nb::object value) {
            int gutter = nb::isinstance<YGGutter>(gutter_obj) ? nb::cast<int>(gutter_obj.attr("value")) : nb::cast<int>(gutter_obj);
            if (nb::isinstance<nb::int_>(value) || nb::isinstance<nb::float_>(value)) {
                YGNodeStyleSetGap(&self, (YGGutter)gutter, nb::cast<float>(value));
            } else if (nb::isinstance<YGValue>(value)) {
                const YGValue& ygv = nb::cast<const YGValue&>(value);
                if (ygv.unit == YGUnitPercent) {
                    YGNodeStyleSetGapPercent(&self, (YGGutter)gutter, ygv.value);
                } else {
                    YGNodeStyleSetGap(&self, (YGGutter)gutter, ygv.value);
                }
            } else {
                YGNodeStyleSetGap(&self, (YGGutter)gutter, nb::cast<float>(value));
            }
        }, nb::arg("gutter"), nb::arg("value"))
        .def("set_gap_percent", [](yoga::Node& self, nb::object gutter_obj, float value) {
            int gutter = nb::isinstance<YGGutter>(gutter_obj) ? nb::cast<int>(gutter_obj.attr("value")) : nb::cast<int>(gutter_obj);
            YGNodeStyleSetGapPercent(&self, (YGGutter)gutter, value);
        }, nb::arg("gutter"), nb::arg("value"))
        .def("insert_child", [](yoga::Node& self, yoga::Node& child, size_t index) { YGNodeInsertChild(&self, &child, index); }, nb::arg("child"), nb::arg("index"))
        .def("remove_child", [](yoga::Node& self, yoga::Node& child) { YGNodeRemoveChild(&self, &child); }, nb::arg("child"))
        .def("remove_all_children", [](yoga::Node& self) { YGNodeRemoveAllChildren(&self); })
        .def("set_children", [](yoga::Node& self, const std::vector<yoga::Node*>& children) {
            // Clear owner for old children that are owned by self and not in the new list
            for (size_t i = 0; i < self.getChildCount(); i++) {
                auto* oldChild = self.getChild(i);
                if (oldChild->getOwner() == &self) {
                    bool inNewList = false;
                    for (auto* newChild : children) {
                        if (newChild == oldChild) { inNewList = true; break; }
                    }
                    if (!inNewList) {
                        oldChild->setOwner(nullptr);
                    }
                }
            }
            self.setChildren(children);
            // Only set owner for children that have no owner (unowned).
            // Children with a different owner are "shared" and keep their
            // original owner - this enables yoga's clone-on-write mechanism.
            for (auto* child : children) {
                if (child->getOwner() == nullptr) {
                    child->setOwner(&self);
                }
            }
            self.markDirtyAndPropagate();
        }, nb::arg("children"))
        .def("set_measure_func", [](yoga::Node& self, nb::object callback) {
            auto* ctx = getOrCreateNodeContext(&self);
            if (callback.is_none()) {
                ctx->measure_callback = nb::none();
                YGNodeSetMeasureFunc(&self, nullptr);
            } else {
                ctx->measure_callback = callback;
                YGNodeSetMeasureFunc(&self, yogaMeasureCallback);
            }
        }, nb::arg("func") = nb::none())
        .def("has_measure_func", [](yoga::Node& self) { return YGNodeHasMeasureFunc(&self); })
        .def("set_baseline_func", [](yoga::Node& self, nb::object callback) {
            auto* ctx = getOrCreateNodeContext(&self);
            if (callback.is_none()) {
                ctx->baseline_callback = nb::none();
                YGNodeSetBaselineFunc(&self, nullptr);
            } else {
                ctx->baseline_callback = callback;
                YGNodeSetBaselineFunc(&self, yogaBaselineCallback);
            }
        }, nb::arg("func") = nb::none())
        .def("has_baseline_func", [](yoga::Node& self) { return YGNodeHasBaselineFunc(&self); })
        .def("set_dirtied_func", [](yoga::Node& self, nb::object callback) {
            auto* ctx = getOrCreateNodeContext(&self);
            if (callback.is_none()) {
                ctx->dirtied_callback = nb::none();
                YGNodeSetDirtiedFunc(&self, nullptr);
            } else {
                ctx->dirtied_callback = callback;
                YGNodeSetDirtiedFunc(&self, yogaDirtiedCallback);
            }
        }, nb::arg("func") = nb::none())
        .def("has_dirtied_func", [](yoga::Node& self) { return YGNodeGetDirtiedFunc(&self) != nullptr; })
        .def("measure", [](yoga::Node& self, float width, nb::object widthModeObj, float height, nb::object heightModeObj) -> nb::tuple {
            int widthMode = nb::isinstance<YGMeasureMode>(widthModeObj) ? nb::cast<int>(widthModeObj.attr("value")) : nb::cast<int>(widthModeObj);
            int heightMode = nb::isinstance<YGMeasureMode>(heightModeObj) ? nb::cast<int>(heightModeObj.attr("value")) : nb::cast<int>(heightModeObj);
            auto* ctx = getNodeContext(&self);
            if (!ctx || ctx->measure_callback.is_none()) {
                return nb::make_tuple(YGUndefined, YGUndefined);
            }
            nb::gil_scoped_acquire acquire;
            try {
                nb::object result = ctx->measure_callback(&self, width, widthMode, height, heightMode);
                if (nb::isinstance<nb::dict>(result)) {
                    nb::dict d = nb::cast<nb::dict>(result);
                    float w = nb::cast<float>(d["width"]);
                    float h = nb::cast<float>(d["height"]);
                    return nb::make_tuple(w, h);
                } else if (nb::isinstance<nb::tuple>(result)) {
                    nb::tuple t = nb::cast<nb::tuple>(result);
                    if (nb::len(t) >= 2) {
                        float w = nb::cast<float>(t[0]);
                        float h = nb::cast<float>(t[1]);
                        return nb::make_tuple(w, h);
                    }
                }
            } catch (...) {
            }
            return nb::make_tuple(YGUndefined, YGUndefined);
        })
        .def("baseline", [](yoga::Node& self, float width, float height) -> float {
            auto* ctx = getNodeContext(&self);
            if (!ctx || ctx->baseline_callback.is_none()) {
                return height;
            }
            nb::gil_scoped_acquire acquire;
            try {
                return nb::cast<float>(ctx->baseline_callback(&self, width, height));
            } catch (...) {
            }
            return height;
        })
        .def_prop_rw("node_type",
            [](yoga::Node& self) { return YGNodeGetNodeType(&self); },
            [](yoga::Node& self, YGNodeType value) { YGNodeSetNodeType(&self, value); })
        .def_prop_rw("is_reference_baseline",
            [](yoga::Node& self) { return YGNodeIsReferenceBaseline(&self); },
            [](yoga::Node& self, bool value) { YGNodeSetIsReferenceBaseline(&self, value); })
        .def_prop_rw("always_forms_containing_block",
            [](yoga::Node& self) { return YGNodeGetAlwaysFormsContainingBlock(&self); },
            [](yoga::Node& self, bool value) { YGNodeSetAlwaysFormsContainingBlock(&self, value); })
        .def("set_margin_percent", [](yoga::Node& self, nb::object edge_obj, float value) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            YGNodeStyleSetMarginPercent(&self, (YGEdge)edge, value);
        }, nb::arg("edge"), nb::arg("value"))
        .def("set_padding_percent", [](yoga::Node& self, nb::object edge_obj, float value) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            YGNodeStyleSetPaddingPercent(&self, (YGEdge)edge, value);
        }, nb::arg("edge"), nb::arg("value"))
        .def("layout_margin", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeLayoutGetMargin(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("layout_padding", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeLayoutGetPadding(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("layout_border", [](yoga::Node& self, nb::object edge_obj) {
            int edge = nb::isinstance<YGEdge>(edge_obj) ? nb::cast<int>(edge_obj.attr("value")) : nb::cast<int>(edge_obj);
            return YGNodeLayoutGetBorder(&self, (YGEdge)edge);
        }, nb::arg("edge"))
        .def("set_width_auto", [](yoga::Node& self) { YGNodeStyleSetWidthAuto(&self); })
        .def("set_width_percent", [](yoga::Node& self, float value) { YGNodeStyleSetWidthPercent(&self, value); })
        .def("set_width_fit_content", [](yoga::Node& self) { YGNodeStyleSetWidthFitContent(&self); })
        .def("set_width_max_content", [](yoga::Node& self) { YGNodeStyleSetWidthMaxContent(&self); })
        .def("set_width_stretch", [](yoga::Node& self) { YGNodeStyleSetWidthStretch(&self); })
        .def("set_height_auto", [](yoga::Node& self) { YGNodeStyleSetHeightAuto(&self); })
        .def("set_height_percent", [](yoga::Node& self, float value) { YGNodeStyleSetHeightPercent(&self, value); })
        .def("set_height_fit_content", [](yoga::Node& self) { YGNodeStyleSetHeightFitContent(&self); })
        .def("set_height_max_content", [](yoga::Node& self) { YGNodeStyleSetHeightMaxContent(&self); })
        .def("set_height_stretch", [](yoga::Node& self) { YGNodeStyleSetHeightStretch(&self); })
        .def("set_min_width_percent", [](yoga::Node& self, float value) { YGNodeStyleSetMinWidthPercent(&self, value); })
        .def("set_min_width_fit_content", [](yoga::Node& self) { YGNodeStyleSetMinWidthFitContent(&self); })
        .def("set_min_width_max_content", [](yoga::Node& self) { YGNodeStyleSetMinWidthMaxContent(&self); })
        .def("set_min_width_stretch", [](yoga::Node& self) { YGNodeStyleSetMinWidthStretch(&self); })
        .def("set_min_height_percent", [](yoga::Node& self, float value) { YGNodeStyleSetMinHeightPercent(&self, value); })
        .def("set_min_height_fit_content", [](yoga::Node& self) { YGNodeStyleSetMinHeightFitContent(&self); })
        .def("set_min_height_max_content", [](yoga::Node& self) { YGNodeStyleSetMinHeightMaxContent(&self); })
        .def("set_min_height_stretch", [](yoga::Node& self) { YGNodeStyleSetMinHeightStretch(&self); })
        .def("set_max_width_percent", [](yoga::Node& self, float value) { YGNodeStyleSetMaxWidthPercent(&self, value); })
        .def("set_max_width_fit_content", [](yoga::Node& self) { YGNodeStyleSetMaxWidthFitContent(&self); })
        .def("set_max_width_max_content", [](yoga::Node& self) { YGNodeStyleSetMaxWidthMaxContent(&self); })
        .def("set_max_width_stretch", [](yoga::Node& self) { YGNodeStyleSetMaxWidthStretch(&self); })
        .def("set_max_height_percent", [](yoga::Node& self, float value) { YGNodeStyleSetMaxHeightPercent(&self, value); })
        .def("set_max_height_fit_content", [](yoga::Node& self) { YGNodeStyleSetMaxHeightFitContent(&self); })
        .def("set_max_height_max_content", [](yoga::Node& self) { YGNodeStyleSetMaxHeightMaxContent(&self); })
        .def("set_max_height_stretch", [](yoga::Node& self) { YGNodeStyleSetMaxHeightStretch(&self); })
        .def("set_flex_basis_fit_content", [](yoga::Node& self) { YGNodeStyleSetFlexBasisFitContent(&self); })
        .def("set_flex_basis_max_content", [](yoga::Node& self) { YGNodeStyleSetFlexBasisMaxContent(&self); })
        .def("set_flex_basis_stretch", [](yoga::Node& self) { YGNodeStyleSetFlexBasisStretch(&self); })
        .def("_node_id", [](yoga::Node& self) -> uintptr_t { return reinterpret_cast<uintptr_t>(&self); });

    // Clean up all Python-side resources during module teardown.
    // Using a capsule ensures cleanup runs when the module dict is cleared,
    // before nanobind's leak checker fires.
    m.attr("_cleanup") = nb::capsule((void*)0x1, [](void*) noexcept {
        // Reset event subscribers (releases captured Python callbacks)
        yoga::Event::reset();

        // Clean up any remaining NodeContexts (releases Python callbacks)
        for (auto* ctx : allNodeContexts) {
            delete ctx;
        }
        allNodeContexts.clear();

        // Clean up any remaining CloneContexts (releases Python callbacks)
        for (auto* ctx : allCloneContexts) {
            delete ctx;
        }
        allCloneContexts.clear();

        nanobindManagedNodes.clear();
    });
}
