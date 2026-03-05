import pytest
from yoga import (
    Node,
    Direction,
    FlexDirection,
    Unit,
    YGValuePoint,
)


class TestCopyStyle:
    def test_copy_style_same(self):
        """Copy style between two default nodes."""
        node0 = Node()
        node1 = Node()
        node0.copy_style(node1)

    def test_copy_style_modified(self):
        """Copy style from a modified node."""
        node0 = Node()
        assert node0.flex_direction == FlexDirection.Column
        assert node0.max_height.unit == Unit.Undefined

        node1 = Node()
        node1.flex_direction = FlexDirection.Row
        node1.max_height = YGValuePoint(10)

        node0.copy_style(node1)
        assert node0.flex_direction == FlexDirection.Row
        assert node0.max_height.value == 10

    def test_copy_style_modified_same(self):
        """Copy same style doesn't re-dirty."""
        node0 = Node()
        node0.flex_direction = FlexDirection.Row
        node0.max_height = YGValuePoint(10)
        node0.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        node1 = Node()
        node1.flex_direction = FlexDirection.Row
        node1.max_height = YGValuePoint(10)

        node0.copy_style(node1)
