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
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestDisplayContents:
    def test_test1(self):
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
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 1
        root_child0_child1.flex_shrink = 1
        root_child0_child1.flex_basis = YGValuePercent(0)
        root_child0_child1.height = YGValuePoint(20)
        root_child0.insert_child(root_child0_child1, 1)

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
