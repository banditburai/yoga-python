import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    PositionType,
    YGValuePoint,
    YGValuePercent,
    Edge,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestRounding:
    def test_rounding_flex_basis_flex_grow_row_width_of_100(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 33)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 33)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 34)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 67)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 33)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 67)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 33)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 33)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 34)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 33)
        assert_float_approx(root_child2.layout_height, 100)

    def test_rounding_flex_basis_flex_grow_row_prime_number_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(113)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root.insert_child(root_child2, 2)

        root_child3 = Node(config)
        root_child3.flex_grow = 1
        root.insert_child(root_child3, 3)

        root_child4 = Node(config)
        root_child4.flex_grow = 1
        root.insert_child(root_child4, 4)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 113)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 23)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 23)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 22)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 45)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 23)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 68)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 22)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 90)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 23)
        assert_float_approx(root_child4.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 113)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 90)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 23)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 68)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 22)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 45)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 23)
        assert_float_approx(root_child2.layout_height, 100)

        assert_float_approx(root_child3.layout_left, 23)
        assert_float_approx(root_child3.layout_top, 0)
        assert_float_approx(root_child3.layout_width, 22)
        assert_float_approx(root_child3.layout_height, 100)

        assert_float_approx(root_child4.layout_left, 0)
        assert_float_approx(root_child4.layout_top, 0)
        assert_float_approx(root_child4.layout_width, 23)
        assert_float_approx(root_child4.layout_height, 100)

    def test_rounding_flex_basis_flex_shrink_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(101)
        root.height = YGValuePoint(100)

        root_child0 = Node(config)
        root_child0.flex_shrink = 1
        root_child0.flex_basis = YGValuePoint(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_basis = YGValuePoint(25)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_basis = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 101)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 51)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 51)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 76)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 101)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 51)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 25)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 100)

    def test_rounding_flex_basis_overrides_main_size(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(113)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 64)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 24)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 64)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 24)

    def test_rounding_total_fractial(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(87.4)
        root.height = YGValuePoint(113.4)

        root_child0 = Node(config)
        root_child0.flex_grow = 0.7
        root_child0.flex_basis = YGValuePoint(50.3)
        root_child0.height = YGValuePoint(20.3)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1.6
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1.1
        root_child2.height = YGValuePoint(10.7)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 87)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 87)
        assert_float_approx(root_child0.layout_height, 59)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 59)
        assert_float_approx(root_child1.layout_width, 87)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 87)
        assert_float_approx(root_child2.layout_height, 24)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 87)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 87)
        assert_float_approx(root_child0.layout_height, 59)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 59)
        assert_float_approx(root_child1.layout_width, 87)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 87)
        assert_float_approx(root_child2.layout_height, 24)

    def test_rounding_total_fractial_nested(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(87.4)
        root.height = YGValuePoint(113.4)

        root_child0 = Node(config)
        root_child0.flex_grow = 0.7
        root_child0.flex_basis = YGValuePoint(50.3)
        root_child0.height = YGValuePoint(20.3)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_basis = YGValuePoint(0.3)
        root_child0_child0.set_position(Edge.Bottom, 13.3)
        root_child0_child0.height = YGValuePoint(9.9)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.flex_grow = 4
        root_child0_child1.flex_basis = YGValuePoint(0.3)
        root_child0_child1.set_position(Edge.Top, 13.3)
        root_child0_child1.height = YGValuePoint(1.1)
        root_child0.insert_child(root_child0_child1, 1)

        root_child1 = Node(config)
        root_child1.flex_grow = 1.6
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1.1
        root_child2.height = YGValuePoint(10.7)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 87)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 87)
        assert_float_approx(root_child0.layout_height, 59)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, -13)
        assert_float_approx(root_child0_child0.layout_width, 87)
        assert_float_approx(root_child0_child0.layout_height, 12)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 25)
        assert_float_approx(root_child0_child1.layout_width, 87)
        assert_float_approx(root_child0_child1.layout_height, 47)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 59)
        assert_float_approx(root_child1.layout_width, 87)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 87)
        assert_float_approx(root_child2.layout_height, 24)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 87)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 87)
        assert_float_approx(root_child0.layout_height, 59)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, -13)
        assert_float_approx(root_child0_child0.layout_width, 87)
        assert_float_approx(root_child0_child0.layout_height, 12)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 25)
        assert_float_approx(root_child0_child1.layout_width, 87)
        assert_float_approx(root_child0_child1.layout_height, 47)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 59)
        assert_float_approx(root_child1.layout_width, 87)
        assert_float_approx(root_child1.layout_height, 30)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 87)
        assert_float_approx(root_child2.layout_height, 24)

    def test_rounding_fractial_input_1(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(113.4)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 64)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 24)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 64)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 24)

    def test_rounding_fractial_input_2(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(113.6)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 114)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 65)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 24)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 114)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 65)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 24)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 25)

    def test_rounding_fractial_input_3(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_position(Edge.Top, 0.3)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(113.4)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 114)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 24)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 114)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 65)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 24)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 25)

    def test_rounding_fractial_input_4(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.set_position(Edge.Top, 0.7)
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(113.4)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.flex_basis = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 1)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 64)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 24)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 1)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 113)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 64)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 64)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 25)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 89)
        assert_float_approx(root_child2.layout_width, 100)
        assert_float_approx(root_child2.layout_height, 24)

    def test_rounding_inner_node_controversy_horizontal(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.flex_grow = 1
        root_child1_child0.height = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 10)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 107)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 107)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 106)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 106)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 213)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 107)
        assert_float_approx(root_child2.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 320)
        assert_float_approx(root.layout_height, 10)

        assert_float_approx(root_child0.layout_left, 213)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 107)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child1.layout_left, 107)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 106)
        assert_float_approx(root_child1.layout_height, 10)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 106)
        assert_float_approx(root_child1_child0.layout_height, 10)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 107)
        assert_float_approx(root_child2.layout_height, 10)

    def test_rounding_inner_node_controversy_vertical(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.width = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.width = YGValuePoint(10)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.flex_grow = 1
        root_child1_child0.width = YGValuePoint(10)
        root_child1.insert_child(root_child1_child0, 0)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.width = YGValuePoint(10)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 10)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 107)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 107)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 106)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 10)
        assert_float_approx(root_child1_child0.layout_height, 106)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 107)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 10)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 10)
        assert_float_approx(root_child0.layout_height, 107)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 107)
        assert_float_approx(root_child1.layout_width, 10)
        assert_float_approx(root_child1.layout_height, 106)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 10)
        assert_float_approx(root_child1_child0.layout_height, 106)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 213)
        assert_float_approx(root_child2.layout_width, 10)
        assert_float_approx(root_child2.layout_height, 107)

    def test_rounding_inner_node_controversy_combined(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(640)
        root.height = YGValuePoint(320)

        root_child0 = Node(config)
        root_child0.flex_grow = 1
        root_child0.height = YGValuePercent(100)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.flex_grow = 1
        root_child1.height = YGValuePercent(100)
        root.insert_child(root_child1, 1)

        root_child1_child0 = Node(config)
        root_child1_child0.flex_grow = 1
        root_child1_child0.width = YGValuePercent(100)
        root_child1.insert_child(root_child1_child0, 0)

        root_child1_child1 = Node(config)
        root_child1_child1.flex_grow = 1
        root_child1_child1.width = YGValuePercent(100)
        root_child1.insert_child(root_child1_child1, 1)

        root_child1_child1_child0 = Node(config)
        root_child1_child1_child0.flex_grow = 1
        root_child1_child1_child0.width = YGValuePercent(100)
        root_child1_child1.insert_child(root_child1_child1_child0, 0)

        root_child1_child2 = Node(config)
        root_child1_child2.flex_grow = 1
        root_child1_child2.width = YGValuePercent(100)
        root_child1.insert_child(root_child1_child2, 2)

        root_child2 = Node(config)
        root_child2.flex_grow = 1
        root_child2.height = YGValuePercent(100)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 640)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 213)
        assert_float_approx(root_child0.layout_height, 320)

        assert_float_approx(root_child1.layout_left, 213)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 214)
        assert_float_approx(root_child1.layout_height, 320)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 214)
        assert_float_approx(root_child1_child0.layout_height, 107)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 107)
        assert_float_approx(root_child1_child1.layout_width, 214)
        assert_float_approx(root_child1_child1.layout_height, 106)

        assert_float_approx(root_child1_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child1_child0.layout_width, 214)
        assert_float_approx(root_child1_child1_child0.layout_height, 106)

        assert_float_approx(root_child1_child2.layout_left, 0)
        assert_float_approx(root_child1_child2.layout_top, 213)
        assert_float_approx(root_child1_child2.layout_width, 214)
        assert_float_approx(root_child1_child2.layout_height, 107)

        assert_float_approx(root_child2.layout_left, 427)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 213)
        assert_float_approx(root_child2.layout_height, 320)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 640)
        assert_float_approx(root.layout_height, 320)

        assert_float_approx(root_child0.layout_left, 427)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 213)
        assert_float_approx(root_child0.layout_height, 320)

        assert_float_approx(root_child1.layout_left, 213)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 214)
        assert_float_approx(root_child1.layout_height, 320)

        assert_float_approx(root_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child0.layout_width, 214)
        assert_float_approx(root_child1_child0.layout_height, 107)

        assert_float_approx(root_child1_child1.layout_left, 0)
        assert_float_approx(root_child1_child1.layout_top, 107)
        assert_float_approx(root_child1_child1.layout_width, 214)
        assert_float_approx(root_child1_child1.layout_height, 106)

        assert_float_approx(root_child1_child1_child0.layout_left, 0)
        assert_float_approx(root_child1_child1_child0.layout_top, 0)
        assert_float_approx(root_child1_child1_child0.layout_width, 214)
        assert_float_approx(root_child1_child1_child0.layout_height, 106)

        assert_float_approx(root_child1_child2.layout_left, 0)
        assert_float_approx(root_child1_child2.layout_top, 213)
        assert_float_approx(root_child1_child2.layout_width, 214)
        assert_float_approx(root_child1_child2.layout_height, 107)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 213)
        assert_float_approx(root_child2.layout_height, 320)
