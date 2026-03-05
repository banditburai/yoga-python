import pytest
from yoga import (
    Node,
    Config,
    Direction,
    Align,
    YGValuePoint,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestDirtied:
    def test_dirtied(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        dirtied_count = [0]

        def dirtied():
            dirtied_count[0] += 1

        root.set_dirtied_func(dirtied)

        assert dirtied_count[0] == 0

        root.set_dirty(True)
        assert dirtied_count[0] == 1

        root.set_dirty(True)
        assert dirtied_count[0] == 1

    def test_dirtied_propagation(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        dirtied_count = [0]

        def dirtied():
            dirtied_count[0] += 1

        root.set_dirtied_func(dirtied)

        assert dirtied_count[0] == 0

        root_child0.mark_dirty_and_propagate()
        assert dirtied_count[0] == 1

        root_child0.mark_dirty_and_propagate()
        assert dirtied_count[0] == 1

    def test_dirtied_hierarchy(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        dirtied_count = [0]

        def dirtied():
            dirtied_count[0] += 1

        root_child0.set_dirtied_func(dirtied)

        assert dirtied_count[0] == 0

        root.mark_dirty_and_propagate()
        assert dirtied_count[0] == 0

        root_child1.mark_dirty_and_propagate()
        assert dirtied_count[0] == 0

        root_child0.mark_dirty_and_propagate()
        assert dirtied_count[0] == 1
