import math
import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    Justify,
    Align,
    PositionType,
    Wrap,
    Overflow,
    Unit,
    Edge,
    BoxSizing,
    Errata,
)


class TestDefaultValues:
    def test_assert_default_values(self):
        root = Node()

        assert root.child_count == 0

        assert root.direction == Direction.Inherit
        assert root.flex_direction == FlexDirection.Column
        assert root.justify_content == Justify.FlexStart
        assert root.align_content == Align.FlexStart
        assert root.align_items == Align.Stretch
        assert root.align_self == Align.Auto
        assert root.position_type == PositionType.Relative
        assert root.flex_wrap == Wrap.NoWrap
        assert root.overflow == Overflow.Visible
        assert root.flex_grow == 0
        assert root.flex_shrink == 0
        assert root.flex_basis.unit == Unit.Auto

        assert root.get_position(Edge.Left).unit == Unit.Undefined
        assert root.get_position(Edge.Top).unit == Unit.Undefined
        assert root.get_position(Edge.Right).unit == Unit.Undefined
        assert root.get_position(Edge.Bottom).unit == Unit.Undefined
        assert root.get_position(Edge.Start).unit == Unit.Undefined
        assert root.get_position(Edge.End).unit == Unit.Undefined

        assert root.get_margin(Edge.Left).unit == Unit.Undefined
        assert root.get_margin(Edge.Top).unit == Unit.Undefined
        assert root.get_margin(Edge.Right).unit == Unit.Undefined
        assert root.get_margin(Edge.Bottom).unit == Unit.Undefined
        assert root.get_margin(Edge.Start).unit == Unit.Undefined
        assert root.get_margin(Edge.End).unit == Unit.Undefined

        assert root.get_padding(Edge.Left).unit == Unit.Undefined
        assert root.get_padding(Edge.Top).unit == Unit.Undefined
        assert root.get_padding(Edge.Right).unit == Unit.Undefined
        assert root.get_padding(Edge.Bottom).unit == Unit.Undefined
        assert root.get_padding(Edge.Start).unit == Unit.Undefined
        assert root.get_padding(Edge.End).unit == Unit.Undefined

        assert math.isnan(root.get_border(Edge.Left))
        assert math.isnan(root.get_border(Edge.Top))
        assert math.isnan(root.get_border(Edge.Right))
        assert math.isnan(root.get_border(Edge.Bottom))
        assert math.isnan(root.get_border(Edge.Start))
        assert math.isnan(root.get_border(Edge.End))

        assert root.width.unit == Unit.Auto
        assert root.height.unit == Unit.Auto
        assert root.min_width.unit == Unit.Undefined
        assert root.min_height.unit == Unit.Undefined
        assert root.max_width.unit == Unit.Undefined
        assert root.max_height.unit == Unit.Undefined

        assert root.layout_left == 0
        assert root.layout_top == 0
        assert root.layout_right == 0
        assert root.layout_bottom == 0

        assert root.layout_margin(Edge.Left) == 0
        assert root.layout_margin(Edge.Top) == 0
        assert root.layout_margin(Edge.Right) == 0
        assert root.layout_margin(Edge.Bottom) == 0

        assert root.layout_padding(Edge.Left) == 0
        assert root.layout_padding(Edge.Top) == 0
        assert root.layout_padding(Edge.Right) == 0
        assert root.layout_padding(Edge.Bottom) == 0

        assert root.layout_border(Edge.Left) == 0
        assert root.layout_border(Edge.Top) == 0
        assert root.layout_border(Edge.Right) == 0
        assert root.layout_border(Edge.Bottom) == 0

        assert math.isnan(root.layout_width)
        assert math.isnan(root.layout_height)
        assert root.layout_direction == Direction.Inherit

    def test_assert_webdefault_values(self):
        config = Config()
        config.use_web_defaults = True
        root = Node(config)

        assert root.flex_direction == FlexDirection.Row
        assert root.align_content == Align.Stretch
        assert root.flex_shrink == 1.0

    def test_assert_webdefault_values_reset(self):
        config = Config()
        config.use_web_defaults = True
        root = Node(config)
        root.reset()

        assert root.flex_direction == FlexDirection.Row
        assert root.align_content == Align.Stretch
        assert root.flex_shrink == 1.0

    def test_assert_legacy_stretch_behaviour(self):
        config = Config()
        config.errata = Errata.StretchFlexBasis
        root = Node(config)
        root.width = 500
        root.height = 500

        root_child0 = Node(config)
        root_child0.align_items = Align.FlexStart
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_grow = 1
        root_child0_child0.flex_shrink = 1
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.flex_grow = 1
        root_child0_child0_child0.flex_shrink = 1
        root_child0_child0.insert_child(root_child0_child0_child0, 0)
        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert root.layout_left == 0
        assert root.layout_top == 0
        assert root.layout_width == 500
        assert root.layout_height == 500

        assert root_child0.layout_left == 0
        assert root_child0.layout_top == 0
        assert root_child0.layout_width == 500
        assert root_child0.layout_height == 500

        assert root_child0_child0.layout_left == 0
        assert root_child0_child0.layout_top == 0
        assert root_child0_child0.layout_width == 0
        assert root_child0_child0.layout_height == 500

        assert root_child0_child0_child0.layout_left == 0
        assert root_child0_child0_child0.layout_top == 0
        assert root_child0_child0_child0.layout_width == 0
        assert root_child0_child0_child0.layout_height == 500

    def test_assert_box_sizing_border_box(self):
        config = Config()
        root = Node(config)

        assert root.box_sizing == BoxSizing.BorderBox

    def test_initialise_flexShrink_flexGrow(self):
        node0 = Node()
        node0.flex_shrink = 1
        assert node0.flex_shrink == 1

        node0.flex_shrink = float("nan")  # This should clear it
        node0.flex_grow = 3
        assert node0.flex_shrink == 0
        assert node0.flex_grow == 3

        node0.flex_grow = float("nan")
        node0.flex_shrink = 3
        assert node0.flex_grow == 0
        assert node0.flex_shrink == 3
