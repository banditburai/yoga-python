import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Align,
    YGValuePoint,
    Edge,
    MeasureMode,
)


def _make_measure_max(counter):
    def measure(node, width, width_mode, height, height_mode):
        counter.count += 1
        if width_mode == MeasureMode.Undefined:
            w = 10
        else:
            w = width
        if height_mode == MeasureMode.Undefined:
            h = 10
        else:
            h = height
        return {"width": w, "height": h}

    return measure


def _make_measure_min(counter):
    def measure(node, width, width_mode, height, height_mode):
        counter.count += 1
        if width_mode == MeasureMode.Undefined or (width_mode == MeasureMode.AtMost and width > 10):
            w = 10
        else:
            w = width
        if height_mode == MeasureMode.Undefined or (
            height_mode == MeasureMode.AtMost and height > 10
        ):
            h = 10
        else:
            h = height
        return {"width": w, "height": h}

    return measure


def _make_measure_84_49(counter):
    def measure(node, width, width_mode, height, height_mode):
        if counter is not None:
            counter.count += 1
        return {"width": 84, "height": 49}

    return measure


class MeasureCounter:
    def __init__(self):
        self.count = 0


class TestMeasureCache:
    def test_measure_once_single_flexible_child(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        measure_count = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_max(measure_count))
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_count.count == 1

    def test_remeasure_with_same_exact_width_larger_than_needed_height(self):
        config = Config()
        root = Node(config)

        measure_count = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_min(measure_count))
        root.insert_child(root_child0, 0)

        root.calculate_layout(100, 100, Direction.LTR)
        root.calculate_layout(100, 50, Direction.LTR)

        assert measure_count.count == 1

    def test_remeasure_with_same_atmost_width_larger_than_needed_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart

        measure_count = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_min(measure_count))
        root.insert_child(root_child0, 0)

        root.calculate_layout(100, 100, Direction.LTR)
        root.calculate_layout(100, 50, Direction.LTR)

        assert measure_count.count == 1

    def test_remeasure_with_computed_width_larger_than_needed_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart

        measure_count = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_min(measure_count))
        root.insert_child(root_child0, 0)

        root.calculate_layout(100, 100, Direction.LTR)
        root.align_items = Align.Stretch
        root.calculate_layout(10, 50, Direction.LTR)

        assert measure_count.count == 1

    def test_remeasure_with_atmost_computed_width_undefined_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart

        measure_count = MeasureCounter()

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure_min(measure_count))
        root.insert_child(root_child0, 0)

        root.calculate_layout(100, float("nan"), Direction.LTR)
        root.calculate_layout(10, float("nan"), Direction.LTR)

        assert measure_count.count == 1

    def test_remeasure_with_already_measured_value_smaller_but_still_float_equal(self):
        measure_count = MeasureCounter()

        config = Config()
        root = Node(config)
        root.width = YGValuePoint(288)
        root.height = YGValuePoint(288)
        root.flex_direction = FlexDirection.Row

        root_child0 = Node(config)
        root_child0.set_padding(Edge.All, 2.88)
        root_child0.flex_direction = FlexDirection.Row
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_measure_func(_make_measure_84_49(measure_count))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert measure_count.count == 1
