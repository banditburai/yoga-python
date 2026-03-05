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


class TestFlexWrap:
    def test_wrap_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(30)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(30)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(30)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 60)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 30)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 30)
        assert_float_approx(root_child2.layout_top, 60)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

    def test_wrap_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(30)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(30)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(30)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 60)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 60)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

    def test_wrap_row_align_items_flex_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(30)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 60)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 60)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

    def test_wrap_row_align_items_center(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(30)
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 60)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 5)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 60)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 5)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 30)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 30)

    def test_flex_wrap_children_with_min_main_overriding_flex_basis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.min_width = YGValuePoint(55)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_basis = YGValuePoint(50)
        root_child1.min_width = YGValuePoint(55)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 55)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 55)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 45)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 55)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 45)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 55)
        assert_float_approx(root_child1.layout_height, 50)

    def test_flex_wrap_wrap_to_child_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.align_items = Align.FlexStart
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(100)
        root_child0_child0_child0.height = YGValuePoint(100)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

    def test_flex_wrap_align_stretch_fits_one_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
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
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 0)

    def test_wrap_reverse_row_align_content_flex_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(40)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(30)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 40)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

    def test_wrap_reverse_row_align_content_center(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(40)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(30)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 40)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

    def test_wrap_reverse_row_single_line_different_size(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(40)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(30)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 40)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 90)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 120)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 270)
        assert_float_approx(root_child0.layout_top, 40)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 240)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 210)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 180)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 150)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

    def test_wrap_reverse_row_align_content_stretch(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(40)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(30)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 40)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

    def test_wrap_reverse_row_align_content_space_around(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.SpaceAround
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(40)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(30)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 70)
        assert_float_approx(root_child0.layout_top, 70)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 60)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 10)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 70)
        assert_float_approx(root_child3.layout_top, 10)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 40)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

    def test_wrap_reverse_column_fixed_size(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.WrapReverse
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(30)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(30)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(30)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(30)
        root_child3.height = YGValuePoint(40)
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.width = YGValuePoint(30)
        root_child4.height = YGValuePoint(50)
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 170)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 170)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 170)
        assert_float_approx(root_child2.layout_top, 30)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 170)
        assert_float_approx(root_child3.layout_top, 60)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 140)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 30)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 30)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 60)
        assert_float_approx(root_child3.layout_width, 30)
        assert_float_approx(root_child3.layout_height, 40)

        assert_float_approx(root_child4.layout_left, 30)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 30)
        assert_float_approx(root_child4.layout_height, 50)

    def test_wrapped_row_within_align_items_center(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(150)
        root_child0_child0.height = YGValuePoint(80)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(80)
        root_child0_child1.height = YGValuePoint(80)
        root_child0.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 160)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 150)
        assert_float_approx(root_child0_child0.layout_height, 80)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 80)
        assert_float_approx(root_child0_child1.layout_width, 80)
        assert_float_approx(root_child0_child1.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 160)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 150)
        assert_float_approx(root_child0_child0.layout_height, 80)

        assert_float_approx(root_child0_child1.layout_left, 120)
        assert_float_approx(root_child0_child1.layout_top, 80)
        assert_float_approx(root_child0_child1.layout_width, 80)
        assert_float_approx(root_child0_child1.layout_height, 80)

    def test_wrapped_row_within_align_items_flex_start(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(150)
        root_child0_child0.height = YGValuePoint(80)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(80)
        root_child0_child1.height = YGValuePoint(80)
        root_child0.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 160)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 150)
        assert_float_approx(root_child0_child0.layout_height, 80)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 80)
        assert_float_approx(root_child0_child1.layout_width, 80)
        assert_float_approx(root_child0_child1.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 160)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 150)
        assert_float_approx(root_child0_child0.layout_height, 80)

        assert_float_approx(root_child0_child1.layout_left, 120)
        assert_float_approx(root_child0_child1.layout_top, 80)
        assert_float_approx(root_child0_child1.layout_width, 80)
        assert_float_approx(root_child0_child1.layout_height, 80)

    def test_wrapped_column_max_height(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_content = Align.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(700)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(500)
        root_child0.max_height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_margin(Edge.Left, YGValuePoint(20))
        root_child1.set_margin(Edge.Top, YGValuePoint(20))
        root_child1.set_margin(Edge.Right, YGValuePoint(20))
        root_child1.set_margin(Edge.Bottom, YGValuePoint(20))
        root_child1.width = YGValuePoint(200)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 700)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 250)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 200)
        assert_float_approx(root_child1.layout_top, 250)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 200)

        assert_float_approx(root_child2.layout_left, 420)
        assert_float_approx(root_child2.layout_top, 200)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 700)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 350)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 300)
        assert_float_approx(root_child1.layout_top, 250)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 200)

        assert_float_approx(root_child2.layout_left, 180)
        assert_float_approx(root_child2.layout_top, 200)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

    def test_wrapped_column_max_height_flex(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_content = Align.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(700)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(500)
        root_child0.max_height = YGValuePoint(200)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.set_margin(Edge.Left, YGValuePoint(20))
        root_child1.set_margin(Edge.Top, YGValuePoint(20))
        root_child1.set_margin(Edge.Right, YGValuePoint(20))
        root_child1.set_margin(Edge.Bottom, YGValuePoint(20))
        root_child1.width = YGValuePoint(200)
        root_child1.height = YGValuePoint(200)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 700)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 300)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 180)

        assert_float_approx(root_child1.layout_left, 250)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 180)

        assert_float_approx(root_child2.layout_left, 300)
        assert_float_approx(root_child2.layout_top, 400)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 700)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 300)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 180)

        assert_float_approx(root_child1.layout_left, 250)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 180)

        assert_float_approx(root_child2.layout_left, 300)
        assert_float_approx(root_child2.layout_top, 400)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

    def test_wrap_nodes_with_content_sizing_overflowing_margin(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(85)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(40)
        root_child0_child0_child0.height = YGValuePoint(40)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.set_margin(Edge.Right, YGValuePoint(10))
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child1_child0 = Node(config)
        root_child0_child1_child0.width = YGValuePoint(40)
        root_child0_child1_child0.height = YGValuePoint(40)
        root_child0_child1.insert_child(root_child0_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 85)
        assert_float_approx(root_child0.layout_height, 80)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 40)
        assert_float_approx(root_child0_child1.layout_width, 40)
        assert_float_approx(root_child0_child1.layout_height, 40)

        assert_float_approx(root_child0_child1_child0.layout_left, 0)
        assert_float_approx(root_child0_child1_child0.layout_top, 0)
        assert_float_approx(root_child0_child1_child0.layout_width, 40)
        assert_float_approx(root_child0_child1_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 415)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 85)
        assert_float_approx(root_child0.layout_height, 80)

        assert_float_approx(root_child0_child0.layout_left, 45)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child1.layout_left, 35)
        assert_float_approx(root_child0_child1.layout_top, 40)
        assert_float_approx(root_child0_child1.layout_width, 40)
        assert_float_approx(root_child0_child1.layout_height, 40)

        assert_float_approx(root_child0_child1_child0.layout_left, 0)
        assert_float_approx(root_child0_child1_child0.layout_top, 0)
        assert_float_approx(root_child0_child1_child0.layout_width, 40)
        assert_float_approx(root_child0_child1_child0.layout_height, 40)

    def test_wrap_nodes_with_content_sizing_margin_cross(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(70)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(40)
        root_child0_child0_child0.height = YGValuePoint(40)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.set_margin(Edge.Top, YGValuePoint(10))
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child1_child0 = Node(config)
        root_child0_child1_child0.width = YGValuePoint(40)
        root_child0_child1_child0.height = YGValuePoint(40)
        root_child0_child1.insert_child(root_child0_child1_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 70)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 40)
        assert_float_approx(root_child0_child1.layout_height, 40)

        assert_float_approx(root_child0_child1_child0.layout_left, 0)
        assert_float_approx(root_child0_child1_child0.layout_top, 0)
        assert_float_approx(root_child0_child1_child0.layout_width, 40)
        assert_float_approx(root_child0_child1_child0.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 430)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 70)
        assert_float_approx(root_child0.layout_height, 90)

        assert_float_approx(root_child0_child0.layout_left, 30)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 40)
        assert_float_approx(root_child0_child0_child0.layout_height, 40)

        assert_float_approx(root_child0_child1.layout_left, 30)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 40)
        assert_float_approx(root_child0_child1.layout_height, 40)

        assert_float_approx(root_child0_child1_child0.layout_left, 0)
        assert_float_approx(root_child0_child1_child0.layout_top, 0)
        assert_float_approx(root_child0_child1_child0.layout_width, 40)
        assert_float_approx(root_child0_child1_child0.layout_height, 40)

    def test_wrap_with_min_cross_axis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
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
        assert_float_approx(root_child1.layout_top, 200)
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
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_width, 400)
        assert_float_approx(root_child1.layout_height, 200)

    def test_wrap_with_max_cross_axis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
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

    def test_nowrap_expands_flexline_box_to_min_cross(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.min_height = YGValuePoint(400)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 400)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 400)

    def test_wrapped_row_within_align_items_flex_end(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(150)
        root_child0_child0.height = YGValuePoint(80)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(80)
        root_child0_child1.height = YGValuePoint(80)
        root_child0.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 160)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 150)
        assert_float_approx(root_child0_child0.layout_height, 80)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 80)
        assert_float_approx(root_child0_child1.layout_width, 80)
        assert_float_approx(root_child0_child1.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 160)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 150)
        assert_float_approx(root_child0_child0.layout_height, 80)

        assert_float_approx(root_child0_child1.layout_left, 120)
        assert_float_approx(root_child0_child1.layout_top, 80)
        assert_float_approx(root_child0_child1.layout_width, 80)
        assert_float_approx(root_child0_child1.layout_height, 80)

    def test_wrap_does_not_impose_min_cross_onto_single_flexline(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.min_height = YGValuePoint(400)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)
