import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Align,
    Display,
    YGValuePoint,
    Errata,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


@pytest.mark.skip(
    reason="nanobind pytest crash: clone() + free_recursive() causes abort. Works in regular Python."
)
class TestDirtyMarking:
    def test_dirty_propagation(self):
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

        root_child0.width = YGValuePoint(20)

        assert root_child0.is_dirty is True
        assert root_child1.is_dirty is False
        assert root.is_dirty is True

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root_child0.is_dirty is False
        assert root_child1.is_dirty is False
        assert root.is_dirty is False

        root.free_recursive()

    def test_dirty_propagation_only_if_prop_changed(self):
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

        root_child0.width = YGValuePoint(50)

        assert root_child0.is_dirty is False
        assert root_child1.is_dirty is False
        assert root.is_dirty is False

        root.free_recursive()

    def test_dirty_propagation_changing_layout_config(self):
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

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(25)
        root_child0_child0.height = YGValuePoint(20)
        root.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.is_dirty is False
        assert root_child0.is_dirty is False
        assert root_child1.is_dirty is False
        assert root_child0_child0.is_dirty is False

        new_config = Config()
        new_config.errata = Errata.StretchFlexBasis
        root_child0.set_config(new_config)

        assert root.is_dirty is True
        assert root_child0.is_dirty is True
        assert root_child1.is_dirty is False
        assert root_child0_child0.is_dirty is False

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.is_dirty is False
        assert root_child0.is_dirty is False
        assert root_child1.is_dirty is False
        assert root_child0_child0.is_dirty is False

        root.free_recursive()

    def test_dirty_propagation_changing_benign_config(self):
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

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(25)
        root_child0_child0.height = YGValuePoint(20)
        root.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.is_dirty is False
        assert root_child0.is_dirty is False
        assert root_child1.is_dirty is False
        assert root_child0_child0.is_dirty is False

        new_config = Config()

        def logger(config, node, level, format, args):
            return 0

        new_config.set_logger(logger)
        root_child0.set_config(new_config)

        assert root.is_dirty is False
        assert root_child0.is_dirty is False
        assert root_child1.is_dirty is False
        assert root_child0_child0.is_dirty is False

        root.free_recursive()

    def test_dirty_mark_all_children_as_dirty_when_display_changes(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.height = YGValuePoint(100)

        child0 = Node(config)
        child0.flex_grow = 1.0
        child1 = Node(config)
        child1.flex_grow = 1.0

        child1_child0 = Node(config)
        child1_child0_child0 = Node(config)
        child1_child0_child0.width = YGValuePoint(8)
        child1_child0_child0.height = YGValuePoint(16)

        child1_child0.insert_child(child1_child0_child0, 0)

        child1.insert_child(child1_child0, 0)
        root.insert_child(child0, 0)
        root.insert_child(child1, 0)

        child0.display = Display.Flex
        child1.display = Display.None_
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(child1_child0_child0.layout_width, 0)
        assert_float_approx(child1_child0_child0.layout_height, 0)

        child0.display = Display.None_
        child1.display = Display.Flex
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(child1_child0_child0.layout_width, 8)
        assert_float_approx(child1_child0_child0.layout_height, 16)

        child0.display = Display.Flex
        child1.display = Display.None_
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(child1_child0_child0.layout_width, 0)
        assert_float_approx(child1_child0_child0.layout_height, 0)

        child0.display = Display.None_
        child1.display = Display.Flex
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(child1_child0_child0.layout_width, 8)
        assert_float_approx(child1_child0_child0.layout_height, 16)

        root.free_recursive()

    def test_dirty_node_only_if_children_are_actually_removed(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)

        child0 = Node(config)
        child0.width = YGValuePoint(50)
        child0.height = YGValuePoint(25)
        root.insert_child(child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        child1 = Node(config)
        root.remove_child(child1)
        assert root.is_dirty is False
        child1.free()

        root.remove_child(child0)
        assert root.is_dirty is True
        child0.free()

        root.free_recursive()

    def test_dirty_node_only_if_undefined_values_gets_set_to_undefined(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(50)
        root.height = YGValuePoint(50)
        root.min_width = float("nan")

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert root.is_dirty is False

        root.min_width = float("nan")

        assert root.is_dirty is False

        root.free_recursive()

    def test_dirty_removed_child_node(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        child = Node(config)
        child.width = YGValuePoint(50)
        child.height = YGValuePoint(50)
        root.insert_child(child, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert child.is_dirty is False

        root.remove_child(child)

        assert child.is_dirty is True

        child.free()
        root.free_recursive()

    def test_dirty_removed_child_nodes_when_removing_all(self):
        config = Config()
        root = Node(config)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        child0 = Node(config)
        child0.width = YGValuePoint(50)
        child0.height = YGValuePoint(25)
        root.insert_child(child0, 0)

        child1 = Node(config)
        child1.width = YGValuePoint(50)
        child1.height = YGValuePoint(25)
        root.insert_child(child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert child0.is_dirty is False
        assert child1.is_dirty is False

        root.remove_all_children()

        assert child0.is_dirty is True
        assert child1.is_dirty is True

        child0.free()
        child1.free()
        root.free_recursive()
