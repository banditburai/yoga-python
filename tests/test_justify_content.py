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


class TestJustifyContent:
    def test_justify_content_row_flex_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 92)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 82)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 72)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_row_flex_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 72)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 82)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 92)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 10)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_row_center(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 36)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 46)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 56)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 56)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 46)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 36)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_row_space_between(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceBetween
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 46)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 92)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 92)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 46)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_row_space_around(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceAround
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 12)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 46)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 46)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 12)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_column_flex_start(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 10)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 20)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_column_flex_end(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 72)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 82)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 92)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 72)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 82)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 92)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_column_center(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 36)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 56)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 36)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 56)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_column_space_between(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.SpaceBetween
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 92)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 92)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_column_space_around(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.SpaceAround
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 12)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 80)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 12)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 80)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_row_min_width_and_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Left, 100)
        root.min_width = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 15)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 15)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_justify_content_row_max_width_and_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Left, 100)
        root.width = YGValuePoint(100)
        root.max_width = YGValuePoint(80)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 100)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_justify_content_column_min_height_and_margin(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Top, 100)
        root.min_height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 100)
        assert_float_approx(root.layout_width, 20)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 100)
        assert_float_approx(root.layout_width, 20)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 15)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_justify_content_column_max_height_and_margin(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.set_margin(Edge.Top, 100)
        root.height = YGValuePoint(100)
        root.max_height = YGValuePoint(80)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 100)
        assert_float_approx(root.layout_width, 20)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 100)
        assert_float_approx(root.layout_width, 20)
        assert_float_approx(root.layout_height, 80)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 30)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 20)

    def test_justify_content_column_space_evenly(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 18)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 74)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 18)
        assert_float_approx(root_child0.layout_width, 102)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 46)
        assert_float_approx(root_child1.layout_width, 102)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 74)
        assert_float_approx(root_child2.layout_width, 102)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_row_space_evenly(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 26)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 51)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 77)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 0)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 77)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 51)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 0)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 26)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 0)
        assert_float_approx(root_child2.layout_height, 10)

    def test_justify_content_min_width_with_padding_child_width_greater_than_parent(self):
        config = Config()
        root = Node(config)
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(1000)
        root.height = YGValuePoint(1584)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.align_content = Align.Stretch
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.justify_content = Justify.Center
        root_child0_child0.align_content = Align.Stretch
        root_child0_child0.set_padding(Edge.Left, 100)
        root_child0_child0.set_padding(Edge.Right, 100)
        root_child0_child0.min_width = YGValuePoint(400)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0_child0.width = YGValuePoint(300)
        root_child0_child0_child0.height = YGValuePoint(100)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 1000)
        assert_float_approx(root.layout_height, 1584)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1000)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 500)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 300)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 1000)
        assert_float_approx(root.layout_height, 1584)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1000)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 500)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 500)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 100)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 300)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

    def test_justify_content_min_width_with_padding_child_width_lower_than_parent(self):
        config = Config()
        root = Node(config)
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(1080)
        root.height = YGValuePoint(1584)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.align_content = Align.Stretch
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.justify_content = Justify.Center
        root_child0_child0.align_content = Align.Stretch
        root_child0_child0.set_padding(Edge.Left, 100)
        root_child0_child0.set_padding(Edge.Right, 100)
        root_child0_child0.min_width = YGValuePoint(400)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0_child0.width = YGValuePoint(199)
        root_child0_child0_child0.height = YGValuePoint(100)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 1080)
        assert_float_approx(root.layout_height, 1584)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1080)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 400)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 101)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 199)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 1080)
        assert_float_approx(root.layout_height, 1584)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1080)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 680)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 400)
        assert_float_approx(root_child0_child0.layout_height, 100)

        assert_float_approx(root_child0_child0_child0.layout_left, 101)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 199)
        assert_float_approx(root_child0_child0_child0.layout_height, 100)

    def test_justify_content_space_between_indefinite_container_dim_with_free_space(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(300)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.justify_content = Justify.SpaceBetween
        root_child0.min_width = YGValuePoint(200)
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
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 150)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 300)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 150)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 50)

    def test_justify_content_flex_start_row_reverse(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_justify_content_flex_end_row_reverse(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 60)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 100)

    def test_justify_content_overflow_row_flex_start(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 62)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, -18)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_overflow_row_flex_end(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.FlexEnd
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, -18)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 62)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_overflow_row_center(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, -9)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 31)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 71)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 71)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 31)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, -9)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_overflow_row_space_between(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceBetween
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 62)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, -18)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_overflow_row_space_around(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceAround
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 62)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, -18)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_overflow_row_space_evenly(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 62)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, -18)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    def test_justify_content_overflow_row_space_evenly_auto_margin(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.justify_content = Justify.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.set_margin(Edge.Right, 0)
        root_child0.set_margin_auto(Edge.Right)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 80)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 62)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, -18)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_justify_content_overflow_row_reverse_space_around(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.justify_content = Justify.SpaceAround
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, -18)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 62)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_justify_content_overflow_row_reverse_space_evenly(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.RowReverse
        root.justify_content = Justify.SpaceEvenly
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(102)
        root.height = YGValuePoint(102)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(40)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(40)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(40)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 102)
        assert_float_approx(root.layout_height, 102)

        assert_float_approx(root_child0.layout_left, -18)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 40)
        assert_float_approx(root_child0.layout_height, 102)

        assert_float_approx(root_child1.layout_left, 22)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 102)

        assert_float_approx(root_child2.layout_left, 62)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 40)
        assert_float_approx(root_child2.layout_height, 102)
