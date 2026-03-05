import pytest
from yoga import Config, Node, Direction, FlexDirection, Wrap, Edge


class TestYGHadOverflow:
    def test_children_overflow_no_wrap_and_no_flex_children(self):
        config = Config()
        root = Node(config)
        root.width = 200
        root.height = 100
        root.flex_direction = FlexDirection.Column
        root.flex_wrap = Wrap.NoWrap

        child0 = Node(config)
        child0.width = 80
        child0.height = 40
        child0.set_margin(Edge.Top, 10)
        child0.set_margin(Edge.Bottom, 15)
        root.insert_child(child0, 0)

        child1 = Node(config)
        child1.width = 80
        child1.height = 40
        child1.set_margin(Edge.Bottom, 5)
        root.insert_child(child1, 1)

        root.calculate_layout(200, 100, Direction.LTR)

        assert root.layout_had_overflow is True

    def test_spacing_overflow_no_wrap_and_no_flex_children(self):
        config = Config()
        root = Node(config)
        root.width = 200
        root.height = 100
        root.flex_direction = FlexDirection.Column
        root.flex_wrap = Wrap.NoWrap

        child0 = Node(config)
        child0.width = 80
        child0.height = 40
        child0.set_margin(Edge.Top, 10)
        child0.set_margin(Edge.Bottom, 10)
        root.insert_child(child0, 0)

        child1 = Node(config)
        child1.width = 80
        child1.height = 40
        child1.set_margin(Edge.Bottom, 5)
        root.insert_child(child1, 1)

        root.calculate_layout(200, 100, Direction.LTR)

        assert root.layout_had_overflow is True

    def test_no_overflow_no_wrap_and_flex_children(self):
        config = Config()
        root = Node(config)
        root.width = 200
        root.height = 100
        root.flex_direction = FlexDirection.Column
        root.flex_wrap = Wrap.NoWrap

        child0 = Node(config)
        child0.width = 80
        child0.height = 40
        child0.set_margin(Edge.Top, 10)
        child0.set_margin(Edge.Bottom, 10)
        root.insert_child(child0, 0)

        child1 = Node(config)
        child1.width = 80
        child1.height = 40
        child1.set_margin(Edge.Bottom, 5)
        child1.flex_shrink = 1
        root.insert_child(child1, 1)

        root.calculate_layout(200, 100, Direction.LTR)

        assert root.layout_had_overflow is False

    def test_hadOverflow_gets_reset_if_not_logger_valid(self):
        config = Config()
        root = Node(config)
        root.width = 200
        root.height = 100
        root.flex_direction = FlexDirection.Column
        root.flex_wrap = Wrap.NoWrap

        child0 = Node(config)
        child0.width = 80
        child0.height = 40
        child0.set_margin(Edge.Top, 10)
        child0.set_margin(Edge.Bottom, 10)
        root.insert_child(child0, 0)

        child1 = Node(config)
        child1.width = 80
        child1.height = 40
        child1.set_margin(Edge.Bottom, 5)
        root.insert_child(child1, 1)

        root.calculate_layout(200, 100, Direction.LTR)
        assert root.layout_had_overflow is True

        child1.flex_shrink = 1

        root.calculate_layout(200, 100, Direction.LTR)
        assert root.layout_had_overflow is False

    def test_spacing_overflow_in_nested_nodes(self):
        config = Config()
        root = Node(config)
        root.width = 200
        root.height = 100
        root.flex_direction = FlexDirection.Column
        root.flex_wrap = Wrap.NoWrap

        child0 = Node(config)
        child0.width = 80
        child0.height = 40
        child0.set_margin(Edge.Top, 10)
        child0.set_margin(Edge.Bottom, 10)
        root.insert_child(child0, 0)

        child1 = Node(config)
        child1.width = 80
        child1.height = 40
        root.insert_child(child1, 1)

        child1_1 = Node(config)
        child1_1.width = 80
        child1_1.height = 40
        child1_1.set_margin(Edge.Bottom, 5)
        child1.insert_child(child1_1, 0)

        root.calculate_layout(200, 100, Direction.LTR)

        assert root.layout_had_overflow is True
