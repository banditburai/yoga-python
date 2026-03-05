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


class TestAlignItems:
    def test_align_items_stretch(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
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

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

    def test_align_baseline_multiline_row_and_column(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child2_child0 = Node(config)
        root_child2_child0.width = YGValuePoint(50)
        root_child2_child0.height = YGValuePoint(10)
        root_child2.insert_child(root_child2_child0, 0)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child2_child0.layout_left, 0)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 50)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child2_child0.layout_left, 0)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 50)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

    def test_align_flex_start_with_shrinking_children(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
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
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 500)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

    def test_align_flex_start_with_shrinking_children_with_stretch(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
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
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 500)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

    def test_align_flex_end_with_row_reverse(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(75)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 3)
        root_child0.set_margin(Edge.Right, 5)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 75)

        assert_float_approx(root_child0.layout_left, 3)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 58)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 75)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, -8)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_align_stretch_with_row_reverse(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(75)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 3)
        root_child0.set_margin(Edge.Right, 5)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 75)

        assert_float_approx(root_child0.layout_left, 3)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 58)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 75)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, -8)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_align_items_center(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
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

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_align_items_flex_start(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
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

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_align_items_flex_end(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
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

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_align_baseline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
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

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

    def test_align_baseline_child(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

    def test_align_baseline_child_multiline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Row
        root_child1.flex_wrap = Wrap.Wrap
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(25)
        root_child1_child0.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = Node(config)
        root_child1_child1.width = YGValuePoint(25)
        root_child1_child1.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child1, 1)

        root_child1_child2 = Node(config)
        root_child1_child2.width = YGValuePoint(25)
        root_child1_child2.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child2, 2)

        root_child1_child3 = Node(config)
        root_child1_child3.width = YGValuePoint(25)
        root_child1_child3.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child1_child1.layout_left, 25)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 10)

        assert_float_approx(root_child1_child2.layout_left, 0)
        assert_float_approx(root_child1_child2.layout_top, 20)
        assert_float_approx(root_child1_child2.layout_width, 25)
        assert_float_approx(root_child1_child2.layout_height, 20)

        assert_float_approx(root_child1_child3.layout_left, 25)
        assert_float_approx(root_child1_child3.layout_top, 20)
        assert_float_approx(root_child1_child3.layout_width, 25)
        assert_float_approx(root_child1_child3.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child1_child0.layout_left, 25)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 10)

        assert_float_approx(root_child1_child2.layout_left, 25)
        assert_float_approx(root_child1_child2.layout_top, 20)
        assert_float_approx(root_child1_child2.layout_width, 25)
        assert_float_approx(root_child1_child2.layout_height, 20)

        assert_float_approx(root_child1_child3.layout_left, 0)
        assert_float_approx(root_child1_child3.layout_top, 20)
        assert_float_approx(root_child1_child3.layout_width, 25)
        assert_float_approx(root_child1_child3.layout_height, 10)

    def test_align_baseline_child_multiline_override(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Row
        root_child1.flex_wrap = Wrap.Wrap
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(25)
        root_child1_child0.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = Node(config)
        root_child1_child1.align_self = Align.Baseline
        root_child1_child1.width = YGValuePoint(25)
        root_child1_child1.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child1, 1)

        root_child1_child2 = Node(config)
        root_child1_child2.width = YGValuePoint(25)
        root_child1_child2.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child2, 2)

        root_child1_child3 = Node(config)
        root_child1_child3.align_self = Align.Baseline
        root_child1_child3.width = YGValuePoint(25)
        root_child1_child3.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child1_child1.layout_left, 25)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 10)

        assert_float_approx(root_child1_child2.layout_left, 0)
        assert_float_approx(root_child1_child2.layout_top, 20)
        assert_float_approx(root_child1_child2.layout_width, 25)
        assert_float_approx(root_child1_child2.layout_height, 20)

        assert_float_approx(root_child1_child3.layout_left, 25)
        assert_float_approx(root_child1_child3.layout_top, 20)
        assert_float_approx(root_child1_child3.layout_width, 25)
        assert_float_approx(root_child1_child3.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child1_child0.layout_left, 25)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 10)

        assert_float_approx(root_child1_child2.layout_left, 25)
        assert_float_approx(root_child1_child2.layout_top, 20)
        assert_float_approx(root_child1_child2.layout_width, 25)
        assert_float_approx(root_child1_child2.layout_height, 20)

        assert_float_approx(root_child1_child3.layout_left, 0)
        assert_float_approx(root_child1_child3.layout_top, 20)
        assert_float_approx(root_child1_child3.layout_width, 25)
        assert_float_approx(root_child1_child3.layout_height, 10)

    def test_align_baseline_child_multiline_no_override_on_secondline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Row
        root_child1.flex_wrap = Wrap.Wrap
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(25)
        root_child1_child0.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = Node(config)
        root_child1_child1.width = YGValuePoint(25)
        root_child1_child1.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child1, 1)

        root_child1_child2 = Node(config)
        root_child1_child2.width = YGValuePoint(25)
        root_child1_child2.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child2, 2)

        root_child1_child3 = Node(config)
        root_child1_child3.align_self = Align.Baseline
        root_child1_child3.width = YGValuePoint(25)
        root_child1_child3.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child1_child1.layout_left, 25)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 10)

        assert_float_approx(root_child1_child2.layout_left, 0)
        assert_float_approx(root_child1_child2.layout_top, 20)
        assert_float_approx(root_child1_child2.layout_width, 25)
        assert_float_approx(root_child1_child2.layout_height, 20)

        assert_float_approx(root_child1_child3.layout_left, 25)
        assert_float_approx(root_child1_child3.layout_top, 20)
        assert_float_approx(root_child1_child3.layout_width, 25)
        assert_float_approx(root_child1_child3.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child1_child0.layout_left, 25)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 10)

        assert_float_approx(root_child1_child2.layout_left, 25)
        assert_float_approx(root_child1_child2.layout_top, 20)
        assert_float_approx(root_child1_child2.layout_width, 25)
        assert_float_approx(root_child1_child2.layout_height, 20)

        assert_float_approx(root_child1_child3.layout_left, 0)
        assert_float_approx(root_child1_child3.layout_top, 20)
        assert_float_approx(root_child1_child3.layout_width, 25)
        assert_float_approx(root_child1_child3.layout_height, 10)

    def test_align_baseline_child_top(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_position(Edge.Top, 10)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

    def test_align_baseline_child_top2(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_position(Edge.Top, 5)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 45)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 45)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

    def test_align_baseline_double_nested_child(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(15)
        root_child1.insert_child(root_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 5)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 15)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 5)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 15)

    def test_align_baseline_column(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
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
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

    def test_align_baseline_child_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 5)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 5)
        root_child0.set_margin(Edge.Bottom, 5)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.set_margin(Edge.Left, 1)
        root_child1_child0.set_margin(Edge.Top, 1)
        root_child1_child0.set_margin(Edge.Right, 1)
        root_child1_child0.set_margin(Edge.Bottom, 1)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 44)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 1)
        assert_float_approx(root_child1_child0.layout_top, 1)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, -10)
        assert_float_approx(root_child1.layout_top, 44)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, -1)
        assert_float_approx(root_child1_child0.layout_top, 1)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

    def test_align_baseline_child_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 5)
        root.set_padding(Edge.Top, 5)
        root.set_padding(Edge.Right, 5)
        root.set_padding(Edge.Bottom, 5)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_padding(Edge.Left, 5)
        root_child1.set_padding(Edge.Top, 5)
        root_child1.set_padding(Edge.Right, 5)
        root_child1.set_padding(Edge.Bottom, 5)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 55)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 5)
        assert_float_approx(root_child1_child0.layout_top, 5)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, -5)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, -5)
        assert_float_approx(root_child1_child0.layout_top, 5)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

    def test_align_baseline_multiline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(50)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root_child2_child0 = Node(config)
        root_child2_child0.width = YGValuePoint(50)
        root_child2_child0.height = YGValuePoint(10)
        root_child2.insert_child(root_child2_child0, 0)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child2_child0.layout_left, 0)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 50)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 60)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 50)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 20)

        assert_float_approx(root_child2_child0.layout_left, 0)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 50)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 60)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

    def test_align_items_center_child_with_margin_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.align_items = Align.Center
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_margin(Edge.Left, 10)
        root_child0_child0.set_margin(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(52)
        root_child0_child0.height = YGValuePoint(52)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 52)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 52)
        assert_float_approx(root_child0_child0.layout_height, 52)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 52)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 52)
        assert_float_approx(root_child0_child0.layout_height, 52)

    def test_align_items_flex_end_child_with_margin_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.align_items = Align.FlexEnd
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_margin(Edge.Left, 10)
        root_child0_child0.set_margin(Edge.Right, 10)
        root_child0_child0.width = YGValuePoint(52)
        root_child0_child0.height = YGValuePoint(52)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 52)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 52)
        assert_float_approx(root_child0_child0.layout_height, 52)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 52)

        assert_float_approx(root_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 52)
        assert_float_approx(root_child0_child0.layout_height, 52)

    def test_align_items_center_child_without_margin_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.align_items = Align.Center
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(72)
        root_child0_child0.height = YGValuePoint(72)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0.layout_height, 72)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0.layout_height, 72)

    def test_align_items_flex_end_child_without_margin_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.align_items = Align.FlexEnd
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(72)
        root_child0_child0.height = YGValuePoint(72)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0.layout_height, 72)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0.layout_height, 72)

    def test_align_center_should_size_based_on_content(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

    def test_align_stretch_should_size_based_on_parent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Top, 20)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.justify_content = Justify.Center
        root_child0.flex_shrink = 1
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(20)
        root_child0_child0_child0.height = YGValuePoint(20)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child0_child0.layout_left, 80)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 20)
        assert_float_approx(root_child0_child0_child0.layout_height, 20)

    def test_align_flex_start_with_stretching_children(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
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
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 500)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 500)
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 500)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 500)
        assert_float_approx(root_child0_child0_child0.layout_height, 0)

    def test_align_items_non_stretch_s526008(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
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

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_align_baseline_multiline_column(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(20)
        root_child1_child0.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root_child2.height = YGValuePoint(70)
        root.insert_child(root_child2, 2)

        root_child2_child0 = Node(config)
        root_child2_child0.width = YGValuePoint(10)
        root_child2_child0.height = YGValuePoint(10)
        root_child2.insert_child(root_child2_child0, 0)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

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
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 20)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 70)

        assert_float_approx(root_child2_child0.layout_left, 0)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 10)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 70)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child1_child0.layout_left, 10)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 20)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 70)

        assert_float_approx(root_child2_child0.layout_left, 30)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 10)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 70)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_align_baseline_multiline_column2(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Baseline
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePoint(20)
        root_child1_child0.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root_child2.height = YGValuePoint(70)
        root.insert_child(root_child2, 2)

        root_child2_child0 = Node(config)
        root_child2_child0.width = YGValuePoint(10)
        root_child2_child0.height = YGValuePoint(10)
        root_child2.insert_child(root_child2_child0, 0)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(20)
        root.insert_child(root_child3, 3)

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
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 20)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 70)

        assert_float_approx(root_child2_child0.layout_left, 0)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 10)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 70)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child1_child0.layout_left, 10)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 20)
        assert_float_approx(root_child1_child0.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 70)

        assert_float_approx(root_child2_child0.layout_left, 30)
        assert_float_approx(root_child2_child0.layout_top, 0)
        assert_float_approx(root_child2_child0.layout_width, 10)
        assert_float_approx(root_child2_child0.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 70)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)
