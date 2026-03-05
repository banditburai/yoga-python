import pytest
from yoga import (
    Node,
    Config,
    Direction,
    YGValuePercent,
    YGValuePoint,
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestComputedMargin:
    def test_computed_layout_margin(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)
        root.set_margin_percent(Edge.Start, 10)

        root.calculate_layout(100, 100, Direction.LTR)

        assert_float_approx(root.layout_margin(Edge.Left), 10)
        assert_float_approx(root.layout_margin(Edge.Right), 0)

        root.calculate_layout(100, 100, Direction.RTL)

        assert_float_approx(root.layout_margin(Edge.Left), 0)
        assert_float_approx(root.layout_margin(Edge.Right), 10)

    def test_margin_side_overrides_horizontal_and_vertical(self):
        edges = [
            Edge.Top,
            Edge.Bottom,
            Edge.Start,
            Edge.End,
            Edge.Left,
            Edge.Right,
        ]

        for edge_value in range(2):
            for edge in edges:
                horizontal_or_vertical = (
                    Edge.Vertical if edge in (Edge.Top, Edge.Bottom) else Edge.Horizontal
                )

                config = Config()
                root = Node(config)
                root.width = YGValuePoint(100)
                root.height = YGValuePoint(100)
                root.set_margin(horizontal_or_vertical, 10)
                root.set_margin(edge, edge_value)

                root.calculate_layout(100, 100, Direction.LTR)

                assert_float_approx(root.layout_margin(edge), edge_value)

    def test_margin_side_overrides_all(self):
        edges = [
            Edge.Top,
            Edge.Bottom,
            Edge.Start,
            Edge.End,
            Edge.Left,
            Edge.Right,
        ]

        for edge_value in range(2):
            for edge in edges:
                config = Config()
                root = Node(config)
                root.width = YGValuePoint(100)
                root.height = YGValuePoint(100)
                root.set_margin(Edge.All, 10)
                root.set_margin(edge, edge_value)

                root.calculate_layout(100, 100, Direction.LTR)

                assert_float_approx(root.layout_margin(edge), edge_value)

    def test_margin_horizontal_and_vertical_overrides_all(self):
        directions = [Edge.Horizontal, Edge.Vertical]

        for direction_value in range(2):
            for direction in directions:
                config = Config()
                root = Node(config)
                root.width = YGValuePoint(100)
                root.height = YGValuePoint(100)
                root.set_margin(Edge.All, 10)
                root.set_margin(direction, direction_value)

                root.calculate_layout(100, 100, Direction.LTR)

                if direction == Edge.Vertical:
                    assert_float_approx(root.layout_margin(Edge.Top), direction_value)
                    assert_float_approx(root.layout_margin(Edge.Bottom), direction_value)
                else:
                    assert_float_approx(root.layout_margin(Edge.Start), direction_value)
                    assert_float_approx(root.layout_margin(Edge.End), direction_value)
                    assert_float_approx(root.layout_margin(Edge.Left), direction_value)
                    assert_float_approx(root.layout_margin(Edge.Right), direction_value)
