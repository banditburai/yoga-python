import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Align,
    Overflow,
    MeasureMode,
    YGValuePoint,
)


class MeasureConstraint:
    def __init__(self):
        self.constraints = []
        self.length = 0

    def record(self, width, width_mode, height, height_mode):
        self.constraints.append(
            {
                "width": width,
                "widthMode": width_mode,
                "height": height,
                "heightMode": height_mode,
            }
        )
        self.length = len(self.constraints)


def _make_measure(constraint_list):
    def measure(node, width, width_mode, height, height_mode):
        constraint_list.record(
            width,
            width_mode,
            height,
            height_mode,
        )
        if width_mode == MeasureMode.Undefined:
            w = 10
        else:
            w = width
        if height_mode == MeasureMode.Undefined:
            h = 10
        else:
            h = width  # C++ bug: uses width for height
        return {"width": w, "height": h}

    return measure


class TestMeasureMode:
    def test_exactly_measure_stretched_child_column(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["width"] == 100
        assert constraint_list.constraints[0]["widthMode"] == MeasureMode.Exactly

    def test_exactly_measure_stretched_child_row(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["height"] == 100
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.Exactly

    def test_at_most_main_axis_column(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["height"] == 100
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.AtMost

    def test_at_most_cross_axis_column(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["width"] == 100
        assert constraint_list.constraints[0]["widthMode"] == MeasureMode.AtMost

    def test_at_most_main_axis_row(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["width"] == 100
        assert constraint_list.constraints[0]["widthMode"] == MeasureMode.AtMost

    def test_at_most_cross_axis_row(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["height"] == 100
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.AtMost

    def test_flex_child(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 2

        assert constraint_list.constraints[0]["height"] == 100
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.AtMost

        assert constraint_list.constraints[1]["height"] == 100
        assert constraint_list.constraints[1]["heightMode"] == MeasureMode.Exactly

    def test_flex_child_with_flex_basis(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePoint(0)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1

        assert constraint_list.constraints[0]["height"] == 100
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.Exactly

    def test_overflow_scroll_column(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.align_items = Align.FlexStart
        root.overflow = Overflow.Scroll
        root.height = YGValuePoint(100)
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1
        assert constraint_list.constraints[0]["width"] == 100
        assert constraint_list.constraints[0]["widthMode"] == MeasureMode.AtMost

        import math

        assert math.isnan(constraint_list.constraints[0]["height"])
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.Undefined

    def test_overflow_scroll_row(self):
        config = Config()
        constraint_list = MeasureConstraint()

        root = Node(config)
        root.align_items = Align.FlexStart
        root.flex_direction = FlexDirection.Row
        root.overflow = Overflow.Scroll
        root.height = YGValuePoint(100)
        root.width = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_measure_func(_make_measure(constraint_list))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert constraint_list.length == 1

        import math

        assert math.isnan(constraint_list.constraints[0]["width"])
        assert constraint_list.constraints[0]["widthMode"] == MeasureMode.Undefined

        assert constraint_list.constraints[0]["height"] == 100
        assert constraint_list.constraints[0]["heightMode"] == MeasureMode.AtMost
