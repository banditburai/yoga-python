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


class TestAlignContent:
    def test_align_content_flex_start_nowrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_flex_start_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root_child4.height = YGValuePoint(10)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 10)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 20)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 10)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 20)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_flex_start_wrap_singleline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_flex_start_wrapped_negative_space(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_flex_start_wrapped_negative_space_gap(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root_child0.set_gap(Gutter.Column, 10)
        root_child0.set_gap(Gutter.Row, 10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_flex_start_without_height_on_children(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 10)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 20)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 10)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 20)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 0)

    def test_align_content_flex_start_with_flex(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.flex_grow = 1
        root_child3.flex_shrink = 1
        root_child3.flex_basis = YGValuePercent(0)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 40)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 80)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 120)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 40)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 40)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 80)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 120)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 0)

    def test_align_content_flex_end_nowrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_flex_end_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root_child4.height = YGValuePoint(10)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 90)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 90)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 110)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 90)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 90)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 100)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 110)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_flex_end_wrap_singleline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 110)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 110)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 110)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 110)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_flex_end_wrapped_negative_space(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.FlexEnd
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, -10)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -50)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, -10)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_flex_end_wrapped_negative_space_gap(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.FlexEnd
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root_child0.set_gap(Gutter.Column, 10)
        root_child0.set_gap(Gutter.Row, 10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -70)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -40)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, -10)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -70)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -40)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, -10)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_center_nowrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_center_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root_child4.height = YGValuePoint(10)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 45)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 45)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 65)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 45)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 45)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 65)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_center_wrap_singleline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 55)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 55)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_center_wrapped_negative_space(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.Center
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -25)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -5)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 15)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -25)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -5)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 15)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_center_wrapped_negative_space_gap(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.Center
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root_child0.set_gap(Gutter.Column, 10)
        root_child0.set_gap(Gutter.Row, 10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -35)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -5)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 25)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, -35)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, -5)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 25)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_between_nowrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceBetween
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_space_between_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceBetween
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root_child4.height = YGValuePoint(10)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 110)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 110)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_space_between_wrap_singleline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceBetween
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_space_between_wrapped_negative_space(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceBetween
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_between_wrapped_negative_space_row_reverse(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceBetween
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_between_wrapped_negative_space_gap(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceBetween
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root_child0.set_gap(Gutter.Column, 10)
        root_child0.set_gap(Gutter.Row, 10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_around_nowrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_space_around_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root_child4.height = YGValuePoint(10)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 15)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 95)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 15)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 95)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_space_around_wrap_singleline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 55)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 55)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_space_around_wrapped_negative_space(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceAround
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_around_wrapped_negative_space_row_reverse(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.RowReverse
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceAround
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_around_wrapped_negative_space_gap(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceAround
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root_child0.set_gap(Gutter.Column, 10)
        root_child0.set_gap(Gutter.Row, 10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_evenly_nowrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_space_evenly_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root_child3.height = YGValuePoint(10)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root_child4.height = YGValuePoint(10)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 23)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 23)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 88)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 23)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 23)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 90)
        assert_float_approx(root_child2.layout_top, 55)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 10)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 55)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 88)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_space_evenly_wrap_singleline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(140)
        root.height = YGValuePoint(120)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 55)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 140)
        assert_float_approx(root.layout_height, 120)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 55)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 10)

    def test_align_content_space_evenly_wrapped_negative_space(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceEvenly
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 20)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 40)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_space_evenly_wrapped_negative_space_gap(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_border(Edge.Left, 60)
        root.set_border(Edge.Top, 60)
        root.set_border(Edge.Right, 60)
        root.set_border(Edge.Bottom, 60)
        root.width = YGValuePoint(320)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.Center
        root_child0.align_content = Align.SpaceEvenly
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(10)
        root_child0.set_gap(Gutter.Column, 10)
        root_child0.set_gap(Gutter.Row, 10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(80)
        root_child0_child0.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(80)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePercent(80)
        root_child0_child2.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 60)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 160)
        assert_float_approx(root_child0_child0.layout_height, 20)

        assert_float_approx(root_child0_child1.layout_left, 20)
        assert_float_approx(root_child0_child1.layout_top, 30)
        assert_float_approx(root_child0_child1.layout_width, 160)
        assert_float_approx(root_child0_child1.layout_height, 20)

        assert_float_approx(root_child0_child2.layout_left, 20)
        assert_float_approx(root_child0_child2.layout_top, 60)
        assert_float_approx(root_child0_child2.layout_width, 160)
        assert_float_approx(root_child0_child2.layout_height, 20)

    def test_align_content_stretch(self):
        config = Config()
        root = Node(config)
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 0)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 0)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 0)

        assert_float_approx(root_child4.layout_left, 100)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 0)

    def test_align_content_stretch_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

    def test_align_content_stretch_row_with_children(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0.insert_child(root_child0_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

    def test_align_content_stretch_row_with_flex(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.flex_grow = 1
        root_child3.flex_shrink = 1
        root_child3.flex_basis = YGValuePercent(0)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 0)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 100)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 0)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 100)

    def test_align_content_stretch_row_with_flex_no_shrink(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.flex_grow = 1
        root_child3.flex_basis = YGValuePercent(0)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 0)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 100)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 0)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 100)

    def test_align_content_stretch_row_with_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_margin(Edge.Left, 10)
        root_child1.set_margin(Edge.Top, 10)
        root_child1.set_margin(Edge.Right, 10)
        root_child1.set_margin(Edge.Bottom, 10)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.set_margin(Edge.Left, 10)
        root_child3.set_margin(Edge.Top, 10)
        root_child3.set_margin(Edge.Right, 10)
        root_child3.set_margin(Edge.Bottom, 10)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 40)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 40)

        assert_float_approx(root_child3.layout_left, 60)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 40)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 40)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 40)

        assert_float_approx(root_child3.layout_left, 40)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 100)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 20)

    def test_align_content_stretch_row_with_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_padding(Edge.Left, 10)
        root_child1.set_padding(Edge.Top, 10)
        root_child1.set_padding(Edge.Right, 10)
        root_child1.set_padding(Edge.Bottom, 10)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.set_padding(Edge.Left, 10)
        root_child3.set_padding(Edge.Top, 10)
        root_child3.set_padding(Edge.Right, 10)
        root_child3.set_padding(Edge.Bottom, 10)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

    def test_align_content_stretch_row_with_single_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

    def test_align_content_stretch_row_with_fixed_height(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(60)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 80)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 60)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 80)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 80)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 60)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 80)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 80)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 20)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 80)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 20)

    def test_align_content_stretch_row_with_max_height(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.max_height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 50)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 50)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

    def test_align_content_stretch_row_with_min_height(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(150)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.min_height = YGValuePoint(80)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 90)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 90)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 90)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 90)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 90)

        assert_float_approx(root_child3.layout_left, 100)
        assert_float_approx(root_child3.layout_top, 90)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 10)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 90)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 10)

    def test_align_content_stretch_column(self):
        config = Config()
        root = Node(config)
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(150)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0.insert_child(root_child0_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.height = YGValuePoint(50)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 50)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        assert_float_approx(root_child3.layout_left, 50)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 50)
        assert_float_approx(root_child3.layout_height, 50)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 50)
        assert_float_approx(root_child4.layout_height, 50)

    def test_align_content_stretch_is_not_overriding_align_items(self):
        config = Config()
        root = Node(config)
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.align_content = Align.Stretch
        root_child0.align_items = Align.Center
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.align_content = Align.Stretch
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

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
        assert_float_approx(root_child0_child0.layout_top, 45)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

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
        assert_float_approx(root_child0_child0.layout_top, 45)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

    def test_align_content_stretch_with_min_cross_axis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(500)
        root.min_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 250)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 250)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

    def test_align_content_stretch_with_max_cross_axis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(500)
        root.max_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

    def test_align_content_stretch_with_max_cross_axis_and_border_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_padding(Edge.Left, 2)
        root.set_padding(Edge.Top, 2)
        root.set_padding(Edge.Right, 2)
        root.set_padding(Edge.Bottom, 2)
        root.set_border(Edge.Left, 5)
        root.set_border(Edge.Top, 5)
        root.set_border(Edge.Right, 5)
        root.set_border(Edge.Bottom, 5)
        root.width = YGValuePoint(500)
        root.max_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 414)

        assert_float_approx(root_child0.layout_left, 7)
        assert_float_approx(root_child0.layout_top, 7)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 7)
        assert_float_approx(root_child1.layout_top, 207)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 414)

        assert_float_approx(root_child0.layout_left, 93)
        assert_float_approx(root_child0.layout_top, 7)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 93)
        assert_float_approx(root_child1.layout_top, 207)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

    def test_align_content_space_evenly_with_min_cross_axis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(500)
        root.min_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 33)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 267)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 33)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 267)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

    def test_align_content_space_evenly_with_max_cross_axis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(500)
        root.max_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

    def test_align_content_space_evenly_with_max_cross_axis_violated(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(500)
        root.max_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(600)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(600)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 600)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 600)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 600)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 600)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 600)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 600)

    def test_align_content_space_evenly_with_max_cross_axis_violated_padding_and_border(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_padding(Edge.Left, 2)
        root.set_padding(Edge.Top, 2)
        root.set_padding(Edge.Right, 2)
        root.set_padding(Edge.Bottom, 2)
        root.set_border(Edge.Left, 5)
        root.set_border(Edge.Top, 5)
        root.set_border(Edge.Right, 5)
        root.set_border(Edge.Bottom, 5)
        root.width = YGValuePoint(500)
        root.max_height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(400)
        root_child0.height = YGValuePoint(600)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(400)
        root_child1.height = YGValuePoint(600)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 7)
        assert_float_approx(root_child0.layout_top, 7)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 600)

        assert_float_approx(root_child1.layout_left, 7)
        assert_float_approx(root_child1.layout_top, 607)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 600)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 93)
        assert_float_approx(root_child0.layout_top, 7)
        assert_float_approx(root_child0.layout_width, 400)
        assert_float_approx(root_child0.layout_height, 600)

        assert_float_approx(root_child1.layout_left, 93)
        assert_float_approx(root_child1.layout_top, 607)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 600)

    def test_align_content_space_around_and_align_items_flex_end_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 88)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 88)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_space_around_and_align_items_center_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 63)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 63)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_space_around_and_align_items_flex_start_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 38)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 38)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_flex_start_stretch_doesnt_influence_line_box_dim(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.align_content = Align.FlexStart
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

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
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 50)

    def test_align_content_stretch_stretch_does_influence_line_box_dim(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.align_content = Align.Stretch
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

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
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 50)

    def test_align_content_space_evenly_stretch_does_influence_line_box_dim(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.set_padding(Edge.Left, 20)
        root.set_padding(Edge.Top, 20)
        root.set_padding(Edge.Right, 20)
        root.set_padding(Edge.Bottom, 20)
        root.width = YGValuePoint(400)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Right, 20)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Row
        root_child1.align_content = Align.Stretch
        root_child1.flex_wrap = Wrap.Wrap
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.set_margin(Edge.Right, 20)
        root_child1_child0.width = YGValuePoint(30)
        root_child1_child0.height = YGValuePoint(30)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = Node(config)
        root_child1_child1.set_margin(Edge.Right, 20)
        root_child1_child1.width = YGValuePoint(30)
        root_child1_child1.height = YGValuePoint(30)
        root_child1.insert_child(root_child1_child1, 1)

        root_child1_child2 = Node(config)
        root_child1_child2.set_margin(Edge.Right, 20)
        root_child1_child2.width = YGValuePoint(30)
        root_child1_child2.height = YGValuePoint(30)
        root_child1.insert_child(root_child1_child2, 2)

        root_child1_child3 = Node(config)
        root_child1_child3.set_margin(Edge.Right, 20)
        root_child1_child3.width = YGValuePoint(30)
        root_child1_child3.height = YGValuePoint(30)
        root_child1.insert_child(root_child1_child3, 3)

        root_child1_child4 = Node(config)
        root_child1_child4.set_margin(Edge.Right, 20)
        root_child1_child4.width = YGValuePoint(30)
        root_child1_child4.height = YGValuePoint(30)
        root_child1.insert_child(root_child1_child4, 4)

        root_child2 = Node(config)
        root_child2.set_margin(Edge.Left, 20)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 140)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 140)
        assert_float_approx(root_child1.layout_top, 20)
        assert_float_approx(root_child1.layout_width, 170)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 30)
        assert_float_approx(root_child1_child0.layout_height, 30)

        assert_float_approx(root_child1_child1.layout_left, 50)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 30)
        assert_float_approx(root_child1_child1.layout_height, 30)

        assert_float_approx(root_child1_child2.layout_left, 100)
        assert_float_approx(root_child1_child2.layout_top, 0)
        assert_float_approx(root_child1_child2.layout_width, 30)
        assert_float_approx(root_child1_child2.layout_height, 30)

        assert_float_approx(root_child1_child3.layout_left, 0)
        assert_float_approx(root_child1_child3.layout_top, 50)
        assert_float_approx(root_child1_child3.layout_width, 30)
        assert_float_approx(root_child1_child3.layout_height, 30)

        assert_float_approx(root_child1_child4.layout_left, 50)
        assert_float_approx(root_child1_child4.layout_top, 50)
        assert_float_approx(root_child1_child4.layout_width, 30)
        assert_float_approx(root_child1_child4.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 330)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 140)

        assert_float_approx(root_child0.layout_left, 260)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 90)
        assert_float_approx(root_child1.layout_top, 20)
        assert_float_approx(root_child1.layout_width, 170)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child1_child0.layout_left, 120)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 30)
        assert_float_approx(root_child1_child0.layout_height, 30)

        assert_float_approx(root_child1_child1.layout_left, 70)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 30)
        assert_float_approx(root_child1_child1.layout_height, 30)

        assert_float_approx(root_child1_child2.layout_left, 20)
        assert_float_approx(root_child1_child2.layout_top, 0)
        assert_float_approx(root_child1_child2.layout_width, 30)
        assert_float_approx(root_child1_child2.layout_height, 30)

        assert_float_approx(root_child1_child3.layout_left, 120)
        assert_float_approx(root_child1_child3.layout_top, 50)
        assert_float_approx(root_child1_child3.layout_width, 30)
        assert_float_approx(root_child1_child3.layout_height, 30)

        assert_float_approx(root_child1_child4.layout_left, 70)
        assert_float_approx(root_child1_child4.layout_top, 50)
        assert_float_approx(root_child1_child4.layout_width, 30)
        assert_float_approx(root_child1_child4.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_stretch_and_align_items_flex_end_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexStart
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 250)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 250)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_stretch_and_align_items_flex_start_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexEnd
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 125)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 175)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 125)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 175)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_stretch_and_align_items_center_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexEnd
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 125)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 125)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 38)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

    def test_align_content_stretch_and_align_items_stretch_with_flex_wrap(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexEnd
        root_child0.width = YGValuePoint(150)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(120)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(120)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 125)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 175)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 125)
        assert_float_approx(root_child0.layout_width, 150)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 120)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 175)
        assert_float_approx(root_child2.layout_width, 120)
        assert_float_approx(root_child2.layout_height, 50)
