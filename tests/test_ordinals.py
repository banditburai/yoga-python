import pytest
from yoga import Edge


def test_ordinals_iteration():
    expected_edges = [
        Edge.Left,
        Edge.Top,
        Edge.Right,
        Edge.Bottom,
        Edge.Start,
        Edge.End,
        Edge.Horizontal,
        Edge.Vertical,
        Edge.All,
    ]

    edges = list(Edge.__members__.values())
    assert edges == expected_edges
    assert len(edges) == 9
