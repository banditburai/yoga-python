import pytest
from yoga import (
    Node,
    Config,
    Direction,
    PositionType,
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


def _make_measure_floor():
    def measure(node, width, width_mode, height, height_mode):
        return {"width": 10.2, "height": 10.2}

    return measure


def _make_measure_ceil():
    def measure(node, width, width_mode, height, height_mode):
        return {"width": 10.5, "height": 10.5}

    return measure


def _make_measure_fractial():
    def measure(node, width, width_mode, height, height_mode):
        return {"width": 0.5, "height": 0.5}

    return measure


class TestRoundingMeasure:
    def test_rounding_feature_with_custom_measure_func_floor(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_floor())
        root.insert_child(root_child0, 0)

        config.point_scale_factor = 0.0

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_width, 10.2)
        assert_float_approx(root_child0.layout_height, 10.2)

        config.point_scale_factor = 1.0

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_width == 11
        assert root_child0.layout_height == 11

        config.point_scale_factor = 2.0

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_width, 10.5)
        assert_float_approx(root_child0.layout_height, 10.5)

        config.point_scale_factor = 4.0

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_width, 10.25)
        assert_float_approx(root_child0.layout_height, 10.25)

        config.point_scale_factor = 1.0 / 3.0

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_width, 12.0)
        assert_float_approx(root_child0.layout_height, 12.0)

    def test_rounding_feature_with_custom_measure_func_ceil(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_ceil())
        root.insert_child(root_child0, 0)

        config.point_scale_factor = 1.0

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_width == 11
        assert root_child0.layout_height == 11

    def test_rounding_feature_with_custom_measure_and_fractial_matching_scale(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_position(Edge.Left, 73.625)
        root_child0.position_type = PositionType.Relative
        root_child0.set_measure_func(_make_measure_fractial())
        root.insert_child(root_child0, 0)

        config.point_scale_factor = 2.0

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_width, 0.5)
        assert_float_approx(root_child0.layout_height, 0.5)
        assert_float_approx(root_child0.layout_left, 73.5)
