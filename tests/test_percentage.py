import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    PositionType,
    Wrap,
    Justify,
    Align,
    YGValuePoint,
    YGValuePercent,
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestPercentage:
    def test_percentage_width_height(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(30)
        root_child0.height = YGValuePercent(30)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 60)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 140)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 60)

    def test_percentage_position_left_top(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(400)
        root.height = YGValuePoint(400)

        root_child0 = Node(config)
        root_child0.set_position(Edge.Left, YGValuePercent(10))
        root_child0.set_position(Edge.Top, YGValuePercent(20))
        root_child0.width = YGValuePercent(45)
        root_child0.height = YGValuePercent(55)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 40)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 180)
        assert_float_approx(root_child0.layout_height, 220)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 400)
        assert_float_approx(root.layout_height, 400)

        assert_float_approx(root_child0.layout_left, 260)
        assert_float_approx(root_child0.layout_top, 80)
        assert_float_approx(root_child0.layout_width, 180)
        assert_float_approx(root_child0.layout_height, 220)

    def test_percentage_position_bottom_right(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.set_position(Edge.Right, YGValuePercent(20))
        root_child0.set_position(Edge.Bottom, YGValuePercent(10))
        root_child0.width = YGValuePercent(55)
        root_child0.height = YGValuePercent(15)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, -100)
        assert_float_approx(root_child0.layout_top, -50)
        assert_float_approx(root_child0.layout_width, 275)
        assert_float_approx(root_child0.layout_height, 75)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 125)
        assert_float_approx(root_child0.layout_top, -50)
        assert_float_approx(root_child0.layout_width, 275)
        assert_float_approx(root_child0.layout_height, 75)

    def test_percentage_flex_basis(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_basis = YGValuePercent(25)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 125)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 125)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 75)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 75)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 125)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 75)
        assert_float_approx(root_child1.layout_height, 200)

    def test_percentage_flex_basis_cross(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.flex_basis = YGValuePercent(25)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 125)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 125)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 75)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 125)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 125)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 75)

    def test_percentage_flex_basis_main_max_height(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(10)
        root_child0.max_height = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(10)
        root_child1.max_height = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 52)
        assert_float_approx(root_child0.layout_height, 120)

        assert_float_approx(root_child1.layout_left, 52)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 148)
        assert_float_approx(root_child1.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 148)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 52)
        assert_float_approx(root_child0.layout_height, 120)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 148)
        assert_float_approx(root_child1.layout_height, 40)

    def test_percentage_flex_basis_cross_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(10)
        root_child0.max_height = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(10)
        root_child1.max_height = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 120)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 120)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 40)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 120)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 120)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 40)

    def test_percentage_flex_basis_main_max_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(15)
        root_child0.max_width = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(10)
        root_child1.max_width = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 120)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 120)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 120)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 40)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 200)

    def test_percentage_flex_basis_cross_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(10)
        root_child0.max_width = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(15)
        root_child1.max_width = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 120)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 150)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 120)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 160)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 40)
        assert_float_approx(root_child1.layout_height, 150)

    def test_percentage_flex_basis_main_min_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(15)
        root_child0.min_width = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(10)
        root_child1.min_width = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 120)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 120)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 80)
        assert_float_approx(root_child1.layout_height, 200)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 80)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 120)
        assert_float_approx(root_child0.layout_height, 200)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 80)
        assert_float_approx(root_child1.layout_height, 200)

    def test_percentage_flex_basis_cross_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(10)
        root_child0.min_width = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(15)
        root_child1.min_width = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 150)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 150)

    def test_percentage_multiple_nested_with_padding_margin_and_percentage_values(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePercent(10)
        root_child0.set_margin(Edge.Left, 5)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 5)
        root_child0.set_margin(Edge.Bottom, 5)
        root_child0.set_padding(Edge.Left, 3)
        root_child0.set_padding(Edge.Top, 3)
        root_child0.set_padding(Edge.Right, 3)
        root_child0.set_padding(Edge.Bottom, 3)
        root_child0.min_width = YGValuePercent(60)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.set_margin(Edge.Left, 5)
        root_child0_child0.set_margin(Edge.Top, 5)
        root_child0_child0.set_margin(Edge.Right, 5)
        root_child0_child0.set_margin(Edge.Bottom, 5)
        root_child0_child0.set_padding(Edge.Left, YGValuePercent(3))
        root_child0_child0.set_padding(Edge.Top, YGValuePercent(3))
        root_child0_child0.set_padding(Edge.Right, YGValuePercent(3))
        root_child0_child0.set_padding(Edge.Bottom, YGValuePercent(3))
        root_child0_child0.width = YGValuePercent(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.set_margin(Edge.Left, YGValuePercent(5))
        root_child0_child0_child0.set_margin(Edge.Top, YGValuePercent(5))
        root_child0_child0_child0.set_margin(Edge.Right, YGValuePercent(5))
        root_child0_child0_child0.set_margin(Edge.Bottom, YGValuePercent(5))
        root_child0_child0_child0.set_padding(Edge.Left, 3)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 3)
        root_child0_child0_child0.set_padding(Edge.Bottom, 3)
        root_child0_child0_child0.width = YGValuePercent(45)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 4
        root_child1.flex_basis = YGValuePercent(15)
        root_child1.min_width = YGValuePercent(20)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 190)
        assert_float_approx(root_child0.layout_height, 48)

        assert_float_approx(root_child0_child0.layout_left, 8)
        assert_float_approx(root_child0_child0.layout_top, 8)
        assert_float_approx(root_child0_child0.layout_width, 92)
        assert_float_approx(root_child0_child0.layout_height, 25)

        assert_float_approx(root_child0_child0_child0.layout_left, 10)
        assert_float_approx(root_child0_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0_child0.layout_width, 36)
        assert_float_approx(root_child0_child0_child0.layout_height, 6)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 58)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 142)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 5)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 190)
        assert_float_approx(root_child0.layout_height, 48)

        assert_float_approx(root_child0_child0.layout_left, 90)
        assert_float_approx(root_child0_child0.layout_top, 8)
        assert_float_approx(root_child0_child0.layout_width, 92)
        assert_float_approx(root_child0_child0.layout_height, 25)

        assert_float_approx(root_child0_child0_child0.layout_left, 46)
        assert_float_approx(root_child0_child0_child0.layout_top, 10)
        assert_float_approx(root_child0_child0_child0.layout_width, 36)
        assert_float_approx(root_child0_child0_child0.layout_height, 6)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 58)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 142)

    def test_percentage_margin_should_calculate_based_only_on_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_margin(Edge.Left, YGValuePercent(10))
        root_child0.set_margin(Edge.Top, YGValuePercent(10))
        root_child0.set_margin(Edge.Right, YGValuePercent(10))
        root_child0.set_margin(Edge.Bottom, YGValuePercent(10))
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 160)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 20)
        assert_float_approx(root_child0.layout_top, 20)
        assert_float_approx(root_child0.layout_width, 160)
        assert_float_approx(root_child0.layout_height, 60)

        assert_float_approx(root_child0_child0.layout_left, 150)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

    def test_percentage_padding_should_calculate_based_only_on_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_padding(Edge.Left, YGValuePercent(10))
        root_child0.set_padding(Edge.Top, YGValuePercent(10))
        root_child0.set_padding(Edge.Right, YGValuePercent(10))
        root_child0.set_padding(Edge.Bottom, YGValuePercent(10))
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(10)
        root_child0_child0.height = YGValuePoint(10)
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 20)
        assert_float_approx(root_child0_child0.layout_top, 20)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 170)
        assert_float_approx(root_child0_child0.layout_top, 20)
        assert_float_approx(root_child0_child0.layout_width, 10)
        assert_float_approx(root_child0_child0.layout_height, 10)

    def test_percentage_absolute_position(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, YGValuePercent(30))
        root_child0.set_position(Edge.Top, YGValuePercent(10))
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 60)
        assert_float_approx(root_child0.layout_top, 10)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 10)

    def test_percentage_width_height_undefined_parent_size(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePercent(50)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 0)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 0)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 0)

    def test_percent_within_flex_grow(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(350)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.width = YGValuePercent(100)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(100)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 350)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 150)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 150)
        assert_float_approx(root_child1_child0.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 250)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 350)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 250)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 100)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 150)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 150)
        assert_float_approx(root_child1_child0.layout_height, 0)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 100)

    def test_percentage_container_in_wrapping_container(self):
        config = Config()
        root = Node(config)
        root.justify_content = Justify.Center
        root.align_items = Align.Center
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.justify_content = Justify.Center
        root_child0_child0.width = YGValuePercent(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.width = YGValuePoint(50)
        root_child0_child0_child0.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.width = YGValuePoint(50)
        root_child0_child0_child1.height = YGValuePoint(50)
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child0_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 75)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 100)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child0_child1.layout_height, 50)

    def test_percent_absolute_position(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.position_type = PositionType.Absolute
        root_child0.set_position(Edge.Left, YGValuePercent(50))
        root_child0.width = YGValuePercent(100)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePercent(100)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePercent(100)
        root_child0.insert_child(root_child0_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 60)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 60)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 60)
        assert_float_approx(root_child0_child1.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 60)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 60)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, -60)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 60)
        assert_float_approx(root_child0_child1.layout_height, 50)

    def test_percent_of_minmax_main(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.max_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

    def test_percent_of_minmax_cross_stretched(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.max_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

    def test_percent_absolute_of_minmax_cross_stretched(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.max_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Absolute
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

    def test_percent_of_minmax_cross_unstretched(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.max_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

    def test_percent_of_max_cross_unstretched(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.max_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_percent_of_max_main(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.max_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 0)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 0)
        assert_float_approx(root_child0.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_percent_of_min_cross_unstretched(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_percent_of_min_main(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_percent_of_min_main_multiple(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.min_width = YGValuePoint(60)
        root.height = YGValuePoint(50)

        root_child0 = Node(config)
        root_child0.width = YGValuePercent(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePercent(50)
        root_child1.height = YGValuePoint(20)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePercent(50)
        root_child2.height = YGValuePoint(20)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 30)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, 60)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 60)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 30)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 30)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 30)
        assert_float_approx(root_child1.layout_height, 20)

        assert_float_approx(root_child2.layout_left, -30)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 30)
        assert_float_approx(root_child2.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_percentage_flex_basis_cross_min_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)
        root.height = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.set_min_height_percent(60)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 2
        root_child1.set_min_height_percent(10)
        root.insert_child(root_child1, 1)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 120)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 120)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 80)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 200)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 120)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 120)
        assert_float_approx(root_child1.layout_width, 200)
        assert_float_approx(root_child1.layout_height, 80)
