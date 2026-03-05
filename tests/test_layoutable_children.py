import pytest
from yoga import (
    Node,
    Config,
    Direction,
    Display,
)


class TestLayoutableChildren:
    def test_layoutable_children_single_contents_node(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child1 = Node(config)
        root_child2 = Node(config)

        root_grandchild0 = Node(config)
        root_grandchild1 = Node(config)

        root.insert_child(root_child0, 0)
        root.insert_child(root_child1, 1)
        root.insert_child(root_child2, 2)

        root_child1.insert_child(root_grandchild0, 0)
        root_child1.insert_child(root_grandchild1, 1)

        root_child1.display = Display.Contents

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        layout_children = root.get_layout_children()
        expected = [root_child0, root_grandchild0, root_grandchild1, root_child2]

        assert len(layout_children) == len(expected)
        for actual, exp in zip(layout_children, expected):
            assert actual is exp

        root.free_recursive()

    def test_layoutable_children_multiple_contents_nodes(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child1 = Node(config)
        root_child2 = Node(config)

        root_grandchild0 = Node(config)
        root_grandchild1 = Node(config)
        root_grandchild2 = Node(config)
        root_grandchild3 = Node(config)
        root_grandchild4 = Node(config)
        root_grandchild5 = Node(config)

        root.insert_child(root_child0, 0)
        root.insert_child(root_child1, 1)
        root.insert_child(root_child2, 2)

        root_child0.insert_child(root_grandchild0, 0)
        root_child0.insert_child(root_grandchild1, 1)
        root_child1.insert_child(root_grandchild2, 0)
        root_child1.insert_child(root_grandchild3, 1)
        root_child2.insert_child(root_grandchild4, 0)
        root_child2.insert_child(root_grandchild5, 1)

        root_child0.display = Display.Contents
        root_child1.display = Display.Contents
        root_child2.display = Display.Contents

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        layout_children = root.get_layout_children()
        expected = [
            root_grandchild0,
            root_grandchild1,
            root_grandchild2,
            root_grandchild3,
            root_grandchild4,
            root_grandchild5,
        ]

        assert len(layout_children) == len(expected)
        for actual, exp in zip(layout_children, expected):
            assert actual is exp

        root.free_recursive()

    def test_layoutable_children_nested_contents_nodes(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child1 = Node(config)
        root_child2 = Node(config)

        root_grandchild0 = Node(config)
        root_grandchild1 = Node(config)

        root_great_grandchild0 = Node(config)
        root_great_grandchild1 = Node(config)

        root.insert_child(root_child0, 0)
        root.insert_child(root_child1, 1)
        root.insert_child(root_child2, 2)

        root_child1.insert_child(root_grandchild0, 0)
        root_child1.insert_child(root_grandchild1, 1)

        root_grandchild1.insert_child(root_great_grandchild0, 0)
        root_grandchild1.insert_child(root_great_grandchild1, 1)

        root_child1.display = Display.Contents
        root_grandchild1.display = Display.Contents

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        layout_children = root.get_layout_children()
        expected = [
            root_child0,
            root_grandchild0,
            root_great_grandchild0,
            root_great_grandchild1,
            root_child2,
        ]

        assert len(layout_children) == len(expected)
        for actual, exp in zip(layout_children, expected):
            assert actual is exp

        root.free_recursive()

    def test_layoutable_children_contents_leaf_node(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child1 = Node(config)
        root_child2 = Node(config)

        root.insert_child(root_child0, 0)
        root.insert_child(root_child1, 1)
        root.insert_child(root_child2, 2)

        root_child1.display = Display.Contents

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        layout_children = root.get_layout_children()
        expected = [root_child0, root_child2]

        assert len(layout_children) == len(expected)
        for actual, exp in zip(layout_children, expected):
            assert actual is exp

        root.free_recursive()

    def test_layoutable_children_contents_root_node(self):
        config = Config()
        root = Node(config)

        root_child0 = Node(config)
        root_child1 = Node(config)
        root_child2 = Node(config)

        root.insert_child(root_child0, 0)
        root.insert_child(root_child1, 1)
        root.insert_child(root_child2, 2)

        root.display = Display.Contents

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        layout_children = root.get_layout_children()
        expected = [root_child0, root_child1, root_child2]

        assert len(layout_children) == len(expected)
        for actual, exp in zip(layout_children, expected):
            assert actual is exp

        root.free_recursive()
