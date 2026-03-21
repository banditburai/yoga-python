import pytest
from yoga import Node, Config


def get_children(node):
    children = []
    for i in range(node.child_count):
        children.append(node[i])
    return children


class TestTreeMutation:
    def test_set_children_adds_children_to_parent(self):
        config = Config()
        root = Node(config)
        root_child0 = Node(config)
        root_child1 = Node(config)

        root.set_children([root_child0, root_child1])

        expected_children = [root_child0, root_child1]
        assert get_children(root) == expected_children

        owners = [root_child0.owner, root_child1.owner]
        expected_owners = [root, root]
        assert owners == expected_owners

        root.free_recursive()

    def test_set_children_to_empty_removes_old_children(self):
        config = Config()
        root = Node(config)
        root_child0 = Node(config)
        root_child1 = Node(config)

        root.set_children([root_child0, root_child1])
        root.set_children([])

        expected_children = []
        assert get_children(root) == expected_children

        owners = [root_child0.owner, root_child1.owner]
        expected_owners = [None, None]
        assert owners == expected_owners

        root.free_recursive()

    def test_set_children_replaces_non_common_children(self):
        config = Config()
        root = Node(config)
        root_child0 = Node(config)
        root_child1 = Node(config)

        root.set_children([root_child0, root_child1])

        root_child2 = Node(config)
        root_child3 = Node(config)

        root.set_children([root_child2, root_child3])

        expected_children = [root_child2, root_child3]
        assert get_children(root) == expected_children

        owners = [root_child0.owner, root_child1.owner]
        expected_owners = [None, None]
        assert owners == expected_owners

        root.free_recursive()
        root_child0.free()
        root_child1.free()

    def test_set_children_keeps_and_reorders_common_children(self):
        config = Config()
        root = Node(config)
        root_child0 = Node(config)
        root_child1 = Node(config)
        root_child2 = Node(config)

        root.set_children([root_child0, root_child1, root_child2])

        root_child3 = Node(config)

        root.set_children([root_child2, root_child1, root_child3])

        expected_children = [root_child2, root_child1, root_child3]
        assert get_children(root) == expected_children

        owners = [root_child0.owner, root_child1.owner, root_child2.owner, root_child3.owner]
        expected_owners = [None, root, root, root]
        assert owners == expected_owners

        root.free_recursive()
        root_child0.free()

    def test_set_children_same_order_is_noop(self):
        config = Config()
        root = Node(config)
        root_child0 = Node(config)
        root_child1 = Node(config)

        root.set_children([root_child0, root_child1])
        root.set_children([root_child0, root_child1])

        assert get_children(root) == [root_child0, root_child1]
        assert root_child0.owner is root
        assert root_child1.owner is root

        root.free_recursive()
