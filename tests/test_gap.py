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
    Gutter,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestGap:
    def test_column_gap_flexible(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(80)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.flex_shrink = 1
        root_child2.flex_basis = YGValuePercent(0)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_inflexible(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(80)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_mixed_flexible(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(80)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_child_margins(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(80)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.set_margin(Edge.Left, YGValuePoint(2))
        root_child0.set_margin(Edge.Right, YGValuePoint(2))
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.set_margin(Edge.Left, YGValuePoint(10))
        root_child1.set_margin(Edge.Right, YGValuePoint(10))
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.flex_shrink = 1
        root_child2.flex_basis = YGValuePercent(0)
        root_child2.set_margin(Edge.Left, YGValuePoint(15))
        root_child2.set_margin(Edge.Right, YGValuePoint(15))
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 2)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 26)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 2)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 63)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 2)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 76)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 52)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 2)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 15)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 2)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_row_gap_wrapping(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(80)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root_child4.height = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root_child5.height = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root_child6 = Node(config)
        root_child6.width = YGValuePoint(20)
        root_child6.height = YGValuePoint(20)
        root.insert_child(root_child6, 6)

        root_child7 = Node(config)
        root_child7.width = YGValuePoint(20)
        root_child7.height = YGValuePoint(20)
        root.insert_child(root_child7, 7)

        root_child8 = Node(config)
        root_child8.width = YGValuePoint(20)
        root_child8.height = YGValuePoint(20)
        root.insert_child(root_child8, 8)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 40)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 40)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 40)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        assert_float_approx(root_child6.layout_left, 0)
        assert_float_approx(root_child6.layout_top, 80)
        assert_float_approx(root_child6.layout_width, 20)
        assert_float_approx(root_child6.layout_height, 20)

        assert_float_approx(root_child7.layout_left, 30)
        assert_float_approx(root_child7.layout_top, 80)
        assert_float_approx(root_child7.layout_width, 20)
        assert_float_approx(root_child7.layout_height, 20)

        assert_float_approx(root_child8.layout_left, 60)
        assert_float_approx(root_child8.layout_top, 80)
        assert_float_approx(root_child8.layout_width, 20)
        assert_float_approx(root_child8.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 60)
        assert_float_approx(root_child3.layout_top, 40)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 40)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 0)
        assert_float_approx(root_child5.layout_top, 40)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        assert_float_approx(root_child6.layout_left, 60)
        assert_float_approx(root_child6.layout_top, 80)
        assert_float_approx(root_child6.layout_width, 20)
        assert_float_approx(root_child6.layout_height, 20)

        assert_float_approx(root_child7.layout_left, 30)
        assert_float_approx(root_child7.layout_top, 80)
        assert_float_approx(root_child7.layout_width, 20)
        assert_float_approx(root_child7.layout_height, 20)

        assert_float_approx(root_child8.layout_left, 0)
        assert_float_approx(root_child8.layout_top, 80)
        assert_float_approx(root_child8.layout_width, 20)
        assert_float_approx(root_child8.layout_height, 20)

    def test_column_gap_start_index(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(80)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 60)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

    def test_column_gap_justify_flex_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_justify_center(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 70)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_justify_flex_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_justify_space_between(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceBetween
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_justify_space_around(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceAround
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 3)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 77)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 77)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 3)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_justify_space_evenly(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 5)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_column_gap_wrap_align_flex_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root_child4.height = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root_child5.height = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 40)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 40)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 40)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 40)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 40)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 40)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

    def test_column_gap_wrap_align_center(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root_child4.height = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root_child5.height = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 20)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 60)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 60)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 60)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 20)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 60)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 60)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 60)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

    def test_column_gap_wrap_align_flex_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root_child4.height = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root_child5.height = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 40)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 40)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 80)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 40)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 40)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 80)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

    def test_column_gap_wrap_align_space_between(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceBetween
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root_child4.height = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root_child5.height = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 80)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 80)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

    def test_column_gap_wrap_align_space_around(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root_child4.height = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root_child5.height = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 10)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 70)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 70)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 70)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 10)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 70)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 70)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 20)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 70)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 20)

    def test_column_gap_wrap_align_stretch(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)
        root.set_gap(Gutter.Column, 5)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.min_width = YGValuePoint(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.min_width = YGValuePoint(60)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.min_width = YGValuePoint(60)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.flex_grow = 1
        root_child3.min_width = YGValuePoint(60)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.flex_grow = 1
        root_child4.min_width = YGValuePoint(60)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 71)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 76)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 72)
        assert_float_approx(root_child1.layout_height, 150)

        assert_float_approx(root_child2.layout_left, 153)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 71)
        assert_float_approx(root_child2.layout_height, 150)

        assert_float_approx(root_child3.layout_left, 229)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 71)
        assert_float_approx(root_child3.layout_height, 150)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 150)
        assert_float_approx(root_child4.layout_width, 300)
        assert_float_approx(root_child4.layout_height, 150)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 229)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 71)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 153)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 71)
        assert_float_approx(root_child1.layout_height, 150)

        assert_float_approx(root_child2.layout_left, 76)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 72)
        assert_float_approx(root_child2.layout_height, 150)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 71)
        assert_float_approx(root_child3.layout_height, 150)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 150)
        assert_float_approx(root_child4.layout_width, 300)
        assert_float_approx(root_child4.layout_height, 150)

    def test_column_gap_determines_parent_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(100)
        root.set_gap(Gutter.Column, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 100)

    def test_row_gap_align_items_stretch(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 90)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 90)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 110)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 90)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 110)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 90)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 110)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 90)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 90)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 90)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 110)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 90)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 110)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 90)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 110)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 90)

    def test_row_gap_align_items_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)
        root.set_gap(Gutter.Column, 10)
        root.set_gap(Gutter.Row, 20)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(20)
        root.insert_child(root_child4, 4)

        root_child5 = Node(config)
        root_child5.width = YGValuePoint(20)
        root.insert_child(root_child5, 5)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 20)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 0)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 20)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 0)

        assert_float_approx(root_child5.layout_left, 60)
        assert_float_approx(root_child5.layout_top, 20)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 80)
        assert_float_approx(root_child3.layout_top, 20)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 0)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 20)
        assert_float_approx(root_child4.layout_width, 20)
        assert_float_approx(root_child4.layout_height, 0)

        assert_float_approx(root_child5.layout_left, 20)
        assert_float_approx(root_child5.layout_top, 20)
        assert_float_approx(root_child5.layout_width, 20)
        assert_float_approx(root_child5.layout_height, 0)

    def test_row_gap_column_child_margins(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)
        root.set_gap(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.set_margin(Edge.Top, YGValuePoint(2))
        root_child0.set_margin(Edge.Bottom, YGValuePoint(2))
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.set_margin(Edge.Top, YGValuePoint(10))
        root_child1.set_margin(Edge.Bottom, YGValuePoint(10))
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.flex_shrink = 1
        root_child2.flex_basis = YGValuePercent(0)
        root_child2.set_margin(Edge.Top, YGValuePoint(15))
        root_child2.set_margin(Edge.Bottom, YGValuePoint(15))
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 2)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 42)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 66)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 42)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 143)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 42)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 2)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 42)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 66)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 42)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 143)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 42)

    def test_row_gap_row_wrap_child_margins(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)
        root.set_gap(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Top, YGValuePoint(2))
        root_child0.set_margin(Edge.Bottom, YGValuePoint(2))
        root_child0.width = YGValuePoint(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_margin(Edge.Top, YGValuePoint(10))
        root_child1.set_margin(Edge.Bottom, YGValuePoint(10))
        root_child1.width = YGValuePoint(60)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.set_margin(Edge.Top, YGValuePoint(15))
        root_child2.set_margin(Edge.Bottom, YGValuePoint(15))
        root_child2.width = YGValuePoint(60)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 2)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 24)
        assert_float_approx(root_child1.layout_width, 60)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 59)
        assert_float_approx(root_child2.layout_width, 60)
        assert_float_approx(root_child2.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 40)
        assert_float_approx(root_child0.layout_top, 2)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 24)
        assert_float_approx(root_child1.layout_width, 60)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 59)
        assert_float_approx(root_child2.layout_width, 60)
        assert_float_approx(root_child2.layout_height, 0)

    def test_row_gap_determines_parent_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.set_gap(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 20)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 20)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 30)

    @pytest.mark.skip(reason="Skipped in C++ - row_gap_percent_wrapping_with_min_width")
    def test_row_gap_percent_wrapping_with_min_width(self):
        pass

    def test_row_gap_percent_wrapping(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_padding(Edge.Left, YGValuePoint(10))
        root.set_padding(Edge.Top, YGValuePoint(10))
        root.set_padding(Edge.Right, YGValuePoint(10))
        root.set_padding(Edge.Bottom, YGValuePoint(10))
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(700)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(100)
        root_child4.height = YGValuePoint(100)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 138)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 138)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 10)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 190)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 62)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 190)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 62)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 190)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

    def test_row_gap_percent_determines_parent_height(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(100)
        root_child4.height = YGValuePoint(100)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 130)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 130)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 200)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 200)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 70)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 200)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 200)
        assert_float_approx(root_child4.layout_top, 200)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

    def test_row_gap_percent_wrapping_with_both_content_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_padding(Edge.Left, YGValuePoint(10))
        root.set_padding(Edge.Top, YGValuePoint(10))
        root.set_padding(Edge.Right, YGValuePoint(10))
        root.set_padding(Edge.Bottom, YGValuePoint(10))
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(700)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(100)
        root_child4.height = YGValuePoint(100)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 138)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 138)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 10)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 190)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 62)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 190)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 62)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 190)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

    def test_row_gap_percent_wrapping_with_content_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_margin(Edge.Left, YGValuePoint(10))
        root.set_margin(Edge.Top, YGValuePoint(10))
        root.set_margin(Edge.Right, YGValuePoint(10))
        root.set_margin(Edge.Bottom, YGValuePoint(10))
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(700)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(100)
        root_child4.height = YGValuePoint(100)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 10)
        assert_float_approx(root.layout_top, 10)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 130)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 170)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 130)
        assert_float_approx(root_child3.layout_top, 170)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 340)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 10)
        assert_float_approx(root.layout_top, 10)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 200)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 70)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 200)
        assert_float_approx(root_child2.layout_top, 170)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 170)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 200)
        assert_float_approx(root_child4.layout_top, 340)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

    def test_row_gap_percent_wrapping_with_content_margin_and_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_margin(Edge.Left, YGValuePoint(10))
        root.set_margin(Edge.Top, YGValuePoint(10))
        root.set_margin(Edge.Right, YGValuePoint(10))
        root.set_margin(Edge.Bottom, YGValuePoint(10))
        root.set_padding(Edge.Left, YGValuePoint(10))
        root.set_padding(Edge.Top, YGValuePoint(10))
        root.set_padding(Edge.Right, YGValuePoint(10))
        root.set_padding(Edge.Bottom, YGValuePoint(10))
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(700)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(100)
        root_child4.height = YGValuePoint(100)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 10)
        assert_float_approx(root.layout_top, 10)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 138)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 138)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 10)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 10)
        assert_float_approx(root.layout_top, 10)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 190)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 62)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 190)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 62)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 190)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

    def test_row_gap_percent_wrapping_with_flexible_content(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.flex_shrink = 1
        root_child2.flex_basis = YGValuePercent(0)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 300)

        assert_float_approx(root_child1.layout_left, 110)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 80)
        assert_float_approx(root_child1.layout_height, 300)

        assert_float_approx(root_child2.layout_left, 220)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 80)
        assert_float_approx(root_child2.layout_height, 300)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 220)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 300)

        assert_float_approx(root_child1.layout_left, 110)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 80)
        assert_float_approx(root_child1.layout_height, 300)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 80)
        assert_float_approx(root_child2.layout_height, 300)

    def test_row_gap_percent_wrapping_with_mixed_flexible_content(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePercent(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 300)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 300)

        assert_float_approx(root_child2.layout_left, 270)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 300)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 290)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 300)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 300)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 300)

    def test_row_gap_percent_wrapping_with_both_content_padding_and_item_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_padding(Edge.Left, YGValuePoint(10))
        root.set_padding(Edge.Top, YGValuePoint(10))
        root.set_padding(Edge.Right, YGValuePoint(10))
        root.set_padding(Edge.Bottom, YGValuePoint(10))
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(700)
        root.set_gap_percent(Gutter.Column, 10)
        root.set_gap_percent(Gutter.Row, 10)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, YGValuePoint(10))
        root_child0.set_padding(Edge.Top, YGValuePoint(10))
        root_child0.set_padding(Edge.Right, YGValuePoint(10))
        root_child0.set_padding(Edge.Bottom, YGValuePoint(10))
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_padding(Edge.Left, YGValuePoint(10))
        root_child1.set_padding(Edge.Top, YGValuePoint(10))
        root_child1.set_padding(Edge.Right, YGValuePoint(10))
        root_child1.set_padding(Edge.Bottom, YGValuePoint(10))
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.set_padding(Edge.Left, YGValuePoint(10))
        root_child2.set_padding(Edge.Top, YGValuePoint(10))
        root_child2.set_padding(Edge.Right, YGValuePoint(10))
        root_child2.set_padding(Edge.Bottom, YGValuePoint(10))
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.set_padding(Edge.Left, YGValuePoint(10))
        root_child3.set_padding(Edge.Top, YGValuePoint(10))
        root_child3.set_padding(Edge.Right, YGValuePoint(10))
        root_child3.set_padding(Edge.Bottom, YGValuePoint(10))
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.set_padding(Edge.Left, YGValuePoint(10))
        root_child4.set_padding(Edge.Top, YGValuePoint(10))
        root_child4.set_padding(Edge.Right, YGValuePoint(10))
        root_child4.set_padding(Edge.Bottom, YGValuePoint(10))
        root_child4.width = YGValuePoint(100)
        root_child4.height = YGValuePoint(100)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 138)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 138)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 10)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 190)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 62)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 190)
        assert_float_approx(root_child2.layout_top, 178)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 62)
        assert_float_approx(root_child3.layout_top, 178)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 190)
        assert_float_approx(root_child4.layout_top, 346)
        assert_float_approx(root_child4.layout_width, 100)
        assert_float_approx(root_child4.layout_height, 100)
