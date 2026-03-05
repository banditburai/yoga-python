import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestEdge:
    def test_start_overrides(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Start, 10)
        root_child0.set_margin(Edge.Left, 20)
        root_child0.set_margin(Edge.Right, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_right, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)
        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_right, 10)

    def test_end_overrides(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.End, 10)
        root_child0.set_margin(Edge.Left, 20)
        root_child0.set_margin(Edge.Right, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_right, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)
        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_right, 20)

    def test_horizontal_overridden(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Horizontal, 10)
        root_child0.set_margin(Edge.Left, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_right, 10)

    def test_vertical_overridden(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Column
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Vertical, 10)
        root_child0.set_margin(Edge.Top, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_bottom, 10)

    def test_horizontal_overrides_all(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Column
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Horizontal, 10)
        root_child0.set_margin(Edge.All, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_right, 10)
        assert_float_approx(root_child0.layout_bottom, 20)

    def test_vertical_overrides_all(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Column
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Vertical, 10)
        root_child0.set_margin(Edge.All, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_right, 20)
        assert_float_approx(root_child0.layout_bottom, 10)

    def test_all_overridden(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Column
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Right, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root_child0.set_margin(Edge.All, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_right, 10)
        assert_float_approx(root_child0.layout_bottom, 10)
