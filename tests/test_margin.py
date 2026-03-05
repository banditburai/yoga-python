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


class TestMargin:
    def test_margin_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Start, 10)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

    def test_margin_top(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Top, 10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

    def test_margin_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.End, 10)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 100)

    def test_margin_bottom(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Bottom, 10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 10)

    def test_margin_and_flex_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Start, 10)
        root_child0.set_margin(Edge.End, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 100)

    def test_margin_and_flex_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 80)

    def test_margin_and_stretch_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 80)

    def test_margin_and_stretch_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Start, 10)
        root_child0.set_margin(Edge.End, 10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 80)
        assert_float_approx(root_child0.layout_height, 100)

    def test_margin_with_sibling_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.End, 10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 45)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 55)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 45)
        assert_float_approx(root_child1.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 55)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 45)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 45)
        assert_float_approx(root_child1.layout_height, 100)

    def test_margin_with_sibling_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Bottom, 10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 45)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 45)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 45)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 55)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 45)

    def test_margin_auto_bottom(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Bottom)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_top(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Top)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 100)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_bottom_and_top(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Top)
        root_child0.set_margin_auto(Edge.Bottom)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_bottom_and_top_justify_center(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Top)
        root_child0.set_margin_auto(Edge.Bottom)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_multiple_children_column(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Top)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_margin_auto(Edge.Top)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 25)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 100)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

    def test_margin_auto_multiple_children_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Right)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.set_margin_auto(Edge.Right)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 150)
        assert_float_approx(root_child2.layout_top, 75)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 125)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 75)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 50)

    def test_margin_auto_left_and_right_column(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.set_margin_auto(Edge.Right)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_left_and_right(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.set_margin_auto(Edge.Right)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_start_and_end_column(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Start)
        root_child0.set_margin_auto(Edge.End)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_start_and_end(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Start)
        root_child0.set_margin_auto(Edge.End)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_left_and_right_column_and_center(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.set_margin_auto(Edge.Right)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_left(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_right(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Right)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_left_and_right_stretch(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.set_margin_auto(Edge.Right)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_top_and_bottom_stretch(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Top)
        root_child0.set_margin_auto(Edge.Bottom)
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
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 50)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 150)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_should_not_be_part_of_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(250)
        root.height = YGValuePoint(250)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Top, 20)
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root_child0.max_height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 250)
        assert_float_approx(root.layout_height, 250)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 250)
        assert_float_approx(root.layout_height, 250)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

    def test_margin_should_not_be_part_of_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(250)
        root.height = YGValuePoint(250)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 20)
        root_child0.width = YGValuePoint(100)
        root_child0.max_width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 250)
        assert_float_approx(root.layout_height, 250)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 250)
        assert_float_approx(root.layout_height, 250)

        assert_float_approx(root_child0.layout_left, 150)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

    def test_margin_auto_left_right_child_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.set_margin_auto(Edge.Right)
        root_child0.width = YGValuePoint(72)
        root_child0.height = YGValuePoint(72)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -20)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

    def test_margin_auto_left_child_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.width = YGValuePoint(72)
        root_child0.height = YGValuePoint(72)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -20)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

    def test_margin_fix_left_auto_right_child_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin_auto(Edge.Right)
        root_child0.width = YGValuePoint(72)
        root_child0.height = YGValuePoint(72)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, 10)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -20)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

    def test_margin_auto_left_fix_right_child_bigger_than_parent(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(52)
        root.height = YGValuePoint(52)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Left)
        root_child0.set_margin(Edge.Right, 10)
        root_child0.width = YGValuePoint(72)
        root_child0.height = YGValuePoint(72)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 52)
        assert_float_approx(root.layout_height, 52)

        assert_float_approx(root_child0.layout_left, -30)
        assert_float_approx(root_child0.layout_top, -10)
        assert_float_approx(root_child0.layout_width, 72)
        assert_float_approx(root_child0.layout_height, 72)

    def test_margin_auto_top_stretching_child(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.set_margin_auto(Edge.Top)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 100)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_left_stretching_child(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.set_margin_auto(Edge.Left)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 200)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 200)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 50)

    def test_margin_auto_overflowing_container(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_margin_auto(Edge.Bottom)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(150)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(150)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 150)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child1.layout_left, 75)
        assert_float_approx(root_child1.layout_top, 150)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 150)
