import pytest
from yoga import (
    Node,
    Config,
    Direction,
    PositionType,
    YGValuePoint,
    YGValuePercent,
    Edge,
    Justify,
    Align,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestPadding:
    def test_padding_no_size(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 10)
        root.set_padding(Edge.Top, 10)
        root.set_padding(Edge.Right, 10)
        root.set_padding(Edge.Bottom, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 20)
        assert_float_approx(root.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 20)
        assert_float_approx(root.layout_height, 20)

    def test_padding_container_match_child(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 10)
        root.set_padding(Edge.Top, 10)
        root.set_padding(Edge.Right, 10)
        root.set_padding(Edge.Bottom, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 30)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 30)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_padding_flex_child(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 10)
        root.set_padding(Edge.Top, 10)
        root.set_padding(Edge.Right, 10)
        root.set_padding(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 80)

    def test_padding_stretch_child(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 10)
        root.set_padding(Edge.Top, 10)
        root.set_padding(Edge.Right, 10)
        root.set_padding(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 10)

    def test_padding_center_child(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Start, 10)
        root.set_padding(Edge.End, 20)
        root.set_padding(Edge.Bottom, 20)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 40)
        assert_float_approx(root_child0.layout_top, 35)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 35)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_child_with_padding_align_end(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.FlexEnd
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 20)
        root_child0.set_padding(Edge.Top, 20)
        root_child0.set_padding(Edge.Right, 20)
        root_child0.set_padding(Edge.Bottom, 20)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

    def test_physical_and_relative_edge_defined(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 20)
        root.set_padding(Edge.End, 50)
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(100)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 130)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)
