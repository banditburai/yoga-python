import pytest
from yoga import (
    Node,
    Config,
    Direction,
    PositionType,
    Edge,
    Unit,
    YGValuePoint,
    YGValuePercent,
    YGValueUndefined,
    ExperimentalFeature,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestRelayout:
    def test_dont_cache_computed_flex_basis_between_layouts(self):
        config = Config()
        config.set_experimental_feature_enabled(ExperimentalFeature.WebFlexBasis, True)

        root = Node(config)
        root.height = YGValuePercent(100)
        root.width = YGValuePercent(100)

        root_child0 = Node(config)
        root_child0.flex_basis = YGValuePercent(100)
        root.insert_child(root_child0, 0)

        root.calculate_layout(100, float("nan"), Direction.LTR)
        root.calculate_layout(100, 100, Direction.LTR)

        assert_float_approx(root_child0.layout_height, 100)

        root.free_recursive()

    def test_recalculate_resolvedDimonsion_onchange(self):
        root = Node()

        root_child0 = Node()
        root_child0.min_height = YGValuePoint(10)
        root_child0.max_height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)
        assert_float_approx(root_child0.layout_height, 10)

        root_child0.min_height = YGValueUndefined
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root_child0.layout_height, 0)

        root.free_recursive()

    def test_relayout_containing_block_size_changes(self):
        config = Config()

        root = Node(config)
        root.position_type = PositionType.Absolute

        root_child0 = Node(config)
        root_child0.position_type = PositionType.Relative
        root_child0.set_margin(Edge.Left, 4)
        root_child0.set_margin(Edge.Top, 5)
        root_child0.set_margin(Edge.Right, 9)
        root_child0.set_margin(Edge.Bottom, 1)
        root_child0.set_padding(Edge.Left, 2)
        root_child0.set_padding(Edge.Top, 9)
        root_child0.set_padding(Edge.Right, 11)
        root_child0.set_padding(Edge.Bottom, 13)
        root_child0.set_border(Edge.Left, 5)
        root_child0.set_border(Edge.Top, 6)
        root_child0.set_border(Edge.Right, 7)
        root_child0.set_border(Edge.Bottom, 8)
        root_child0.width = YGValuePoint(500)
        root_child0.height = YGValuePoint(500)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.set_margin(Edge.Left, 8)
        root_child0_child0.set_margin(Edge.Top, 6)
        root_child0_child0.set_margin(Edge.Right, 3)
        root_child0_child0.set_margin(Edge.Bottom, 9)
        root_child0_child0.set_padding(Edge.Left, 1)
        root_child0_child0.set_padding(Edge.Top, 7)
        root_child0_child0.set_padding(Edge.Right, 9)
        root_child0_child0.set_padding(Edge.Bottom, 4)
        root_child0_child0.set_border(Edge.Left, 8)
        root_child0_child0.set_border(Edge.Top, 10)
        root_child0_child0.set_border(Edge.Right, 2)
        root_child0_child0.set_border(Edge.Bottom, 1)
        root_child0_child0.width = YGValuePoint(200)
        root_child0_child0.height = YGValuePoint(200)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.set_position(Edge.Left, 2)
        root_child0_child0_child0.set_position(Edge.Right, 12)
        root_child0_child0_child0.set_margin(Edge.Left, 9)
        root_child0_child0_child0.set_margin(Edge.Top, 12)
        root_child0_child0_child0.set_margin(Edge.Right, 4)
        root_child0_child0_child0.set_margin(Edge.Bottom, 7)
        root_child0_child0_child0.set_padding(Edge.Left, 5)
        root_child0_child0_child0.set_padding(Edge.Top, 3)
        root_child0_child0_child0.set_padding(Edge.Right, 8)
        root_child0_child0_child0.set_padding(Edge.Bottom, 10)
        root_child0_child0_child0.set_border(Edge.Left, 2)
        root_child0_child0_child0.set_border(Edge.Top, 1)
        root_child0_child0_child0.set_border(Edge.Right, 5)
        root_child0_child0_child0.set_border(Edge.Bottom, 9)
        root_child0_child0_child0.width = YGValuePercent(41)
        root_child0_child0_child0.height = YGValuePercent(63)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 1)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 513)
        assert_float_approx(root.layout_height, 506)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 279)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, -2)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0_child0.layout_height, 306)

        root_child0.width = YGValuePoint(456)
        root_child0.height = YGValuePoint(432)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 469)
        assert_float_approx(root.layout_height, 438)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 456)
        assert_float_approx(root_child0.layout_height, 432)

        assert_float_approx(root_child0_child0.layout_left, 15)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 1)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 182)
        assert_float_approx(root_child0_child0_child0.layout_height, 263)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 469)
        assert_float_approx(root.layout_height, 438)

        assert_float_approx(root_child0.layout_left, 4)
        assert_float_approx(root_child0.layout_top, 5)
        assert_float_approx(root_child0.layout_width, 456)
        assert_float_approx(root_child0.layout_height, 432)

        assert_float_approx(root_child0_child0.layout_left, 235)
        assert_float_approx(root_child0_child0.layout_top, 21)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 200)

        assert_float_approx(root_child0_child0_child0.layout_left, 16)
        assert_float_approx(root_child0_child0_child0.layout_top, 29)
        assert_float_approx(root_child0_child0_child0.layout_width, 182)
        assert_float_approx(root_child0_child0_child0.layout_height, 263)

        root.free_recursive()

    def test_has_new_layout_flag_set_static(self):
        root = Node()
        root.width = YGValuePoint(100)
        root.height = YGValuePoint(100)

        root_child0 = Node()
        root_child0.position_type = PositionType.Static
        root_child0.width = YGValuePoint(10)
        root_child0.height = YGValuePoint(10)
        root.insert_child(root_child0, 0)

        root_child0_child1 = Node()
        root_child0_child1.position_type = PositionType.Absolute
        root_child0_child1.width = YGValuePoint(5)
        root_child0_child1.height = YGValuePoint(5)
        root_child0.insert_child(root_child0_child1, 0)

        root_child0_child0 = Node()
        root_child0_child0.position_type = PositionType.Static
        root_child0_child0.width = YGValuePoint(5)
        root_child0_child0.height = YGValuePoint(5)
        root_child0.insert_child(root_child0_child0, 1)

        root_child0_child0_child0 = Node()
        root_child0_child0_child0.position_type = PositionType.Absolute
        root_child0_child0_child0.width = YGValuePercent(1)
        root_child0_child0_child0.height = YGValuePoint(1)
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        root.has_new_layout = False
        root_child0.has_new_layout = False
        root_child0_child0.has_new_layout = False
        root_child0_child0_child0.has_new_layout = False

        root.width = YGValuePoint(110)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.has_new_layout is True
        assert root_child0.has_new_layout is True
        assert root_child0_child0.has_new_layout is True
        assert root_child0_child0_child0.has_new_layout is True

        root.free_recursive()
