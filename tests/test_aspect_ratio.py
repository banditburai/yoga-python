import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    PositionType,
    Overflow,
    YGValuePoint,
    YGValuePercent,
    Align,
    Justify,
    Edge,
    MeasureMode,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


def _measure(node, width, width_mode, height, height_mode):
    return {
        "width": width if width_mode == MeasureMode.Exactly else 50,
        "height": height if height_mode == MeasureMode.Exactly else 50,
    }


class TestAspectRatio:
    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_aspect_ratio_does_not_stretch_cross_axis_dim(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.overflow = Overflow.Scroll
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.flex_grow = 2
        root_child0_child0_child0.flex_shrink = 1
        root_child0_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0_child0.aspect_ratio = 1 / 1
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.width = YGValuePoint(5)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child2 = Node(config)
        root_child0_child0_child2.flex_grow = 1
        root_child0_child0_child2.flex_shrink = 1
        root_child0_child0_child2.flex_basis = YGValuePercent(0)
        root_child0_child0.insert_child(root_child0_child0_child2, 2)

        root_child0_child0_child2_child0 = Node(config)
        root_child0_child0_child2_child0.flex_grow = 1
        root_child0_child0_child2_child0.flex_shrink = 1
        root_child0_child0_child2_child0.flex_basis = YGValuePercent(0)
        root_child0_child0_child2_child0.aspect_ratio = 1 / 1
        root_child0_child0_child2.insert_child(root_child0_child0_child2_child0, 0)

        root_child0_child0_child2_child0_child0 = Node(config)
        root_child0_child0_child2_child0_child0.width = YGValuePoint(5)
        root_child0_child0_child2_child0.insert_child(root_child0_child0_child2_child0_child0, 0)

        root_child0_child0_child2_child0_child1 = Node(config)
        root_child0_child0_child2_child0_child1.flex_grow = 1
        root_child0_child0_child2_child0_child1.flex_shrink = 1
        root_child0_child0_child2_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child0_child2_child0_child1.aspect_ratio = 1 / 1
        root_child0_child0_child2_child0.insert_child(root_child0_child0_child2_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 300)
        assert_float_approx(root_child0.layout_height, 300)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 300)
        assert_float_approx(root_child0_child0.layout_height, 197)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 197)
        assert_float_approx(root_child0_child0_child0.layout_height, 197)

        assert_float_approx(root_child0_child0_child1.layout_left, 197)
        assert_float_approx(root_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1.layout_width, 5)
        assert_float_approx(root_child0_child0_child1.layout_height, 197)

        assert_float_approx(root_child0_child0_child2.layout_left, 202)
        assert_float_approx(root_child0_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child0_child2.layout_width, 98)
        assert_float_approx(root_child0_child0_child2.layout_height, 197)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 98)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 197)

        assert_float_approx(root_child0_child0_child2_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child2_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child2_child0_child0.layout_width, 5)
        assert_float_approx(root_child0_child0_child2_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child2_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child0_child2_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child2_child0_child1.layout_width, 98)
        assert_float_approx(root_child0_child0_child2_child0_child1.layout_height, 197)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 300)
        assert_float_approx(root_child0.layout_height, 300)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 300)
        assert_float_approx(root_child0_child0.layout_height, 197)

        assert_float_approx(root_child0_child0_child0.layout_left, 103)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 197)
        assert_float_approx(root_child0_child0_child0.layout_height, 197)

        assert_float_approx(root_child0_child0_child1.layout_left, 98)
        assert_float_approx(root_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1.layout_width, 5)
        assert_float_approx(root_child0_child0_child1.layout_height, 197)

        assert_float_approx(root_child0_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child0_child2.layout_width, 98)
        assert_float_approx(root_child0_child0_child2.layout_height, 197)

        assert_float_approx(root_child0_child0_child2_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child2_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child2_child0.layout_width, 98)
        assert_float_approx(root_child0_child0_child2_child0.layout_height, 197)

        assert_float_approx(root_child0_child0_child2_child0_child0.layout_left, 93)
        assert_float_approx(root_child0_child0_child2_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child2_child0_child0.layout_width, 5)
        assert_float_approx(root_child0_child0_child2_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child2_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child0_child2_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child2_child0_child1.layout_width, 98)
        assert_float_approx(root_child0_child0_child2_child0_child1.layout_height, 197)

    def test_zero_aspect_ratio_behaves_like_auto(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(300)
        root.height = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.aspect_ratio = 0 / 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 300)

        assert_float_approx(root_child0.layout_left, 250)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

    def test_aspect_ratio_cross_defined(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_main_defined(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_both_dimensions_defined_row(self):
        root = Node()
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 100
        root_child0.height = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

    def test_aspect_ratio_both_dimensions_defined_column(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 100
        root_child0.height = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_align_stretch(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

    def test_aspect_ratio_flex_grow(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

    def test_aspect_ratio_flex_shrink(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 150
        root_child0.flex_shrink = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

    def test_aspect_ratio_flex_shrink_2(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.set_height_percent(100)
        root_child0.flex_shrink = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node()
        root_child1.set_height_percent(100)
        root_child1.flex_shrink = 1
        root_child1.aspect_ratio = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

        assert root_child1.layout_left == 0
        assert root_child1.layout_top == 50
        assert root_child1.layout_width == 50
        assert root_child1.layout_height == 50

    def test_aspect_ratio_basis(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.flex_basis = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_absolute_layout_width_defined(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 0)
        root_child0.set_position(Edge.Top, 0)
        root_child0.width = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_absolute_layout_height_defined(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 0)
        root_child0.set_position(Edge.Top, 0)
        root_child0.height = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_with_max_cross_defined(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.max_width = 40
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 40
        assert root_child0.layout_height == 50

    def test_aspect_ratio_with_max_main_defined(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.max_height = 40
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 40
        assert root_child0.layout_height == 40

    def test_aspect_ratio_with_min_cross_defined(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 30
        root_child0.min_width = 40
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 40
        assert root_child0.layout_height == 30

    def test_aspect_ratio_with_min_main_defined(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 30
        root_child0.min_height = 40
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 40
        assert root_child0.layout_height == 40

    def test_aspect_ratio_double_cross(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.aspect_ratio = 2
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 50

    def test_aspect_ratio_half_cross(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 100
        root_child0.aspect_ratio = 0.5
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 100

    def test_aspect_ratio_double_main(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.aspect_ratio = 0.5
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 100

    def test_aspect_ratio_half_main(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 100
        root_child0.aspect_ratio = 2
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 50

    def test_aspect_ratio_with_measure_func(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.set_measure_func(_measure)
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_width_height_flex_grow_row(self):
        root = Node()
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 200

        root_child0 = Node()
        root_child0.width = 50
        root_child0.height = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

    def test_aspect_ratio_width_height_flex_grow_column(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 200
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.height = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

    def test_aspect_ratio_height_as_flex_basis(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.flex_direction = FlexDirection.Row
        root.width = 200
        root.height = 200

        root_child0 = Node()
        root_child0.height = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node()
        root_child1.height = 100
        root_child1.flex_grow = 1
        root_child1.aspect_ratio = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 75
        assert root_child0.layout_height == 75

        assert root_child1.layout_left == 75
        assert root_child1.layout_top == 0
        assert root_child1.layout_width == 125
        assert root_child1.layout_height == 125

    def test_aspect_ratio_width_as_flex_basis(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 200
        root.height = 200

        root_child0 = Node()
        root_child0.width = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node()
        root_child1.width = 100
        root_child1.flex_grow = 1
        root_child1.aspect_ratio = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 75
        assert root_child0.layout_height == 75

        assert root_child1.layout_left == 0
        assert root_child1.layout_top == 75
        assert root_child1.layout_width == 125
        assert root_child1.layout_height == 125

    def test_aspect_ratio_overrides_flex_grow_row(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.flex_direction = FlexDirection.Row
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 0.5
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 200

    def test_aspect_ratio_overrides_flex_grow_column(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.flex_grow = 1
        root_child0.aspect_ratio = 2
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 200
        assert root_child0.layout_height == 100

    def test_aspect_ratio_left_right_absolute(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 10)
        root_child0.set_position(Edge.Top, 10)
        root_child0.set_position(Edge.Right, 10)
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 10
        assert root_child0.layout_top == 10
        assert root_child0.layout_width == 80
        assert root_child0.layout_height == 80

    def test_aspect_ratio_top_bottom_absolute(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, 10)
        root_child0.set_position(Edge.Top, 10)
        root_child0.set_position(Edge.Bottom, 10)
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 10
        assert root_child0.layout_top == 10
        assert root_child0.layout_width == 80
        assert root_child0.layout_height == 80

    def test_aspect_ratio_width_overrides_align_stretch_row(self):
        root = Node()
        root.flex_direction = FlexDirection.Row
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_height_overrides_align_stretch_column(self):
        root = Node()
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.aspect_ratio = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_allow_child_overflow_parent_size(self):
        root = Node()
        root.align_items = Align.FlexStart
        root.width = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.aspect_ratio = 4
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_width == 100
        assert root.layout_height == 50

        assert root_child0.layout_width == 200
        assert root_child0.layout_height == 50

    def test_aspect_ratio_defined_main_with_margin(self):
        root = Node()
        root.align_items = Align.Center
        root.justify_content = Justify.Center
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.height = 50
        root_child0.aspect_ratio = 1
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Right, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_width == 100
        assert root.layout_height == 100

        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_defined_cross_with_margin(self):
        root = Node()
        root.align_items = Align.Center
        root.justify_content = Justify.Center
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.aspect_ratio = 1
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Right, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_width == 100
        assert root.layout_height == 100

        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_defined_cross_with_main_margin(self):
        root = Node()
        root.align_items = Align.Center
        root.justify_content = Justify.Center
        root.width = 100
        root.height = 100

        root_child0 = Node()
        root_child0.width = 50
        root_child0.aspect_ratio = 1
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_width == 100
        assert root.layout_height == 100

        assert root_child0.layout_width == 50
        assert root_child0.layout_height == 50

    def test_aspect_ratio_should_prefer_explicit_height(self):
        config = Config()
        config.use_web_defaults = True

        root = Node(config)
        root.flex_direction = FlexDirection.Column

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Column
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Column
        root_child0_child0.height = 100
        root_child0_child0.aspect_ratio = 2
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(100, 200, Direction.LTR)

        assert root.layout_width == 100
        assert root.layout_height == 200

        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

        assert root_child0_child0.layout_width == 200
        assert root_child0_child0.layout_height == 100

    def test_aspect_ratio_should_prefer_explicit_width(self):
        config = Config()
        config.use_web_defaults = True

        root = Node(config)
        root.flex_direction = FlexDirection.Row

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.width = 100
        root_child0_child0.aspect_ratio = 0.5
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(200, 100, Direction.LTR)

        assert root.layout_width == 200
        assert root.layout_height == 100

        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

        assert root_child0_child0.layout_width == 100
        assert root_child0_child0.layout_height == 200

    def test_aspect_ratio_should_prefer_flexed_dimension(self):
        config = Config()
        config.use_web_defaults = True

        root = Node(config)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Column
        root_child0.aspect_ratio = 2
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.aspect_ratio = 4
        root_child0_child0.flex_grow = 1
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(100, 100, Direction.LTR)

        assert root.layout_width == 100
        assert root.layout_height == 100

        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 50

        assert root_child0_child0.layout_width == 200
        assert root_child0_child0.layout_height == 50
