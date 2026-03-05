import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    PositionType,
    YGValuePoint,
    YGValuePercent,
    YGValueAuto,
    Edge,
    Wrap,
    Justify,
    Align,
    Overflow,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestAbsolutePosition:
    def test_absolute_layout_width_height_start_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Start, 10)
        root_child0.set_position(Edge.Top, 10)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_absolute_layout_width_height_left_auto_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position_auto(Edge.Left)
        root_child0.set_position(Edge.Right, 10)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_absolute_layout_width_height_left_right_auto(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 10)
        root_child0.set_position_auto(Edge.Right)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_absolute_layout_width_height_left_auto_right_auto(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position_auto(Edge.Left)
        root_child0.set_position_auto(Edge.Right)
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

    def test_absolute_layout_width_height_end_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.End, 10)
        root_child0.set_position(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_absolute_layout_start_top_end_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Start, 10)
        root_child0.set_position(Edge.Top, 10)
        root_child0.set_position(Edge.End, 10)
        root_child0.set_position(Edge.Bottom, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 80)

    def test_absolute_layout_width_height_start_top_end_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Start, 10)
        root_child0.set_position(Edge.Top, 10)
        root_child0.set_position(Edge.End, 10)
        root_child0.set_position(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_do_not_clamp_height_of_absolute_node_to_height_of_its_overflow_hidden_parent(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.overflow = Overflow.Hidden
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Start, 0)
        root_child0.set_position(Edge.Top, 0)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(100)
        root_child0_child0.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, -50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

    def test_absolute_layout_within_border(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Left, 10)
        root.set_margin(Edge.Top, 10)
        root.set_margin(Edge.Right, 10)
        root.set_margin(Edge.Bottom, 10)
        root.set_padding(Edge.Left, 10)
        root.set_padding(Edge.Top, 10)
        root.set_padding(Edge.Right, 10)
        root.set_padding(Edge.Bottom, 10)
        root.set_border(Edge.Left, 10)
        root.set_border(Edge.Top, 10)
        root.set_border(Edge.Right, 10)
        root.set_border(Edge.Bottom, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 0)
        root_child0.set_position(Edge.Top, 0)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.position_type = PositionType.Absolute
        root_child1.set_position(Edge.Right, 0)
        root_child1.set_position(Edge.Bottom, 0)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.position_type = PositionType.Absolute
        root_child2.set_position(Edge.Left, 0)
        root_child2.set_position(Edge.Top, 0)
        root_child2.set_margin(Edge.Left, 10)
        root_child2.set_margin(Edge.Top, 10)
        root_child2.set_margin(Edge.Right, 10)
        root_child2.set_margin(Edge.Bottom, 10)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.position_type = PositionType.Absolute
        root_child3.set_position(Edge.Right, 0)
        root_child3.set_position(Edge.Bottom, 0)
        root_child3.set_margin(Edge.Left, 10)
        root_child3.set_margin(Edge.Top, 10)
        root_child3.set_margin(Edge.Right, 10)
        root_child3.set_margin(Edge.Bottom, 10)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 10)
        assert_float_approx(root.layout_top, 10)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 30)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 10)
        assert_float_approx(root.layout_top, 10)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 30)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

    def test_absolute_layout_align_items_and_justify_content_center(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_and_justify_content_flex_end(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.FlexEnd
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_justify_content_center(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_center(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_center_on_child_only(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.align_self = Align.Center
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_and_justify_content_center_and_top_position(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Top, 10)
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_and_justify_content_center_and_bottom_position(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_and_justify_content_center_and_left_position(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 5)
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_absolute_layout_align_items_and_justify_content_center_and_right_position(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_grow = 1
        root.width = YGValuePoint(110)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Right, 5)
        root_child0.width = YGValuePoint(60)
        root_child0.height = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 110)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 40)

    def test_position_root_with_rtl_should_position_withoutdirection(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_position(Edge.Left, 72)
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 72)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 72)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

    def test_absolute_layout_percentage_bottom_based_on_parent_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Top, YGValuePercent(50))
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.position_type = PositionType.Absolute
        root_child1.set_position(Edge.Bottom, YGValuePercent(50))
        root_child1.width = YGValuePoint(10)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.position_type = PositionType.Absolute
        root_child2.set_position(Edge.Top, YGValuePercent(10))
        root_child2.set_position(Edge.Bottom, YGValuePercent(10))
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 90)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 160)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 90)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 160)

    def test_absolute_layout_in_wrap_reverse_column_container(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_absolute_layout_in_wrap_reverse_row_container(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_absolute_layout_in_wrap_reverse_column_container_flex_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexEnd
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_absolute_layout_in_wrap_reverse_row_container_flex_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexEnd
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_percent_absolute_position_infinite_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(300)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.position_type = PositionType.Absolute
        root_child1.set_position(Edge.Left, YGValuePercent(20))
        root_child1.set_position(Edge.Top, YGValuePercent(20))
        root_child1.width = YGValuePercent(20)
        root_child1.height = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 0)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 300)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 60)
        assert_float_approx(root_child1.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 0)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 300)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 60)
        assert_float_approx(root_child1.layout_height, 0)

    def test_absolute_layout_percentage_height_based_on_padded_parent(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Top, 10)
        root.set_border(Edge.Top, 10)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePercent(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 45)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 45)

    def test_absolute_layout_percentage_height_based_on_padded_parent_and_align_items_center(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.set_padding(Edge.Top, 20)
        root.set_padding(Edge.Bottom, 20)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePercent(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 50)

    def test_absolute_layout_padding_left(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 100)
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

    def test_absolute_layout_padding_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Right, 100)
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

    def test_absolute_layout_padding_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Top, 100)
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

    def test_absolute_layout_padding_bottom(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Bottom, 100)
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

    def test_absolute_layout_padding(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Right, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_padding(Edge.Left, 50)
        root_child0_child0.set_padding(Edge.Top, 50)
        root_child0_child0.set_padding(Edge.Right, 50)
        root_child0_child0.set_padding(Edge.Bottom, 50)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 220)
        assert_float_approx(root.layout_height, 220)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 220)
        assert_float_approx(root.layout_height, 220)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 50)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_absolute_layout_border(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Right, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(200)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_border(Edge.Left, 10)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 10)
        root_child0_child0.set_border(Edge.Bottom, 10)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 220)
        assert_float_approx(root.layout_height, 220)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 220)
        assert_float_approx(root.layout_height, 220)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 140)
        assert_float_approx(root_child0_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

    def test_absolute_layout_column_reverse_margin_border(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.ColumnReverse
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 5)
        root_child0.set_position(Edge.Right, 3)
        root_child0.set_margin(Edge.Left, 3)
        root_child0.set_margin(Edge.Right, 4)
        root_child0.set_border(Edge.Left, 1)
        root_child0.set_border(Edge.Right, 7)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 8)
        assert_float_approx(root_child0.layout_top, 150)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 143)
        assert_float_approx(root_child0.layout_top, 150)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)
