import pytest
from yoga import (
    Node,
    Config,
    Direction,
    PositionType,
    YGValuePoint,
    YGValuePercent,
    Display,
    FlexDirection,
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestDisplay:
    def test_display_none(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.display = Display.None_
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

    def test_display_none_fixed_size(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root_child1.height = YGValuePoint(20)
        root_child1.display = Display.None_
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

    def test_display_none_with_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Right, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root_child0.display = Display.None_
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
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

    def test_display_none_with_child(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_shrink = 1
        root_child1.flex_basis = YGValuePercent(0)
        root_child1.display = Display.None_
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.flex_grow = 1
        root_child1_child0.flex_shrink = 1
        root_child1_child0.flex_basis = YGValuePercent(0)
        root_child1_child0.width = YGValuePoint(20)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.flex_shrink = 1
        root_child2.flex_basis = YGValuePercent(0)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        # Debug output
        print(f"DEBUG: child0 left={root_child0.layout_left}, width={root_child0.layout_width}")
        print(f"DEBUG: child1 left={root_child1.layout_left}, width={root_child1.layout_width}")
        print(f"DEBUG: child2 left={root_child2.layout_left}, width={root_child2.layout_width}")
        print(
            f"DEBUG: child1_child0 left={root_child1_child0.layout_left}, width={root_child1_child0.layout_width}"
        )

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 0)
        assert_float_approx(root_child1_child0.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 50)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 0)
        assert_float_approx(root_child1_child0.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 100)

    def test_display_none_with_position(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.set_position(Edge.Top, 10)
        root_child1.display = Display.None_
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

    def test_display_none_with_position_absolute(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(100)
        root_child0.height = YGValuePoint(100)
        root_child0.display = Display.None_
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

    def test_display_contents(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.display = Display.Contents
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0.height = YGValuePoint(10)
        root.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 1
        root_child0_child1.flex_shrink = 1
        root_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child1.height = YGValuePoint(20)
        root.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

    def test_display_contents_fixed_size(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root_child0.display = Display.Contents
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0.height = YGValuePoint(10)
        root.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 1
        root_child0_child1.flex_shrink = 1
        root_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child1.height = YGValuePoint(20)
        root.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

    def test_display_contents_with_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Left, 10)
        root_child0.set_margin(Edge.Top, 10)
        root_child0.set_margin(Edge.Right, 10)
        root_child0.set_margin(Edge.Bottom, 10)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root_child0.display = Display.Contents
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
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 100)

    def test_display_contents_with_padding(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_padding(Edge.Left, 10)
        root_child0.set_padding(Edge.Top, 10)
        root_child0.set_padding(Edge.Right, 10)
        root_child0.set_padding(Edge.Bottom, 10)
        root_child0.display = Display.Contents
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0.height = YGValuePoint(10)
        root.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 1
        root_child0_child1.flex_shrink = 1
        root_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child1.height = YGValuePoint(20)
        root.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

    def test_display_contents_with_position(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.set_position(Edge.Top, 10)
        root_child0.display = Display.Contents
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0.height = YGValuePoint(10)
        root.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 1
        root_child0_child1.flex_shrink = 1
        root_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child1.height = YGValuePoint(20)
        root.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

    def test_display_contents_with_position_absolute(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root_child0.display = Display.Contents
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0.height = YGValuePoint(10)
        root.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 1
        root_child0_child1.flex_shrink = 1
        root_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child1.height = YGValuePoint(20)
        root.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 20)

    def test_display_contents_nested(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.display = Display.Contents
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.display = Display.Contents
        root.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.flex_grow = 1
        root_child0_child0_child0.flex_shrink = 1
        root_child0_child0_child0.flex_basis = YGValuePercent(0)
        root_child0_child0_child0.height = YGValuePoint(10)
        root.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.flex_grow = 1
        root_child0_child0_child1.flex_shrink = 1
        root_child0_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child0_child1.height = YGValuePoint(20)
        root.insert_child(root_child0_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child0_child1.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 0)
        assert_float_approx(root_child0_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 10)

        assert_float_approx(root_child0_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child0_child1.layout_height, 20)

    def test_display_contents_with_siblings(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePercent(0)
        root_child0.height = YGValuePoint(30)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.display = Display.Contents
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.flex_grow = 1
        root_child1_child0.flex_shrink = 1
        root_child1_child0.flex_basis = YGValuePercent(0)
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = Node(config)
        root_child1_child1.flex_grow = 1
        root_child1_child1.flex_shrink = 1
        root_child1_child1.flex_basis = YGValuePercent(0)
        root_child1_child1.height = YGValuePoint(20)
        root_child1.insert_child(root_child1_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.flex_shrink = 1
        root_child2.flex_basis = YGValuePercent(0)
        root_child2.height = YGValuePoint(30)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child1_child0.layout_left, 25)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child1_child1.layout_left, 50)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 25)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 0)

        assert_float_approx(root_child1_child0.layout_left, 50)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 25)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child1_child1.layout_left, 25)
        assert_float_approx(root_child1_child1.layout_top, 0)
        assert_float_approx(root_child1_child1.layout_width, 25)
        assert_float_approx(root_child1_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 30)
