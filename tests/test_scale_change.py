import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Align,
    YGValuePoint,
    Errata,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"



@pytest.mark.skip(reason="nanobind pytest crash: clone() + free_recursive() causes abort. Works in regular Python.")
class TestScaleChange:
    def test_scale_change_invalidates_layout(self):
        config = Config()
        root = Node(config)

        config.point_scale_factor = 1.0

        root.flex_direction = FlexDirection.Row
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child1.layout_left, 25)

        config.point_scale_factor = 1.5
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        # Left should change due to pixel alignment of new scale factor
        assert_float_approx(root_child1.layout_left, 25.333334)

        root.free_recursive()

    def test_errata_config_change_relayout(self):
        config = Config()
        config.errata = Errata.StretchFlexBasis

        root = Node(config)
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.align_items = Align.FlexStart
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.flex_grow = 1
        root_child0_child0_child0.flex_shrink = 1
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 500)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0.layout_height, 500)

        config.errata = Errata.None_
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        # This should be modified by the lack of the errata
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        # This should be modified by the lack of the errata
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 0)
        # This should be modified by the lack of the errata
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

        root.free_recursive()

    def test_setting_compatible_config_maintains_layout_cache(self):
        measure_call_count = [0]

        def measure_custom(node, width, width_mode, height, height_mode):
            measure_call_count[0] += 1
            return {"width": 25.0, "height": 25.0}

        config = Config()

        root = Node(config)
        config.point_scale_factor = 1.0

        root.flex_direction = FlexDirection.Row
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        assert measure_call_count[0] == 0

        root_child0.set_measure_func(measure_custom)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_call_count[0] == 1
        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child1.layout_left, 25)

        config2 = Config()
        # Calling set_point_scale_factor multiple times ensures that config2
        # gets a different config version than config1
        config2.point_scale_factor = 1.0
        config2.point_scale_factor = 1.5
        config2.point_scale_factor = 1.0

        root.set_config(config2)
        root_child0.set_config(config2)
        root_child1.set_config(config2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        # Measure should not be called again, as layout should have been cached since
        # config is functionally the same as before
        assert measure_call_count[0] == 1
        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child1.layout_left, 25)

        root.free_recursive()
