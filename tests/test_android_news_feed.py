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
    Overflow,
    Display,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


class TestAndroidNewsFeed:
    def test_android_news_feed(self):
        config = Config()
        root = Node(config)
        root.align_content = Align.Stretch
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(1080)

        root_child0 = Node(config)
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.align_content = Align.Stretch
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child0_child0 = Node(config)
        root_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0.insert_child(root_child0_child0_child0, 0)

        root_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0_child0_child0.align_items = Align.FlexStart
        root_child0_child0_child0_child0.set_margin(Edge.Start, 36)
        root_child0_child0_child0_child0.set_margin(Edge.Top, 24)
        root_child0_child0_child0.insert_child(root_child0_child0_child0_child0, 0)

        root_child0_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0_child0_child0.insert_child(root_child0_child0_child0_child0_child0, 0)

        root_child0_child0_child0_child0_child0_child0 = Node(config)
        root_child0_child0_child0_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0_child0_child0_child0_child0.width = YGValuePoint(120)
        root_child0_child0_child0_child0_child0_child0.height = YGValuePoint(120)
        root_child0_child0_child0_child0_child0.insert_child(
            root_child0_child0_child0_child0_child0_child0, 0
        )

        root_child0_child0_child0_child0_child1 = Node(config)
        root_child0_child0_child0_child0_child1.align_content = Align.Stretch
        root_child0_child0_child0_child0_child1.flex_shrink = 1
        root_child0_child0_child0_child0_child1.set_margin(Edge.Right, 36)
        root_child0_child0_child0_child0_child1.set_padding(Edge.Left, 36)
        root_child0_child0_child0_child0_child1.set_padding(Edge.Top, 21)
        root_child0_child0_child0_child0_child1.set_padding(Edge.Right, 36)
        root_child0_child0_child0_child0_child1.set_padding(Edge.Bottom, 18)
        root_child0_child0_child0_child0.insert_child(root_child0_child0_child0_child0_child1, 1)

        root_child0_child0_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child0_child0_child1_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child0_child0_child1_child0.align_content = Align.Stretch
        root_child0_child0_child0_child0_child1_child0.flex_shrink = 1
        root_child0_child0_child0_child0_child1.insert_child(
            root_child0_child0_child0_child0_child1_child0, 0
        )

        root_child0_child0_child0_child0_child1_child1 = Node(config)
        root_child0_child0_child0_child0_child1_child1.align_content = Align.Stretch
        root_child0_child0_child0_child0_child1_child1.flex_shrink = 1
        root_child0_child0_child0_child0_child1.insert_child(
            root_child0_child0_child0_child0_child1_child1, 1
        )

        root_child0_child0_child1 = Node(config)
        root_child0_child0_child1.align_content = Align.Stretch
        root_child0_child0.insert_child(root_child0_child0_child1, 1)

        root_child0_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child1_child0.align_content = Align.Stretch
        root_child0_child0_child1_child0.align_items = Align.FlexStart
        root_child0_child0_child1_child0.set_margin(Edge.Start, 174)
        root_child0_child0_child1_child0.set_margin(Edge.Top, 24)
        root_child0_child0_child1.insert_child(root_child0_child0_child1_child0, 0)

        root_child0_child0_child1_child0_child0 = Node(config)
        root_child0_child0_child1_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child1_child0_child0.align_content = Align.Stretch
        root_child0_child0_child1_child0.insert_child(root_child0_child0_child1_child0_child0, 0)

        root_child0_child0_child1_child0_child0_child0 = Node(config)
        root_child0_child0_child1_child0_child0_child0.align_content = Align.Stretch
        root_child0_child0_child1_child0_child0_child0.width = YGValuePoint(72)
        root_child0_child0_child1_child0_child0_child0.height = YGValuePoint(72)
        root_child0_child0_child1_child0_child0.insert_child(
            root_child0_child0_child1_child0_child0_child0, 0
        )

        root_child0_child0_child1_child0_child1 = Node(config)
        root_child0_child0_child1_child0_child1.align_content = Align.Stretch
        root_child0_child0_child1_child0_child1.flex_shrink = 1
        root_child0_child0_child1_child0_child1.set_margin(Edge.Right, 36)
        root_child0_child0_child1_child0_child1.set_padding(Edge.Left, 36)
        root_child0_child0_child1_child0_child1.set_padding(Edge.Top, 21)
        root_child0_child0_child1_child0_child1.set_padding(Edge.Right, 36)
        root_child0_child0_child1_child0_child1.set_padding(Edge.Bottom, 18)
        root_child0_child0_child1_child0.insert_child(root_child0_child0_child1_child0_child1, 1)

        root_child0_child0_child1_child0_child1_child0 = Node(config)
        root_child0_child0_child1_child0_child1_child0.flex_direction = FlexDirection.Row
        root_child0_child0_child1_child0_child1_child0.align_content = Align.Stretch
        root_child0_child0_child1_child0_child1_child0.flex_shrink = 1
        root_child0_child0_child1_child0_child1.insert_child(
            root_child0_child0_child1_child0_child1_child0, 0
        )

        root_child0_child0_child1_child0_child1_child1 = Node(config)
        root_child0_child0_child1_child0_child1_child1.align_content = Align.Stretch
        root_child0_child0_child1_child0_child1_child1.flex_shrink = 1
        root_child0_child0_child1_child0_child1.insert_child(
            root_child0_child0_child1_child0_child1_child1, 1
        )

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 1080)
        assert_float_approx(root.layout_height, 240)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1080)
        assert_float_approx(root_child0.layout_height, 240)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 1080)
        assert_float_approx(root_child0_child0.layout_height, 240)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 1080)
        assert_float_approx(root_child0_child0_child0.layout_height, 144)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 36)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 24)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 1044)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 120)

        assert_float_approx(root_child0_child0_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_width, 120)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_height, 120)

        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_width, 120)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_height, 120)

        assert_float_approx(root_child0_child0_child0_child0_child1.layout_left, 120)
        assert_float_approx(root_child0_child0_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child1.layout_width, 72)
        assert_float_approx(root_child0_child0_child0_child0_child1.layout_height, 39)

        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_left, 36)
        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_top, 21)
        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_left, 36)
        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_top, 21)
        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_width, 0)
        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_height, 0)

        assert_float_approx(root_child0_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child0_child1.layout_top, 144)
        assert_float_approx(root_child0_child0_child1.layout_width, 1080)
        assert_float_approx(root_child0_child0_child1.layout_height, 96)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 174)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 24)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 906)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 72)

        assert_float_approx(root_child0_child0_child1_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0_child1_child0_child0.layout_height, 72)

        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_height, 72)

        assert_float_approx(root_child0_child0_child1_child0_child1.layout_left, 72)
        assert_float_approx(root_child0_child0_child1_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1_child0_child1.layout_width, 72)
        assert_float_approx(root_child0_child0_child1_child0_child1.layout_height, 39)

        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_left, 36)
        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_top, 21)
        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_left, 36)
        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_top, 21)
        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_width, 0)
        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_height, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 1080)
        assert_float_approx(root.layout_height, 240)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1080)
        assert_float_approx(root_child0.layout_height, 240)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 1080)
        assert_float_approx(root_child0_child0.layout_height, 240)

        assert_float_approx(root_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0.layout_width, 1080)
        assert_float_approx(root_child0_child0_child0.layout_height, 144)

        assert_float_approx(root_child0_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0_child0.layout_top, 24)
        assert_float_approx(root_child0_child0_child0_child0.layout_width, 1044)
        assert_float_approx(root_child0_child0_child0_child0.layout_height, 120)

        assert_float_approx(root_child0_child0_child0_child0_child0.layout_left, 924)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_width, 120)
        assert_float_approx(root_child0_child0_child0_child0_child0.layout_height, 120)

        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_width, 120)
        assert_float_approx(root_child0_child0_child0_child0_child0_child0.layout_height, 120)

        assert_float_approx(root_child0_child0_child0_child0_child1.layout_left, 816)
        assert_float_approx(root_child0_child0_child0_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child0_child0_child1.layout_width, 72)
        assert_float_approx(root_child0_child0_child0_child0_child1.layout_height, 39)

        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_left, 36)
        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_top, 21)
        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child0_child0_child1_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_left, 36)
        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_top, 21)
        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_width, 0)
        assert_float_approx(root_child0_child0_child0_child0_child1_child1.layout_height, 0)

        assert_float_approx(root_child0_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child0_child1.layout_top, 144)
        assert_float_approx(root_child0_child0_child1.layout_width, 1080)
        assert_float_approx(root_child0_child0_child1.layout_height, 96)

        assert_float_approx(root_child0_child0_child1_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child1_child0.layout_top, 24)
        assert_float_approx(root_child0_child0_child1_child0.layout_width, 906)
        assert_float_approx(root_child0_child0_child1_child0.layout_height, 72)

        assert_float_approx(root_child0_child0_child1_child0_child0.layout_left, 834)
        assert_float_approx(root_child0_child0_child1_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0_child1_child0_child0.layout_height, 72)

        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_width, 72)
        assert_float_approx(root_child0_child0_child1_child0_child0_child0.layout_height, 72)

        assert_float_approx(root_child0_child0_child1_child0_child1.layout_left, 726)
        assert_float_approx(root_child0_child0_child1_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child0_child1_child0_child1.layout_width, 72)
        assert_float_approx(root_child0_child0_child1_child0_child1.layout_height, 39)

        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_left, 36)
        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_top, 21)
        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_width, 0)
        assert_float_approx(root_child0_child0_child1_child0_child1_child0.layout_height, 0)

        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_left, 36)
        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_top, 21)
        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_width, 0)
        assert_float_approx(root_child0_child0_child1_child0_child1_child1.layout_height, 0)
