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
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestStaticPosition:
    def test_static_position_insets_have_no_effect_left_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root_child0.set_position(Edge.Left, 50)
        root_child0.set_position(Edge.Top, 50)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

    def test_static_position_insets_have_no_effect_right_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root_child0.set_position(Edge.Right, 50)
        root_child0.set_position(Edge.Bottom, 50)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

    def test_static_position_absolute_child_insets_relative_to_positioned_ancestor(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 100)
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 50)
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_row_reverse(
        self,
    ):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 50)
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_column_reverse_static_position_absolute_child_insets_relative_to_positioned_ancestor_row_reverse(
        self,
    ):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 50)
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_row(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.set_position(Edge.Right, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_column_reverse_static_position_absolute_child_insets_relative_to_positioned_ancestor_row(
        self,
    ):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.set_position(Edge.Right, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_column_reverse(
        self,
    ):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.set_position(Edge.Right, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_column_reverse_static_position_absolute_child_insets_relative_to_positioned_ancestor_column_reverse(
        self,
    ):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0.set_position(Edge.Right, 50)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_deep(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 100)
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_margin(Edge.Left, 100)
        root_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0.height = YGValuePoint(100)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0_child0.set_margin(Edge.Left, 100)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(100)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0_child0_child0.set_margin(Edge.Left, 100)
        root_child0_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0_child0.height = YGValuePoint(100)
        root_child0_child0_child0_child0.insert_child(root_child0_child0_child0_child0_child0, 0)

        root_child0_child0_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0_child0_child0_child0.set_position(Edge.Left, 50)
        root_child0_child0_child0_child0_child0_child0.set_position(Edge.Top, 50)
        root_child0_child0_child0_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0_child0_child0.insert_child(
            root_child0_child0_child0_child0_child0_child0, 0
        )
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_left, -350)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_width_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePercent(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_width_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePercent(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_width_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.width = YGValuePercent(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_height_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePercent(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

    def test_static_position_relative_child_height_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePercent(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_height_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePercent(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_left_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_left_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_position(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_left_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_position(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_right_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_right_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_position(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_right_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_position(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_top_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 2)
        root_child0_child0_child0.set_position(Edge.Right, 12)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 1)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -2)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_no_position_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 18)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -15)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_zero_for_inset_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, YGValuePercent(0))
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -1)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -265)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_justify_flex_start_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.justify_content = Justify.FlexStart
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 2)
        root_child0_child0_child0.set_position(Edge.Right, 12)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 1)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -2)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_align_flex_start_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.align_items = Align.FlexStart
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 2)
        root_child0_child0_child0.set_position(Edge.Right, 12)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 1)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -2)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_static_root(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Static
        root.set_padding(Edge.Left, 6)
        root.set_padding(Edge.Top, 1)
        root.set_padding(Edge.Right, 11)
        root.set_padding(Edge.Bottom, 4)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_margin(Edge.Left, 12)
        root_child0.set_margin(Edge.Top, 11)
        root_child0.set_margin(Edge.Right, 15)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 3)
        root_child0.set_padding(Edge.Top, 7)
        root_child0.set_padding(Edge.Right, 5)
        root_child0.set_padding(Edge.Bottom, 4)
        root_child0.set_border(Edge.Left, 4)
        root_child0.set_border(Edge.Top, 3)
        root_child0.set_border(Edge.Right, 2)
        root_child0.set_border(Edge.Bottom, 1)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePercent(50)
        root.insert_child(root_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 18)
        assert_float_approx(root_child0.layout_top, 12)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 24)
        assert_float_approx(root_child0.layout_top, 12)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

    def test_static_position_absolute_child_multiple(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePercent(10)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.position_type = PositionType.Static
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child1_child0 = Node(config)
        root_child0_child1_child0.position_type = PositionType.Absolute
        root_child0_child1_child0.width = YGValuePercent(50)
        root_child0_child1_child0.height = YGValuePoint(50)
        root_child0_child1.insert_child(root_child0_child1_child0, 0)

        root_child0_child1_child1 = Node(config)
        root_child0_child1_child1.position_type = PositionType.Absolute
        root_child0_child1_child1.width = YGValuePercent(50)
        root_child0_child1_child1.height = YGValuePoint(50)
        root_child0_child1.insert_child(root_child0_child1_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.position_type = PositionType.Absolute
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 100)
        assert_float_approx(root_child0_child1.layout_top, 200)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child1_child0.layout_left, 0)
        assert_float_approx(root_child0_child1_child0.layout_top, 0)
        assert_float_approx(root_child0_child1_child0.layout_width, 200)
        assert_float_approx(root_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child1_child1.layout_left, 0)
        assert_float_approx(root_child0_child1_child1.layout_top, 0)
        assert_float_approx(root_child0_child1_child1.layout_width, 200)
        assert_float_approx(root_child0_child1_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 100)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 200)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 60)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 200)
        assert_float_approx(root_child0_child1.layout_top, 200)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child1_child0.layout_left, -100)
        assert_float_approx(root_child0_child1_child0.layout_top, 0)
        assert_float_approx(root_child0_child1_child0.layout_width, 200)
        assert_float_approx(root_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child1_child1.layout_left, -100)
        assert_float_approx(root_child0_child1_child1.layout_top, 0)
        assert_float_approx(root_child0_child1_child1.layout_width, 200)
        assert_float_approx(root_child0_child1_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 275)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    def test_static_position_absolute_child_padding_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_padding(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 200)

    def test_static_position_relative_child_padding_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_padding(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

    def test_static_position_static_child_padding_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_padding(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.set_padding(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

    def test_static_position_absolute_child_border_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_border_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_border_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_containing_block_padding_box(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePercent(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 200)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_containing_block_padding_box(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePercent(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 200)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_containing_block_padding_box(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.width = YGValuePercent(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 200)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_containing_block_content_box(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePercent(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 50)

    def test_static_position_relative_child_containing_block_content_box(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 200)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 50)

    def test_static_position_static_child_containing_block_content_box(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 100)
        root_child0.set_padding(Edge.Top, 100)
        root_child0.set_padding(Edge.Right, 100)
        root_child0.set_padding(Edge.Bottom, 100)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePercent(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 200)
        assert_float_approx(root_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 50)

    def test_static_position_containing_block_padding_and_border(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 9)
        root_child0.set_padding(Edge.Top, 8)
        root_child0.set_padding(Edge.Right, 1)
        root_child0.set_padding(Edge.Bottom, 4)
        root_child0.set_border(Edge.Left, 2)
        root_child0.set_border(Edge.Top, 5)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 4)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(400)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(61)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 11)
        assert_float_approx(root_child0_child0.layout_top, 13)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0_child0.layout_height, 239)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 400)

        assert_float_approx(root_child0_child0.layout_left, 292)
        assert_float_approx(root_child0_child0.layout_top, 13)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -60)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0_child0.layout_height, 239)

    def test_static_position_relative_child_top_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_position(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_top_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_position(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_bottom_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_bottom_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_position(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_bottom_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_position(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_absolute_child_margin_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, -50)
        assert_float_approx(root_child0_child0_child0.layout_top, 100)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_relative_child_margin_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_margin(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_static_child_margin_percentage(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Static
        root_child0_child0_child0.set_margin(Edge.Left, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Top, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Right, YGValuePercent(50))
        root_child0_child0_child0.set_margin(Edge.Bottom, YGValuePercent(50))
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_static_position_start_inset_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Start, 12)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 11)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -2)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_end_inset_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.End, 4)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 270)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -261)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

    def test_static_position_row_reverse_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.RowReverse
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.height = YGValuePercent(12)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, -128)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 133)
        assert_float_approx(root_child0_child0_child0.layout_height, 23)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, 18)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 133)
        assert_float_approx(root_child0_child0_child0.layout_height, 23)

    def test_static_position_column_reverse_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.ColumnReverse
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(21)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, 18)
        assert_float_approx(root_child0_child0_child0.layout_top, -82)
        assert_float_approx(root_child0_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, -15)
        assert_float_approx(root_child0_child0_child0.layout_top, -82)
        assert_float_approx(root_child0_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

    def test_static_position_align_center_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.align_items = Align.Center
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(21)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.set_margin(Edge.Left, 9)
        root_child0_child0_child1.set_margin(Edge.Top, 12)
        root_child0_child0_child1.set_margin(Edge.Right, 4)
        root_child0_child0_child1.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1.set_padding(Edge.Left, 5)
        root_child0_child0_child1.set_padding(Edge.Top, 3)
        root_child0_child0_child1.set_padding(Edge.Right, 8)
        root_child0_child0_child1.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1.set_border(Edge.Left, 2)
        root_child0_child0_child1.set_border(Edge.Top, 1)
        root_child0_child0_child1.set_border(Edge.Right, 5)
        root_child0_child0_child1.set_border(Edge.Bottom, 9)
        root_child0_child0_child1.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child1_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child1_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child1_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child1_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child1_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child1_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1_child0.set_border(Edge.Left, 2)
        root_child0_child0_child1_child0.set_border(Edge.Top, 1)
        root_child0_child0_child1_child0.set_border(Edge.Right, 5)
        root_child0_child0_child1_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child1_child0.width = YGValuePoint(100)
        root_child0_child0_child1_child0.height = YGValuePoint(50)
        root_child0_child0_child1.insert_child(root_child0_child0_child1_child0, 0)

        root_child0_child0_child2 = Node(config)
        root_child0_child0_child2.set_margin(Edge.Left, 9)
        root_child0_child0_child2.set_margin(Edge.Top, 12)
        root_child0_child0_child2.set_margin(Edge.Right, 4)
        root_child0_child0_child2.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2.set_padding(Edge.Left, 5)
        root_child0_child0_child2.set_padding(Edge.Top, 3)
        root_child0_child0_child2.set_padding(Edge.Right, 8)
        root_child0_child0_child2.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2.set_border(Edge.Left, 2)
        root_child0_child0_child2.set_border(Edge.Top, 1)
        root_child0_child0_child2.set_border(Edge.Right, 5)
        root_child0_child0_child2.set_border(Edge.Bottom, 9)
        root_child0_child0_child2.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child2, 2)

        root_child0_child0_child2_child0 = Node(config)
        root_child0_child0_child2_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child2_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child2_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child2_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child2_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child2_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child2_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2_child0.set_border(Edge.Left, 2)
        root_child0_child0_child2_child0.set_border(Edge.Top, 1)
        root_child0_child0_child2_child0.set_border(Edge.Right, 5)
        root_child0_child0_child2_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child2_child0.width = YGValuePoint(100)
        root_child0_child0_child2_child0.height = YGValuePoint(50)
        root_child0_child0_child2.insert_child(root_child0_child0_child2_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 65)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 39)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 75)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 75)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 65)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 39)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, -77)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 75)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 75)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

    def test_static_position_align_flex_end_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.align_items = Align.FlexEnd
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(21)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.set_margin(Edge.Left, 9)
        root_child0_child0_child1.set_margin(Edge.Top, 12)
        root_child0_child0_child1.set_margin(Edge.Right, 4)
        root_child0_child0_child1.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1.set_padding(Edge.Left, 5)
        root_child0_child0_child1.set_padding(Edge.Top, 3)
        root_child0_child0_child1.set_padding(Edge.Right, 8)
        root_child0_child0_child1.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1.set_border(Edge.Left, 2)
        root_child0_child0_child1.set_border(Edge.Top, 1)
        root_child0_child0_child1.set_border(Edge.Right, 5)
        root_child0_child0_child1.set_border(Edge.Bottom, 9)
        root_child0_child0_child1.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child1_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child1_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child1_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child1_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child1_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child1_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1_child0.set_border(Edge.Left, 2)
        root_child0_child0_child1_child0.set_border(Edge.Top, 1)
        root_child0_child0_child1_child0.set_border(Edge.Right, 5)
        root_child0_child0_child1_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child1_child0.width = YGValuePoint(100)
        root_child0_child0_child1_child0.height = YGValuePoint(50)
        root_child0_child0_child1.insert_child(root_child0_child0_child1_child0, 0)

        root_child0_child0_child2 = Node(config)
        root_child0_child0_child2.set_margin(Edge.Left, 9)
        root_child0_child0_child2.set_margin(Edge.Top, 12)
        root_child0_child0_child2.set_margin(Edge.Right, 4)
        root_child0_child0_child2.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2.set_padding(Edge.Left, 5)
        root_child0_child0_child2.set_padding(Edge.Top, 3)
        root_child0_child0_child2.set_padding(Edge.Right, 8)
        root_child0_child0_child2.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2.set_border(Edge.Left, 2)
        root_child0_child0_child2.set_border(Edge.Top, 1)
        root_child0_child0_child2.set_border(Edge.Right, 5)
        root_child0_child0_child2.set_border(Edge.Bottom, 9)
        root_child0_child0_child2.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child2, 2)

        root_child0_child0_child2_child0 = Node(config)
        root_child0_child0_child2_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child2_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child2_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child2_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child2_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child2_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child2_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2_child0.set_border(Edge.Left, 2)
        root_child0_child0_child2_child0.set_border(Edge.Top, 1)
        root_child0_child0_child2_child0.set_border(Edge.Right, 5)
        root_child0_child0_child2_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child2_child0.width = YGValuePoint(100)
        root_child0_child0_child2_child0.height = YGValuePoint(50)
        root_child0_child0_child2.insert_child(root_child0_child0_child2_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 111)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 131)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 131)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 18)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, -77)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 18)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 18)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

    def test_static_position_justify_center_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.justify_content = Justify.Center
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(21)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.set_margin(Edge.Left, 9)
        root_child0_child0_child1.set_margin(Edge.Top, 12)
        root_child0_child0_child1.set_margin(Edge.Right, 4)
        root_child0_child0_child1.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1.set_padding(Edge.Left, 5)
        root_child0_child0_child1.set_padding(Edge.Top, 3)
        root_child0_child0_child1.set_padding(Edge.Right, 8)
        root_child0_child0_child1.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1.set_border(Edge.Left, 2)
        root_child0_child0_child1.set_border(Edge.Top, 1)
        root_child0_child0_child1.set_border(Edge.Right, 5)
        root_child0_child0_child1.set_border(Edge.Bottom, 9)
        root_child0_child0_child1.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child1_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child1_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child1_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child1_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child1_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child1_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1_child0.set_border(Edge.Left, 2)
        root_child0_child0_child1_child0.set_border(Edge.Top, 1)
        root_child0_child0_child1_child0.set_border(Edge.Right, 5)
        root_child0_child0_child1_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child1_child0.width = YGValuePoint(100)
        root_child0_child0_child1_child0.height = YGValuePoint(50)
        root_child0_child0_child1.insert_child(root_child0_child0_child1_child0, 0)

        root_child0_child0_child2 = Node(config)
        root_child0_child0_child2.set_margin(Edge.Left, 9)
        root_child0_child0_child2.set_margin(Edge.Top, 12)
        root_child0_child0_child2.set_margin(Edge.Right, 4)
        root_child0_child0_child2.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2.set_padding(Edge.Left, 5)
        root_child0_child0_child2.set_padding(Edge.Top, 3)
        root_child0_child0_child2.set_padding(Edge.Right, 8)
        root_child0_child0_child2.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2.set_border(Edge.Left, 2)
        root_child0_child0_child2.set_border(Edge.Top, 1)
        root_child0_child0_child2.set_border(Edge.Right, 5)
        root_child0_child0_child2.set_border(Edge.Bottom, 9)
        root_child0_child0_child2.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child2, 2)

        root_child0_child0_child2_child0 = Node(config)
        root_child0_child0_child2_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child2_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child2_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child2_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child2_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child2_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child2_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2_child0.set_border(Edge.Left, 2)
        root_child0_child0_child2_child0.set_border(Edge.Top, 1)
        root_child0_child0_child2_child0.set_border(Edge.Right, 5)
        root_child0_child0_child2_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child2_child0.width = YGValuePoint(100)
        root_child0_child0_child2_child0.height = YGValuePoint(50)
        root_child0_child0_child2.insert_child(root_child0_child0_child2_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 18)
        assert_float_approx(root_child0_child0_child0.layout_top, 85)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 18)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 18)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 111)
        assert_float_approx(root_child0_child0_child0.layout_top, 85)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, -77)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 131)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 131)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

    def test_static_position_justify_flex_end_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.justify_content = Justify.FlexEnd
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(21)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.set_margin(Edge.Left, 9)
        root_child0_child0_child1.set_margin(Edge.Top, 12)
        root_child0_child0_child1.set_margin(Edge.Right, 4)
        root_child0_child0_child1.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1.set_padding(Edge.Left, 5)
        root_child0_child0_child1.set_padding(Edge.Top, 3)
        root_child0_child0_child1.set_padding(Edge.Right, 8)
        root_child0_child0_child1.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1.set_border(Edge.Left, 2)
        root_child0_child0_child1.set_border(Edge.Top, 1)
        root_child0_child0_child1.set_border(Edge.Right, 5)
        root_child0_child0_child1.set_border(Edge.Bottom, 9)
        root_child0_child0_child1.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child1_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child1_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child1_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child1_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child1_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child1_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1_child0.set_border(Edge.Left, 2)
        root_child0_child0_child1_child0.set_border(Edge.Top, 1)
        root_child0_child0_child1_child0.set_border(Edge.Right, 5)
        root_child0_child0_child1_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child1_child0.width = YGValuePoint(100)
        root_child0_child0_child1_child0.height = YGValuePoint(50)
        root_child0_child0_child1.insert_child(root_child0_child0_child1_child0, 0)

        root_child0_child0_child2 = Node(config)
        root_child0_child0_child2.set_margin(Edge.Left, 9)
        root_child0_child0_child2.set_margin(Edge.Top, 12)
        root_child0_child0_child2.set_margin(Edge.Right, 4)
        root_child0_child0_child2.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2.set_padding(Edge.Left, 5)
        root_child0_child0_child2.set_padding(Edge.Top, 3)
        root_child0_child0_child2.set_padding(Edge.Right, 8)
        root_child0_child0_child2.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2.set_border(Edge.Left, 2)
        root_child0_child0_child2.set_border(Edge.Top, 1)
        root_child0_child0_child2.set_border(Edge.Right, 5)
        root_child0_child0_child2.set_border(Edge.Bottom, 9)
        root_child0_child0_child2.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child2, 2)

        root_child0_child0_child2_child0 = Node(config)
        root_child0_child0_child2_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child2_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child2_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child2_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child2_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child2_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child2_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2_child0.set_border(Edge.Left, 2)
        root_child0_child0_child2_child0.set_border(Edge.Top, 1)
        root_child0_child0_child2_child0.set_border(Edge.Right, 5)
        root_child0_child0_child2_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child2_child0.width = YGValuePoint(100)
        root_child0_child0_child2_child0.height = YGValuePoint(50)
        root_child0_child0_child2.insert_child(root_child0_child0_child2_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 18)
        assert_float_approx(root_child0_child0_child0.layout_top, 140)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 18)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 18)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 111)
        assert_float_approx(root_child0_child0_child0.layout_top, 140)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, -77)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 131)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 131)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

    def test_static_position_justify_flex_start_position_set_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Right, 30)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(21)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.set_margin(Edge.Left, 9)
        root_child0_child0_child1.set_margin(Edge.Top, 12)
        root_child0_child0_child1.set_margin(Edge.Right, 4)
        root_child0_child0_child1.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1.set_padding(Edge.Left, 5)
        root_child0_child0_child1.set_padding(Edge.Top, 3)
        root_child0_child0_child1.set_padding(Edge.Right, 8)
        root_child0_child0_child1.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1.set_border(Edge.Left, 2)
        root_child0_child0_child1.set_border(Edge.Top, 1)
        root_child0_child0_child1.set_border(Edge.Right, 5)
        root_child0_child0_child1.set_border(Edge.Bottom, 9)
        root_child0_child0_child1.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child1_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child1_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child1_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child1_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child1_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child1_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child1_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child1_child0.set_border(Edge.Left, 2)
        root_child0_child0_child1_child0.set_border(Edge.Top, 1)
        root_child0_child0_child1_child0.set_border(Edge.Right, 5)
        root_child0_child0_child1_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child1_child0.width = YGValuePoint(100)
        root_child0_child0_child1_child0.height = YGValuePoint(50)
        root_child0_child0_child1.insert_child(root_child0_child0_child1_child0, 0)

        root_child0_child0_child2 = Node(config)
        root_child0_child0_child2.set_margin(Edge.Left, 9)
        root_child0_child0_child2.set_margin(Edge.Top, 12)
        root_child0_child0_child2.set_margin(Edge.Right, 4)
        root_child0_child0_child2.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2.set_padding(Edge.Left, 5)
        root_child0_child0_child2.set_padding(Edge.Top, 3)
        root_child0_child0_child2.set_padding(Edge.Right, 8)
        root_child0_child0_child2.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2.set_border(Edge.Left, 2)
        root_child0_child0_child2.set_border(Edge.Top, 1)
        root_child0_child0_child2.set_border(Edge.Right, 5)
        root_child0_child0_child2.set_border(Edge.Bottom, 9)
        root_child0_child0_child2.width = YGValuePercent(10)
        root_child0_child0.insert_child(root_child0_child0_child2, 2)

        root_child0_child0_child2_child0 = Node(config)
        root_child0_child0_child2_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child2_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child2_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child2_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child2_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child2_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child2_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child2_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child2_child0.set_border(Edge.Left, 2)
        root_child0_child0_child2_child0.set_border(Edge.Top, 1)
        root_child0_child0_child2_child0.set_border(Edge.Right, 5)
        root_child0_child0_child2_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child2_child0.width = YGValuePoint(100)
        root_child0_child0_child2_child0.height = YGValuePoint(50)
        root_child0_child0_child2.insert_child(root_child0_child0_child2_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 106)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 18)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 18)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 215)
        assert_float_approx(root.layout_height, 301)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 202)
        assert_float_approx(root_child0.layout_height, 295)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 166)
        assert_float_approx(root_child0_child0.layout_height, 244)

        assert_float_approx(root_child0_child0_child0.layout_left, 106)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, -77)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 131)
        assert_float_approx(root_child0_child0_child1.layout_top, 29)
        assert_float_approx(root_child0_child0_child1.layout_width, 20)
        assert_float_approx(root_child0_child0_child1.layout_height, 92)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child2.layout_left, 131)
        assert_float_approx(root_child0_child0_child2.layout_top, 140)
        assert_float_approx(root_child0_child0_child2.layout_width, 20)
        assert_float_approx(root_child0_child0_child2.layout_height, 92)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 50)

    def test_static_position_no_definite_size_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, YGValuePercent(23))
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 133)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 133)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

    def test_static_position_both_insets_set_amalgamation(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, YGValuePercent(23))
        root_child0_child0_child0.set_position(Edge.Right, 13)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, 9)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 69)
        assert_float_approx(root.layout_height, 79)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 56)
        assert_float_approx(root_child0.layout_height, 73)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0.layout_height, 22)

        assert_float_approx(root_child0_child0_child0.layout_left, -3)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0_child0.layout_height, 92)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, -97)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 16)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 50)
