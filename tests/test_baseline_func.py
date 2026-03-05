import pytest
from yoga import Node, Config, Direction, FlexDirection, Align


def test_align_baseline_customer_func():
    config = Config()

    baseline_value = 10.0

    def _baseline(node, width, height):
        return baseline_value

    root = Node(config)
    root.flex_direction = FlexDirection.Row
    root.align_items = Align.Baseline
    root.width = 100
    root.height = 100

    root_child0 = Node(config)
    root_child0.width = 50
    root_child0.height = 50
    root.insert_child(root_child0, 0)

    root_child1 = Node(config)
    root_child1.width = 50
    root_child1.height = 20
    root.insert_child(root_child1, 1)

    root_child1_child0 = Node(config)
    root_child1_child0.width = 50
    root_child1_child0.height = 20
    root_child1_child0.set_baseline_func(_baseline)
    root_child1.insert_child(root_child1_child0, 0)

    root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

    assert root.layout_left == 0
    assert root.layout_top == 0
    assert root.layout_width == 100
    assert root.layout_height == 100

    assert root_child0.layout_left == 0
    assert root_child0.layout_top == 0
    assert root_child0.layout_width == 50
    assert root_child0.layout_height == 50

    assert root_child1.layout_left == 50
    assert root_child1.layout_top == 40
    assert root_child1.layout_width == 50
    assert root_child1.layout_height == 20

    assert root_child1_child0.layout_left == 0
    assert root_child1_child0.layout_top == 0
    assert root_child1_child0.layout_width == 50
    assert root_child1_child0.layout_height == 20
