import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    PositionType,
    Wrap,
    Justify,
    Align,
    YGValuePoint,
    YGValuePercent,
    Gutter,
    Edge,
    Overflow,
    Display,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestFlexDirection:
    def test_flex_direction_column_no_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 10)

    def test_flex_direction_row_no_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 30)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 30)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_col_reverse_inner_padding_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_col_reverse_inner_padding_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_padding(Edge.Top, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_row_reverse_inner_border_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_border(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_border_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_border(Edge.Left, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_margin_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_margin(Edge.End, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_marign_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_margin(Edge.Start, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_padding_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_padding(Edge.Start, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_padding_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_padding(Edge.End, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_col_reverse_inner_border_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_col_reverse_inner_border_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_border(Edge.Bottom, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_row_reverse_inner_padding_left(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_padding(Edge.Left, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_padding_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_padding(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_border_left(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_border(Edge.Left, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_border_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_border(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_alternating_with_percent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.set_position(Edge.Left, YGValuePercent(10))
        root_child0.set_position(Edge.Top, YGValuePercent(10))
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePercent(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 120)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

    def test_flex_direction_col_reverse_inner_margin_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_margin(Edge.Top, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 90)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_col_reverse_inner_margin_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_margin(Edge.Bottom, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 80)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 80)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_col_reverse_inner_pos_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_position(Edge.Top, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_col_reverse_inner_pos_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_position(Edge.Bottom, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 80)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 80)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_row_reverse_inner_margin_left(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_margin(Edge.Left, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_margin_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_margin(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_pos_left(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_position(Edge.Left, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_pos_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_position(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_pos_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_position(Edge.Start, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_inner_pos_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_position(Edge.End, 10)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 80)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 10)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_border_left(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 110)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 120)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_border_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Start, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_border_right(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Right, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, -20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, -30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_border_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_border(Edge.End, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, -20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, -30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 110)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 120)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_column_reverse_border_top(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Top, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

    def test_flex_direction_column_reverse_border_bottom(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Bottom, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

    def test_flex_direction_row_reverse_pos_left(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.set_position(Edge.Left, 100)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 80)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 70)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 10)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_pos_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.set_position(Edge.Start, 100)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 80)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 70)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 10)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_pos_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.set_position(Edge.Right, 100)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 80)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 70)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 10)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_row_reverse_pos_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.set_position(Edge.End, 100)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 80)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 70)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child1.layout_left, 10)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 100)

    def test_flex_direction_column_reverse_pos_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.set_position(Edge.Top, 100)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_column_reverse_pos_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.set_position(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(10)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, -100)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, -100)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child1.layout_left, 90)
        assert_float_approx(root_child0_child1.layout_top, 100)
        assert_float_approx(root_child0_child1.layout_width, 10)
        assert_float_approx(root_child0_child1.layout_height, 0)

        assert_float_approx(root_child0_child2.layout_left, 90)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 10)
        assert_float_approx(root_child0_child2.layout_height, 0)

    def test_flex_direction_column_reverse_margin_top(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Top, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 100)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 100)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

    def test_flex_direction_column_reverse_margin_bottom(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Bottom, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

    def test_flex_direction_row_reverse_padding_left(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 110)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 120)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_padding_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Start, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_padding_right(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Right, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, -20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, -30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_padding_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.End, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, -20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, -30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 110)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 120)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_column_reverse_padding_top(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Top, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

    def test_flex_direction_column_reverse_padding_bottom(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Bottom, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 0)

    def test_flex_direction_row_reverse_margin_left(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Left, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_margin_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Start, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_margin_right(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Right, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_row_reverse_margin_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.End, 100)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 10)

    def test_flex_direction_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

    def test_flex_direction_column_reverse(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 90)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 80)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 70)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 90)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 80)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 70)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 10)

    def test_flex_direction_row_reverse(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 80)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 100)
