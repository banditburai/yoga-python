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


def _baseline_func(node, width, height):
    return height / 2


def _measure1(node, width, width_mode, height, height_mode):
    return {"width": 42, "height": 50}


def _measure2(node, width, width_mode, height, height_mode):
    return {"width": 279, "height": 126}


def _createYGNode(config, direction, width, height, alignBaseline):
    node = Node(config)
    node.flex_direction = direction
    if alignBaseline:
        node.align_items = Align.Baseline
    node.width = YGValuePoint(width)
    node.height = YGValuePoint(height)
    return node


class TestAlignBaseline:
    def test_align_baseline_parent_ht_not_specified(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_content = Align.Stretch
        root.align_items = Align.Baseline
        root.width = YGValuePoint(340)
        root.max_height = YGValuePoint(170)
        root.min_height = YGValuePoint(0)

        root_child0 = Node(config)
        root_child0.flex_grow = 0
        root_child0.flex_shrink = 1
        root_child0.set_measure_func(_measure1)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 0
        root_child1.flex_shrink = 1
        root_child1.set_measure_func(_measure2)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 340)
        assert_float_approx(root.layout_height, 126)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 76)
        assert_float_approx(root_child0.layout_width, 42)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 42)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 279)
        assert_float_approx(root_child1.layout_height, 126)

    def test_align_baseline_with_no_parent_ht(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.width = YGValuePoint(150)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(40)
        root_child1.set_baseline_func(_baseline_func)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 70)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 40)

    def test_align_baseline_with_no_baseline_func_and_no_parent_ht(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.width = YGValuePoint(150)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(80)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 150)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 80)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 30)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_align_baseline_parent_using_child_in_column_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Column, 500, 800, False)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_with_padding_in_column_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Column, 500, 800, False)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1_child1.set_padding(Edge.Left, 100)
        root_child1_child1.set_padding(Edge.Right, 100)
        root_child1_child1.set_padding(Edge.Top, 100)
        root_child1_child1.set_padding(Edge.Bottom, 100)
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_with_padding_using_child_in_column_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Column, 500, 800, False)
        root_child1.set_padding(Edge.Left, 100)
        root_child1.set_padding(Edge.Right, 100)
        root_child1.set_padding(Edge.Top, 100)
        root_child1.set_padding(Edge.Bottom, 100)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 0)

        assert_float_approx(root_child1_child0.layout_left, 100)
        assert_float_approx(root_child1_child0.layout_top, 100)

        assert_float_approx(root_child1_child1.layout_left, 100)
        assert_float_approx(root_child1_child1.layout_top, 400)

    def test_align_baseline_parent_with_margin_using_child_in_column_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Column, 500, 800, False)
        root_child1.set_margin(Edge.Left, 100)
        root_child1.set_margin(Edge.Right, 100)
        root_child1.set_margin(Edge.Top, 100)
        root_child1.set_margin(Edge.Bottom, 100)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 600)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_with_margin_in_column_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Column, 500, 800, False)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1_child1.set_margin(Edge.Left, 100)
        root_child1_child1.set_margin(Edge.Right, 100)
        root_child1_child1.set_margin(Edge.Top, 100)
        root_child1_child1.set_margin(Edge.Bottom, 100)
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 0)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 100)
        assert_float_approx(root_child1_child1.layout_top, 400)

    def test_align_baseline_parent_using_child_in_row_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Row, 500, 800, True)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 500, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 500)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_with_padding_in_row_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Row, 500, 800, True)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 500, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1_child1.set_padding(Edge.Left, 100)
        root_child1_child1.set_padding(Edge.Right, 100)
        root_child1_child1.set_padding(Edge.Top, 100)
        root_child1_child1.set_padding(Edge.Bottom, 100)
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 500)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_with_margin_in_row_as_reference(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Row, 500, 800, True)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 500, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1_child1.set_margin(Edge.Left, 100)
        root_child1_child1.set_margin(Edge.Right, 100)
        root_child1_child1.set_margin(Edge.Top, 100)
        root_child1_child1.set_margin(Edge.Bottom, 100)
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 600)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_in_column_as_reference_with_no_baseline_func(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Column, 500, 800, False)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 0)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_in_row_as_reference_with_no_baseline_func(self):
        config = Config()

        root = _createYGNode(config, FlexDirection.Row, 1000, 1000, True)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = _createYGNode(config, FlexDirection.Row, 500, 800, True)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 500, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 500)
        assert_float_approx(root_child1_child1.layout_top, 100)

    def test_align_baseline_parent_using_child_in_column_as_reference_with_height_not_specified(
        self,
    ):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.width = YGValuePoint(1000)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Column
        root_child1.width = YGValuePoint(500)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_height, 800)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_height, 700)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_in_row_as_reference_with_height_not_specified(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.width = YGValuePoint(1000)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Row
        root_child1.width = YGValuePoint(500)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 500, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.set_baseline_func(_baseline_func)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_height, 900)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 400)
        assert_float_approx(root_child1.layout_height, 500)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 500)
        assert_float_approx(root_child1_child1.layout_top, 0)

    def test_align_baseline_parent_using_child_in_column_as_reference_with_no_baseline_func_and_height_not_specified(
        self,
    ):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.width = YGValuePoint(1000)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Column
        root_child1.width = YGValuePoint(500)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 300, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 100)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_height, 700)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 300)

    def test_align_baseline_parent_using_child_in_row_as_reference_with_no_baseline_func_and_height_not_specified(
        self,
    ):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Baseline
        root.width = YGValuePoint(1000)

        root_child0 = _createYGNode(config, FlexDirection.Column, 500, 600, False)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_direction = FlexDirection.Row
        root_child1.width = YGValuePoint(500)
        root.insert_child(root_child1, 1)

        root_child1_child0 = _createYGNode(config, FlexDirection.Column, 500, 500, False)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = _createYGNode(config, FlexDirection.Column, 500, 400, False)
        root_child1_child1.is_reference_baseline = True
        root_child1.insert_child(root_child1_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_height, 700)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)

        assert_float_approx(root_child1.layout_left, 500)
        assert_float_approx(root_child1.layout_top, 200)
        assert_float_approx(root_child1.layout_height, 500)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)

        assert_float_approx(root_child1_child1.layout_left, 500)
        assert_float_approx(root_child1_child1.layout_top, 0)
