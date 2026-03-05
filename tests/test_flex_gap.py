import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Gutter,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestFlexGap:
    def test_gap_negative_value(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.set_gap(Gutter.All, -20)
        root.height = 200

        root_child0 = Node(config)
        root_child0.width = 20
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = 20
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = 20
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.width = 20
        root.insert_child(root_child3, 3)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 20)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 200)

        assert_float_approx(root_child2.layout_left, 40)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 200)

        assert_float_approx(root_child3.layout_left, 60)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 80)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 20)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 20)
        assert_float_approx(root_child1.layout_height, 200)

        assert_float_approx(root_child2.layout_left, 20)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 20)
        assert_float_approx(root_child2.layout_height, 200)

        assert_float_approx(root_child3.layout_left, 0)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 20)
        assert_float_approx(root_child3.layout_height, 200)
