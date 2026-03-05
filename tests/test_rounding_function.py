import math
import pytest
import yoga
from yoga import (
    Node,
    Config,
    Direction,
    Edge,
    YGValuePoint,
)


class TestRoundingFunction:
    def test_rounding_value(self):
        round_value = yoga.round_value_to_pixel_grid

        # Test that whole numbers are rounded to whole despite ceil/floor flags
        assert round_value(6.000001, 2.0, False, False) == 6.0
        assert round_value(6.000001, 2.0, True, False) == 6.0
        assert round_value(6.000001, 2.0, False, True) == 6.0
        assert round_value(5.999999, 2.0, False, False) == 6.0
        assert round_value(5.999999, 2.0, True, False) == 6.0
        assert round_value(5.999999, 2.0, False, True) == 6.0

        # Same tests for negative numbers
        assert round_value(-6.000001, 2.0, False, False) == -6.0
        assert round_value(-6.000001, 2.0, True, False) == -6.0
        assert round_value(-6.000001, 2.0, False, True) == -6.0
        assert round_value(-5.999999, 2.0, False, False) == -6.0
        assert round_value(-5.999999, 2.0, True, False) == -6.0
        assert round_value(-5.999999, 2.0, False, True) == -6.0

        # Test that numbers with fraction are rounded correctly accounting for
        # ceil/floor flags
        assert round_value(6.01, 2.0, False, False) == 6.0
        assert round_value(6.01, 2.0, True, False) == 6.5
        assert round_value(6.01, 2.0, False, True) == 6.0
        assert round_value(5.99, 2.0, False, False) == 6.0
        assert round_value(5.99, 2.0, True, False) == 6.0
        assert round_value(5.99, 2.0, False, True) == 5.5

        # Same tests for negative numbers
        assert round_value(-6.01, 2.0, False, False) == -6.0
        assert round_value(-6.01, 2.0, True, False) == -6.0
        assert round_value(-6.01, 2.0, False, True) == -6.5
        assert round_value(-5.99, 2.0, False, False) == -6.0
        assert round_value(-5.99, 2.0, True, False) == -5.5
        assert round_value(-5.99, 2.0, False, True) == -6.0

        # Rounding up/down halfway values is as expected for both positive and
        # negative numbers
        assert round_value(-3.5, 1.0, False, False) == -3
        assert round_value(-3.4, 1.0, False, False) == -3
        assert round_value(-3.6, 1.0, False, False) == -4
        assert round_value(-3.499999, 1.0, False, False) == -3
        assert round_value(-3.500001, 1.0, False, False) == -3
        assert round_value(-3.5001, 1.0, False, False) == -4

        assert round_value(-3.5, 1.0, True, False) == -3
        assert round_value(-3.4, 1.0, True, False) == -3
        assert round_value(-3.6, 1.0, True, False) == -3
        assert round_value(-3.499999, 1.0, True, False) == -3
        assert round_value(-3.500001, 1.0, True, False) == -3
        assert round_value(-3.5001, 1.0, True, False) == -3
        assert round_value(-3.00001, 1.0, True, False) == -3
        assert round_value(-3, 1.0, True, False) == -3

        assert round_value(-3.5, 1.0, False, True) == -4
        assert round_value(-3.4, 1.0, False, True) == -4
        assert round_value(-3.6, 1.0, False, True) == -4
        assert round_value(-3.499999, 1.0, False, True) == -4
        assert round_value(-3.500001, 1.0, False, True) == -4
        assert round_value(-3.5001, 1.0, False, True) == -4
        assert round_value(-3.00001, 1.0, False, True) == -3
        assert round_value(-3, 1.0, False, True) == -3

        # NAN is treated as expected:
        assert math.isnan(round_value(float("nan"), 1.5, False, False))
        assert math.isnan(round_value(1.5, float("nan"), False, False))
        assert math.isnan(round_value(float("nan"), float("nan"), False, False))

    def test_consistent_rounding_during_repeated_layouts(self):
        def measure_text(node, width, width_mode, height, height_mode):
            return {"width": 10, "height": 10}

        config = Config()
        config.point_scale_factor = 2.0

        root = Node(config)
        root.set_margin(Edge.Top, -1.49)
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        node0 = Node(config)
        root.insert_child(node0, 0)

        node1 = Node(config)
        node1.set_measure_func(measure_text)
        node0.insert_child(node1, 0)

        for i in range(5):
            root.set_margin(Edge.Left, i + 1)
            root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
            assert node1.layout_height == 10

    def test_per_node_point_scale_factor(self):
        config1 = Config()
        config1.point_scale_factor = 2.0

        config2 = Config()
        config2.point_scale_factor = 1.0

        config3 = Config()
        config3.point_scale_factor = 0.5

        root = Node(config1)
        root.width = YGValuePoint(11.5)
        root.height = YGValuePoint(11.5)

        node0 = Node(config2)
        node0.width = YGValuePoint(9.5)
        node0.height = YGValuePoint(9.5)
        root.insert_child(node0, 0)

        node1 = Node(config3)
        node1.width = YGValuePoint(7)
        node1.height = YGValuePoint(7)
        node0.insert_child(node1, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_width == 11.5
        assert root.layout_height == 11.5

        assert node0.layout_width == 10
        assert node0.layout_height == 10

        assert node1.layout_width == 8
        assert node1.layout_height == 8

    def test_raw_layout_dimensions(self):
        config = Config()
        config.point_scale_factor = 0.5

        root = Node(config)
        root.width = YGValuePoint(11.5)
        root.height = YGValuePoint(9.5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_width == 12.0
        assert root.layout_height == 10.0
        assert root.layout_raw_width == 11.5
        assert root.layout_raw_height == 9.5
