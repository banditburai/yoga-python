import pytest
from yoga import (
    Node,
    Config,
    Direction,
    PositionType,
    YGValuePoint,
    YGValuePercent,
    Edge,
    FlexDirection,
    BoxSizing,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestBoxSizing:
    def test_box_sizing_content_box_simple(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 130)
        assert_float_approx(root.layout_height, 130)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 130)
        assert_float_approx(root.layout_height, 130)

    def test_box_sizing_border_box_simple(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_content_box_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 4)
        root_child0.set_padding(Edge.Top, 4)
        root_child0.set_padding(Edge.Right, 4)
        root_child0.set_padding(Edge.Bottom, 4)
        root_child0.set_border(Edge.Left, 16)
        root_child0.set_border(Edge.Top, 16)
        root_child0.set_border(Edge.Right, 16)
        root_child0.set_border(Edge.Bottom, 16)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePercent(25)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 65)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 65)

    def test_box_sizing_border_box_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 4)
        root_child0.set_padding(Edge.Top, 4)
        root_child0.set_padding(Edge.Right, 4)
        root_child0.set_padding(Edge.Bottom, 4)
        root_child0.set_border(Edge.Left, 16)
        root_child0.set_border(Edge.Top, 16)
        root_child0.set_border(Edge.Right, 16)
        root_child0.set_border(Edge.Bottom, 16)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePercent(25)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

    def test_box_sizing_content_box_absolute(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_padding(Edge.Left, 12)
        root_child0.set_padding(Edge.Top, 12)
        root_child0.set_padding(Edge.Right, 12)
        root_child0.set_padding(Edge.Bottom, 12)
        root_child0.set_border(Edge.Left, 8)
        root_child0.set_border(Edge.Top, 8)
        root_child0.set_border(Edge.Right, 8)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.height = YGValuePercent(25)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 65)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 65)

    def test_box_sizing_border_box_absolute(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_padding(Edge.Left, 12)
        root_child0.set_padding(Edge.Top, 12)
        root_child0.set_padding(Edge.Right, 12)
        root_child0.set_padding(Edge.Bottom, 12)
        root_child0.set_border(Edge.Left, 8)
        root_child0.set_border(Edge.Top, 8)
        root_child0.set_border(Edge.Right, 8)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.height = YGValuePercent(25)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 40)

    def test_box_sizing_content_box_comtaining_block(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 12)
        root.set_padding(Edge.Top, 12)
        root.set_padding(Edge.Right, 12)
        root.set_padding(Edge.Bottom, 12)
        root.set_border(Edge.Left, 8)
        root.set_border(Edge.Top, 8)
        root.set_border(Edge.Right, 8)
        root.set_border(Edge.Bottom, 8)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePercent(25)
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 140)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 31)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 140)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 31)

    def test_box_sizing_border_box_comtaining_block(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 12)
        root.set_padding(Edge.Top, 12)
        root.set_padding(Edge.Right, 12)
        root.set_padding(Edge.Bottom, 12)
        root.set_border(Edge.Left, 8)
        root.set_border(Edge.Top, 8)
        root.set_border(Edge.Right, 8)
        root.set_border(Edge.Bottom, 8)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePercent(25)
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 21)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 21)

    def test_box_sizing_content_box_padding_only(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 110)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 110)

    def test_box_sizing_content_box_padding_only_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(150)

        root_child0 = Node(config)
        root_child0.set_padding_percent(Edge.Left, 10)
        root_child0.set_padding_percent(Edge.Top, 10)
        root_child0.set_padding_percent(Edge.Right, 10)
        root_child0.set_padding_percent(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(75)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 70)
        assert_float_approx(root_child0.layout_height, 95)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 70)
        assert_float_approx(root_child0.layout_height, 95)

    def test_box_sizing_border_box_padding_only(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_padding_only_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(150)

        root_child0 = Node(config)
        root_child0.set_padding_percent(Edge.Left, 10)
        root_child0.set_padding_percent(Edge.Top, 10)
        root_child0.set_padding_percent(Edge.Right, 10)
        root_child0.set_padding_percent(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(75)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 75)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 75)

    def test_box_sizing_content_box_border_only(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 120)
        assert_float_approx(root.layout_height, 120)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 120)
        assert_float_approx(root.layout_height, 120)

    def test_box_sizing_content_box_border_only_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

    def test_box_sizing_border_box_border_only(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_border_only_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

    def test_box_sizing_content_box_no_padding_no_border(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_no_padding_no_border(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_content_box_children(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(25)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(25)
        root_child3.height = YGValuePoint(25)
        root.insert_child(root_child3, 3)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 130)
        assert_float_approx(root.layout_height, 130)

        assert_float_approx(root_child0.layout_left, 15)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 15)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 15)
        assert_float_approx(root_child2.layout_top, 65)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 15)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 130)
        assert_float_approx(root.layout_height, 130)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 65)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 90)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

    def test_box_sizing_border_box_children(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(25)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(25)
        root_child3.height = YGValuePoint(25)
        root.insert_child(root_child3, 3)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 15)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 15)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 15)
        assert_float_approx(root_child2.layout_top, 65)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 15)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 65)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 60)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

    def test_box_sizing_content_box_siblings(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(25)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_padding(Edge.Left, 10)
        root_child1.set_padding(Edge.Top, 10)
        root_child1.set_padding(Edge.Right, 10)
        root_child1.set_padding(Edge.Bottom, 10)
        root_child1.set_border(Edge.Left, 10)
        root_child1.set_border(Edge.Top, 10)
        root_child1.set_border(Edge.Right, 10)
        root_child1.set_border(Edge.Bottom, 10)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root_child1.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(25)
        root_child3.height = YGValuePoint(25)
        root.insert_child(root_child3, 3)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 25)
        assert_float_approx(root_child1.layout_width, 65)
        assert_float_approx(root_child1.layout_height, 65)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 90)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 115)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 35)
        assert_float_approx(root_child1.layout_top, 25)
        assert_float_approx(root_child1.layout_width, 65)
        assert_float_approx(root_child1.layout_height, 65)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 90)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 75)
        assert_float_approx(root_child3.layout_top, 115)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

    def test_box_sizing_border_box_siblings(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(25)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_padding(Edge.Left, 10)
        root_child1.set_padding(Edge.Top, 10)
        root_child1.set_padding(Edge.Right, 10)
        root_child1.set_padding(Edge.Bottom, 10)
        root_child1.set_border(Edge.Left, 10)
        root_child1.set_border(Edge.Top, 10)
        root_child1.set_border(Edge.Right, 10)
        root_child1.set_border(Edge.Bottom, 10)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(25)
        root_child3.height = YGValuePoint(25)
        root.insert_child(root_child3, 3)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 25)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 40)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 65)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 25)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 25)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 40)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 65)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 25)

        assert_float_approx(root_child3.layout_left, 75)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 25)
        assert_float_approx(root_child3.layout_height, 25)

    def test_box_sizing_content_box_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.max_width = YGValuePoint(50)
        root_child0.height = YGValuePoint(25)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 65)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 65)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_border_box_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.max_width = YGValuePoint(50)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_content_box_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.width = YGValuePoint(50)
        root_child0.max_height = YGValuePoint(50)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_border_box_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.width = YGValuePoint(50)
        root_child0.max_height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_content_box_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.min_width = YGValuePoint(50)
        root_child0.height = YGValuePoint(25)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 65)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 65)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_border_box_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.min_width = YGValuePoint(50)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_content_box_min_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.width = YGValuePoint(50)
        root_child0.min_height = YGValuePoint(50)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 90)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 90)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_border_box_min_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 15)
        root_child0.set_border(Edge.Top, 15)
        root_child0.set_border(Edge.Right, 15)
        root_child0.set_border(Edge.Bottom, 15)
        root_child0.width = YGValuePoint(50)
        root_child0.min_height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(25)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 25)

    def test_box_sizing_content_box_no_height_no_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 2)
        root_child0.set_padding(Edge.Right, 2)
        root_child0.set_padding(Edge.Bottom, 2)
        root_child0.set_border(Edge.Left, 7)
        root_child0.set_border(Edge.Top, 7)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 7)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 18)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 18)

    def test_box_sizing_border_box_no_height_no_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 2)
        root_child0.set_padding(Edge.Right, 2)
        root_child0.set_padding(Edge.Bottom, 2)
        root_child0.set_border(Edge.Left, 7)
        root_child0.set_border(Edge.Top, 7)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 7)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 18)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 18)

    def test_box_sizing_content_box_nested(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 15)
        root.set_padding(Edge.Top, 15)
        root.set_padding(Edge.Right, 15)
        root.set_padding(Edge.Bottom, 15)
        root.set_border(Edge.Left, 3)
        root.set_border(Edge.Top, 3)
        root.set_border(Edge.Right, 3)
        root.set_border(Edge.Bottom, 3)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 2)
        root_child0.set_padding(Edge.Right, 2)
        root_child0.set_padding(Edge.Bottom, 2)
        root_child0.set_border(Edge.Left, 7)
        root_child0.set_border(Edge.Top, 7)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 7)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 1)
        root_child0_child0.set_padding(Edge.Right, 1)
        root_child0_child0.set_padding(Edge.Bottom, 1)
        root_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0.set_border(Edge.Top, 2)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 2)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(5)
        root_child0_child0.box_sizing = BoxSizing.ContentBox
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 136)
        assert_float_approx(root.layout_height, 136)

        assert_float_approx(root_child0.layout_left, 18)
        assert_float_approx(root_child0.layout_top, 18)
        assert_float_approx(root_child0.layout_width, 38)
        assert_float_approx(root_child0.layout_height, 38)

        assert_float_approx(root_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0.layout_width, 16)
        assert_float_approx(root_child0_child0.layout_height, 11)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 136)
        assert_float_approx(root.layout_height, 136)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 18)
        assert_float_approx(root_child0.layout_width, 38)
        assert_float_approx(root_child0.layout_height, 38)

        assert_float_approx(root_child0_child0.layout_left, 13)
        assert_float_approx(root_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0.layout_width, 16)
        assert_float_approx(root_child0_child0.layout_height, 11)

    def test_box_sizing_border_box_nested(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 15)
        root.set_padding(Edge.Top, 15)
        root.set_padding(Edge.Right, 15)
        root.set_padding(Edge.Bottom, 15)
        root.set_border(Edge.Left, 3)
        root.set_border(Edge.Top, 3)
        root.set_border(Edge.Right, 3)
        root.set_border(Edge.Bottom, 3)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 2)
        root_child0.set_padding(Edge.Right, 2)
        root_child0.set_padding(Edge.Bottom, 2)
        root_child0.set_border(Edge.Left, 7)
        root_child0.set_border(Edge.Top, 7)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 7)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 1)
        root_child0_child0.set_padding(Edge.Right, 1)
        root_child0_child0.set_padding(Edge.Bottom, 1)
        root_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0.set_border(Edge.Top, 2)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 2)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(5)
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 18)
        assert_float_approx(root_child0.layout_top, 18)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 6)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 62)
        assert_float_approx(root_child0.layout_top, 18)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child0_child0.layout_left, 1)
        assert_float_approx(root_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 6)

    def test_box_sizing_content_box_nested_alternating(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 3)
        root.set_padding(Edge.Top, 3)
        root.set_padding(Edge.Right, 3)
        root.set_padding(Edge.Bottom, 3)
        root.set_border(Edge.Left, 2)
        root.set_border(Edge.Top, 2)
        root.set_border(Edge.Right, 2)
        root.set_border(Edge.Bottom, 2)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 8)
        root_child0.set_padding(Edge.Top, 8)
        root_child0.set_padding(Edge.Right, 8)
        root_child0.set_padding(Edge.Bottom, 8)
        root_child0.set_border(Edge.Left, 2)
        root_child0.set_border(Edge.Top, 2)
        root_child0.set_border(Edge.Right, 2)
        root_child0.set_border(Edge.Bottom, 2)
        root_child0.width = YGValuePoint(40)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_padding(Edge.Left, 3)
        root_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0.set_padding(Edge.Right, 3)
        root_child0_child0.set_padding(Edge.Bottom, 3)
        root_child0_child0.set_border(Edge.Left, 6)
        root_child0_child0.set_border(Edge.Top, 6)
        root_child0_child0.set_border(Edge.Right, 6)
        root_child0_child0.set_border(Edge.Bottom, 6)
        root_child0_child0.width = YGValuePoint(20)
        root_child0_child0.height = YGValuePoint(25)
        root_child0_child0.box_sizing = BoxSizing.ContentBox
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0_child0.set_padding(Edge.Top, 1)
        root_child0_child0_child0.set_padding(Edge.Right, 1)
        root_child0_child0_child0.set_padding(Edge.Bottom, 1)
        root_child0_child0_child0.set_border(Edge.Left, 1)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 1)
        root_child0_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0_child0.width = YGValuePoint(10)
        root_child0_child0_child0.height = YGValuePoint(5)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 110)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0.layout_width, 38)
        assert_float_approx(root_child0_child0.layout_height, 43)

        assert_float_approx(root_child0_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0_child0.layout_height, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 110)

        assert_float_approx(root_child0.layout_left, 65)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child0_child0.layout_left, -8)
        assert_float_approx(root_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0.layout_width, 38)
        assert_float_approx(root_child0_child0.layout_height, 43)

        assert_float_approx(root_child0_child0_child0.layout_left, 19)
        assert_float_approx(root_child0_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0_child0.layout_height, 5)

    def test_box_sizing_border_box_nested_alternating(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 3)
        root.set_padding(Edge.Top, 3)
        root.set_padding(Edge.Right, 3)
        root.set_padding(Edge.Bottom, 3)
        root.set_border(Edge.Left, 2)
        root.set_border(Edge.Top, 2)
        root.set_border(Edge.Right, 2)
        root.set_border(Edge.Bottom, 2)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 8)
        root_child0.set_padding(Edge.Top, 8)
        root_child0.set_padding(Edge.Right, 8)
        root_child0.set_padding(Edge.Bottom, 8)
        root_child0.set_border(Edge.Left, 2)
        root_child0.set_border(Edge.Top, 2)
        root_child0.set_border(Edge.Right, 2)
        root_child0.set_border(Edge.Bottom, 2)
        root_child0.width = YGValuePoint(40)
        root_child0.height = YGValuePoint(40)
        root_child0.box_sizing = BoxSizing.ContentBox
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_padding(Edge.Left, 3)
        root_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0.set_padding(Edge.Right, 3)
        root_child0_child0.set_padding(Edge.Bottom, 3)
        root_child0_child0.set_border(Edge.Left, 6)
        root_child0_child0.set_border(Edge.Top, 6)
        root_child0_child0.set_border(Edge.Right, 6)
        root_child0_child0.set_border(Edge.Bottom, 6)
        root_child0_child0.width = YGValuePoint(20)
        root_child0_child0.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0_child0.set_padding(Edge.Top, 1)
        root_child0_child0_child0.set_padding(Edge.Right, 1)
        root_child0_child0_child0.set_padding(Edge.Bottom, 1)
        root_child0_child0_child0.set_border(Edge.Left, 1)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 1)
        root_child0_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0_child0.width = YGValuePoint(10)
        root_child0_child0_child0.height = YGValuePoint(5)
        root_child0_child0_child0.box_sizing = BoxSizing.ContentBox
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 25)

        assert_float_approx(root_child0_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0_child0.layout_width, 14)
        assert_float_approx(root_child0_child0_child0.layout_height, 9)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 35)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child0_child0.layout_left, 30)
        assert_float_approx(root_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 25)

        assert_float_approx(root_child0_child0_child0.layout_left, -3)
        assert_float_approx(root_child0_child0_child0.layout_top, 9)
        assert_float_approx(root_child0_child0_child0.layout_width, 14)
        assert_float_approx(root_child0_child0_child0.layout_height, 9)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++")
    def test_box_sizing_content_box_flex_basis_row(self):
        pass

    def test_box_sizing_border_box_flex_basis_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 10)
        root_child0.set_border(Edge.Top, 10)
        root_child0.set_border(Edge.Right, 10)
        root_child0.set_border(Edge.Bottom, 10)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 30)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++")
    def test_box_sizing_content_box_flex_basis_column(self):
        pass

    def test_box_sizing_border_box_flex_basis_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.set_padding(Edge.Left, 5)
        root_child0.set_padding(Edge.Top, 5)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 5)
        root_child0.set_border(Edge.Left, 10)
        root_child0.set_border(Edge.Top, 10)
        root_child0.set_border(Edge.Right, 10)
        root_child0.set_border(Edge.Bottom, 10)
        root_child0.height = YGValuePoint(25)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 50)

    def test_box_sizing_content_box_padding_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Start, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_padding_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Start, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_content_box_padding_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.End, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_padding_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.End, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_content_box_border_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Start, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_border_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Start, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_content_box_border_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.End, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.box_sizing = BoxSizing.ContentBox
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 105)
        assert_float_approx(root.layout_height, 100)

    def test_box_sizing_border_box_border_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.End, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)
