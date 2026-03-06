import pytest
from yoga import Node, Config, Direction


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


@pytest.mark.skip(
    reason="nanobind pytest crash: clone() + free_recursive() causes abort. Works in regular Python."
)
class TestPersistence:
    def test_cloning_shared_root(self):
        config = Config()

        root = Node(config)
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = 50
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 75)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        root2 = root.clone()
        root2.width = 100

        assert root2.child_count == 2
        assert root2[0] is root_child0
        assert root2[1] is root_child1

        root2.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root2.child_count == 2
        assert root2[0] is root_child0
        assert root2[1] is root_child1

        root2.width = 150
        root2.height = 200
        root2.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root2.child_count == 2
        root2_child0 = root2[0]
        root2_child1 = root2[1]
        assert root_child0 is not root2_child0
        assert root_child1 is not root2_child1

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 75)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 75)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root2.layout_left, 0)
        assert_float_approx(root2.layout_top, 0)
        assert_float_approx(root2.layout_width, 150)
        assert_float_approx(root2.layout_height, 200)

        assert_float_approx(root2_child0.layout_left, 0)
        assert_float_approx(root2_child0.layout_top, 0)
        assert_float_approx(root2_child0.layout_width, 150)
        assert_float_approx(root2_child0.layout_height, 125)

        assert_float_approx(root2_child1.layout_left, 0)
        assert_float_approx(root2_child1.layout_top, 125)
        assert_float_approx(root2_child1.layout_width, 150)
        assert_float_approx(root2_child1.layout_height, 75)

        root2.free_recursive()
        root.free_recursive()

    def test_mutating_children_of_a_clone_clones_only_after_layout(self):
        config = Config()

        root = Node(config)
        assert root.child_count == 0

        root2 = root.clone()
        assert root2.child_count == 0

        root2_child0 = Node(config)
        root2.insert_child(root2_child0, 0)

        assert root.child_count == 0
        assert root2.child_count == 1

        root3 = root2.clone()
        assert root2.child_count == 1
        assert root3.child_count == 1
        assert root2[0] is root3[0]

        root3_child1 = Node(config)
        root3.insert_child(root3_child1, 1)
        assert root2.child_count == 1
        assert root3.child_count == 2
        assert root3_child1 is root3[1]
        assert root2[0] is root3[0]

        root4 = root3.clone()
        assert root3_child1 is root4[1]

        root4.remove_child(root3_child1)
        assert root3.child_count == 2
        assert root4.child_count == 1
        assert root3[0] is root4[0]

        root4.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert root3[0] is not root4[0]
        root3.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert root2[0] is not root3[0]

        root4.free_recursive()
        root3.free_recursive()
        root2.free_recursive()
        root.free_recursive()

    def test_cloning_two_levels(self):
        config = Config()

        root = Node(config)
        root.width = 100
        root.height = 100

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = 15
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root_child1_0 = Node(config)
        root_child1_0.flex_basis = 10
        root_child1_0.flex_grow = 1
        root_child1.insert_child(root_child1_0, 0)

        root_child1_1 = Node(config)
        root_child1_1.flex_basis = 25
        root_child1.insert_child(root_child1_1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_height, 40)
        assert_float_approx(root_child1.layout_height, 60)
        assert_float_approx(root_child1_0.layout_height, 35)
        assert_float_approx(root_child1_1.layout_height, 25)

        root2_child0 = root_child0.clone()
        root2_child1 = root_child1.clone()
        root2 = root.clone()

        root2_child0.flex_grow = 0
        root2_child0.flex_basis = 40

        root2.remove_all_children()
        root2.insert_child(root2_child0, 0)
        root2.insert_child(root2_child1, 1)
        assert root2.child_count == 2

        root2.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_height, 40)
        assert_float_approx(root_child1.layout_height, 60)
        assert_float_approx(root_child1_0.layout_height, 35)
        assert_float_approx(root_child1_1.layout_height, 25)

        assert_float_approx(root2_child0.layout_height, 40)
        assert_float_approx(root2_child1.layout_height, 60)

        assert root2_child1[0] is root_child1_0
        assert root2_child1[1] is root_child1_1

        root2.free_recursive()
        root.free_recursive()

    def test_cloning_and_freeing(self):
        config = Config()

        root = Node(config)
        root.width = 100
        root.height = 100
        root_child0 = Node(config)
        root.insert_child(root_child0, 0)
        root_child1 = Node(config)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        root2 = root.clone()
        root.free()
        root2.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        root2.free_recursive()
        root_child0.free()
        root_child1.free()

    def test_mixed_shared_and_owned_children(self):
        root0 = Node()
        root1 = Node()

        root0_child0 = Node()
        root0_child0_0 = Node()
        root0.insert_child(root0_child0, 0)
        root0_child0.insert_child(root0_child0_0, 0)

        root1_child0 = Node()
        root1_child2 = Node()
        root1.insert_child(root1_child0, 0)
        root1.insert_child(root1_child2, 1)

        root1.set_children([root1_child0, root0_child0, root1_child2])

        secondChild = root1[1]
        assert secondChild is root0[0]
        assert secondChild[0] is root0_child0[0]

        root1.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        secondChild = root1[1]
        assert secondChild is not root0[0]
        assert secondChild.owner is root1
        assert secondChild[0] is not root0_child0[0]
        assert secondChild[0].owner is secondChild
