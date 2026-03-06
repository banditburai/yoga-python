import pytest
from yoga import (
    Node,
    Config,
    Direction,
    PositionType,
    YGValuePoint,
    YGValuePercent,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


def recursively_assert_proper_node_ownership(node):
    for i in range(node.child_count):
        child = node[i]
        assert node is child.owner, "Node owner mismatch"
        recursively_assert_proper_node_ownership(child)


class TestCloneNode:
    def test_free_root_only(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePercent(1)
        root_child0_child0.height = YGValuePoint(1)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        cloned_root = root.clone()
        cloned_root.width = YGValuePoint(110)
        cloned_root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        # Only free root, not cloned
        root.free_recursive()

    def test_free_clone_only(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePercent(1)
        root_child0_child0.height = YGValuePoint(1)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        cloned_root = root.clone()
        cloned_root.width = YGValuePoint(110)
        cloned_root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        # Only free clone, not root
        cloned_root.free_recursive()

    def test_free_both_order1(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePercent(1)
        root_child0_child0.height = YGValuePoint(1)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        cloned_root = root.clone()
        cloned_root.width = YGValuePoint(110)
        cloned_root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        # Free root first
        root.free_recursive()
        # Then clone
        cloned_root.free_recursive()

    def test_free_both_order2(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Static
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Absolute
        root_child0_child0.width = YGValuePercent(1)
        root_child0_child0.height = YGValuePoint(1)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        cloned_root = root.clone()
        cloned_root.width = YGValuePoint(110)
        cloned_root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        # Free clone first
        cloned_root.free_recursive()
        # Then root
        root.free_recursive()
