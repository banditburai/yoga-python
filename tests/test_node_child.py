import pytest
from yoga import Node, Direction


class TestYGNodeChild:
    def test_reset_layout_when_child_removed(self):
        root = Node()

        root_child0 = Node()
        root_child0.width = 100
        root_child0.height = 100
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 100
        assert root_child0.layout_height == 100

        root.remove_child(root_child0)

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width is None or root_child0.layout_width != 100
        assert root_child0.layout_height is None or root_child0.layout_height != 100

    def test_removed_child_can_be_reused_with_valid_layout(self):
        root = Node()
        root.width = 200
        root.height = 200

        child = Node()
        child.width = 100
        child.height = 100
        root.insert_child(child, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert child.layout_width == 100
        assert child.layout_height == 100

        root.remove_child(child)

        assert child.layout_width is None or child.layout_width != 100
        assert child.layout_height is None or child.layout_height != 100
        assert child.is_dirty is True

        root.insert_child(child, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert child.layout_width == 100
        assert child.layout_height == 100
        assert child.is_dirty is False
