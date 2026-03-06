import pytest
from yoga import Node, Config, Direction, FlexDirection, Display, Edge


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"



class TestZeroOutLayout:
    def test_zero_out_layout(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.width = 200
        root.height = 200

        child = Node(config)
        child.width = 100
        child.height = 100
        child.set_margin(Edge.Top, 10)
        child.set_padding(Edge.Top, 10)
        root.insert_child(child, 0)

        root.calculate_layout(100, 100, Direction.LTR)

        assert_float_approx(child.layout_margin(Edge.Top), 10)
        assert_float_approx(child.layout_padding(Edge.Top), 10)

        child.display = Display.None_

        root.calculate_layout(100, 100, Direction.LTR)

        assert_float_approx(child.layout_margin(Edge.Top), 0)
        assert_float_approx(child.layout_padding(Edge.Top), 0)

        root.free_recursive()
