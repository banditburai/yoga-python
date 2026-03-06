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
    BoxSizing,
    MeasureMode,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class MeasureCounter:
    def __init__(self):
        self.count = 0


def _make_measure(counter=None):
    def measure(node, width, width_mode, height, height_mode):
        if counter is not None:
            counter.count += 1
        return {"width": 10, "height": 10}

    return measure


def _make_simulate_wrapping_text():
    def simulate_wrapping_text(node, width, width_mode, height, height_mode):
        if width_mode == MeasureMode.Undefined or width >= 68:
            return {"width": 68, "height": 16}
        return {"width": 50, "height": 32}

    return simulate_wrapping_text


def _make_measure_assert_negative():
    def measure_assert_negative(node, width, width_mode, height, height_mode):
        assert width >= 0, "width should not be negative"
        assert height >= 0, "height should not be negative"
        return {"width": 0, "height": 0}

    return measure_assert_negative


def _make_measure_90_10():
    def measure_90_10(node, width, width_mode, height, height_mode):
        return {"width": 90, "height": 10}

    return measure_90_10


def _make_measure_100_100():
    def measure_100_100(node, width, width_mode, height, height_mode):
        return {"width": 100, "height": 100}

    return measure_100_100


def _make_measure_half_width_height(counter=None):
    def measure_half_width_height(node, width, width_mode, height, height_mode):
        if counter is not None:
            counter.count += 1
        return {"width": 0.5 * width, "height": 0.5 * height}

    return measure_half_width_height


class TestMeasure:
    def test_dont_measure_single_grow_shrink_child(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(measure_counter))
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 0

    def test_measure_absolute_child_with_no_constraints(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root.insert_child(root_child0, 0)

        measure_counter = MeasureCounter()

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.set_measure_func(_make_measure(measure_counter))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 1

    def test_dont_measure_when_min_equals_max(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(measure_counter))
        root_child0.min_width = YGValuePoint(10)
        root_child0.max_width = YGValuePoint(10)
        root_child0.min_height = YGValuePoint(10)
        root_child0.max_height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 0
        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_dont_measure_when_min_equals_max_percentages(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(measure_counter))
        root_child0.min_width = YGValuePercent(10)
        root_child0.max_width = YGValuePercent(10)
        root_child0.min_height = YGValuePercent(10)
        root_child0.max_height = YGValuePercent(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 0
        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_measure_nodes_with_margin_auto_and_stretch(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure())
        root_child0.set_margin_auto(Edge.Left)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_left, 490)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_dont_measure_when_min_equals_max_mixed_width_percent(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(measure_counter))
        root_child0.min_width = YGValuePercent(10)
        root_child0.max_width = YGValuePercent(10)
        root_child0.min_height = YGValuePoint(10)
        root_child0.max_height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 0
        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_dont_measure_when_min_equals_max_mixed_height_percent(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(measure_counter))
        root_child0.min_width = YGValuePoint(10)
        root_child0.max_width = YGValuePoint(10)
        root_child0.min_height = YGValuePercent(10)
        root_child0.max_height = YGValuePercent(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 0
        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_measure_enough_size_should_be_in_single_line(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexStart
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_width, 68)
        assert_float_approx(root_child0.layout_height, 16)

    def test_measure_not_enough_size_should_wrap(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(55)

        root_child0 = Node(config)
        root_child0.align_self = Align.FlexStart
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 32)

    def test_measure_zero_space_should_grow(self):
        config = Config()
        root = Node(config)
        root.height = YGValuePoint(200)
        root.flex_direction = FlexDirection.Column
        root.flex_grow = 0

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Column
        root_child0.set_padding(Edge.All, 100)
        root_child0.set_measure_func(_make_measure(measure_counter))
        root.insert_child(root_child0, 0)

        root.calculate_layout(282, float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_width, 282)
        assert_float_approx(root_child0.layout_top, 0)

    def test_measure_flex_direction_row_and_padding(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.set_padding(Edge.Left, 25)
        root.set_padding(Edge.Top, 25)
        root.set_padding(Edge.Right, 25)
        root.set_padding(Edge.Bottom, 25)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 25)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_measure_flex_direction_column_and_padding(self):
        config = Config()

        root = Node(config)
        root.set_margin(Edge.Top, 20)
        root.set_padding(Edge.All, 25)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 32)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 57)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_measure_flex_direction_row_no_padding(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.set_margin(Edge.Top, 20)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_measure_flex_direction_row_no_padding_align_items_flexstart(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.set_margin(Edge.Top, 20)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)
        root.align_items = Align.FlexStart

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 32)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_measure_with_fixed_size(self):
        config = Config()

        root = Node(config)
        root.set_margin(Edge.Top, 20)
        root.set_padding(Edge.All, 25)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 35)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_measure_with_flex_shrink(self):
        config = Config()

        root = Node(config)
        root.set_margin(Edge.Top, 20)
        root.set_padding(Edge.All, 25)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root_child0.flex_shrink = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 25)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 25)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_measure_no_padding(self):
        config = Config()

        root = Node(config)
        root.set_margin(Edge.Top, 20)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_simulate_wrapping_text())
        root_child0.flex_shrink = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(5)
        root_child1.height = YGValuePoint(5)
        root.insert_child(root_child1, 1)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 20)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 32)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 32)
        assert_float_approx(root_child1.layout_width, 5)
        assert_float_approx(root_child1.layout_height, 5)

    def test_can_nullify_measure_func_on_any_node(self):
        config = Config()
        root = Node(config)
        root.insert_child(Node(config), 0)
        root.set_measure_func(None)
        assert root.has_measure_func() == False

    def test_cannot_add_child_to_node_with_measure_func(self):
        root = Node()
        root.set_measure_func(_make_measure())

        root_child0 = Node()
        with pytest.raises((RuntimeError, ValueError)):
            root.insert_child(root_child0, 0)

    def test_cannot_add_nonnull_measure_func_to_non_leaf_node(self):
        root = Node()
        root_child0 = Node()
        root.insert_child(root_child0, 0)

        with pytest.raises((RuntimeError, ValueError)):
            root.set_measure_func(_make_measure())

    def test_cant_call_negative_measure(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Column
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(10)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_assert_negative())
        root_child0.set_margin(Edge.Top, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

    def test_cant_call_negative_measure_horizontal(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = YGValuePoint(10)
        root.height = YGValuePoint(20)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_assert_negative())
        root_child0.set_margin(Edge.Start, 20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

    def test_percent_with_text_node(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceBetween
        root.align_items = Align.Center
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(80)

        root_child0 = Node(config)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_measure_func(_make_measure_90_10())
        root_child1.max_width = YGValuePercent(50)
        root_child1.set_padding(Edge.Top, YGValuePercent(50))
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 40)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 60)

    def test_percent_margin_with_measure_func(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root_child0.set_margin(Edge.Top, 0)
        root_child0.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root_child1.set_margin(Edge.Top, 100)
        root_child1.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root_child2.height = YGValuePoint(100)
        root_child2.set_margin(Edge.Top, YGValuePercent(10))
        root_child2.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = YGValuePoint(100)
        root_child3.height = YGValuePoint(100)
        root_child3.set_margin(Edge.Top, YGValuePercent(20))
        root_child3.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 200)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 300)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 100)

    def test_percent_padding_with_measure_func(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexStart
        root.align_content = Align.FlexStart
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root_child0.set_padding(Edge.Top, 0)
        root_child0.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root_child1.set_padding(Edge.Top, 100)
        root_child1.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.set_padding(Edge.Top, YGValuePercent(10))
        root_child2.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.set_padding(Edge.Top, YGValuePercent(20))
        root_child3.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 200)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 150)

        assert_float_approx(root_child3.layout_left, 300)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 200)

    def test_percent_padding_and_percent_margin_with_measure_func(self):
        config = Config()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexStart
        root.align_content = Align.FlexStart
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root_child0.set_padding(Edge.Top, 0)
        root_child0.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(100)
        root_child1.set_padding(Edge.Top, 100)
        root_child1.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.set_padding(Edge.Top, YGValuePercent(10))
        root_child2.set_margin(Edge.Top, YGValuePercent(10))
        root_child2.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.set_padding(Edge.Top, YGValuePercent(20))
        root_child3.set_margin(Edge.Top, YGValuePercent(20))
        root_child3.set_measure_func(_make_measure_100_100())
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 200)
        assert_float_approx(root_child2.layout_top, 50)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 150)

        assert_float_approx(root_child3.layout_left, 300)
        assert_float_approx(root_child3.layout_top, 100)
        assert_float_approx(root_child3.layout_width, 100)
        assert_float_approx(root_child3.layout_height, 200)

    def test_measure_content_box(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)
        root.box_sizing = BoxSizing.ContentBox
        root.set_padding(Edge.All, 5)
        root.set_border(Edge.All, 10)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_half_width_height(measure_counter))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 1

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 130)
        assert_float_approx(root.layout_height, 230)

        assert_float_approx(root_child0.layout_left, 15)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

    def test_measure_border_box(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(200)
        root.box_sizing = BoxSizing.BorderBox
        root.set_padding(Edge.All, 5)
        root.set_border(Edge.All, 10)

        measure_counter = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_half_width_height(measure_counter))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_counter.count == 1

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 15)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 70)
        assert_float_approx(root_child0.layout_height, 85)
