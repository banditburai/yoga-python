import pytest
from yoga import (
    Node,
    Config,
    Direction,
    FlexDirection,
    PositionType,
    Wrap,
    YGValuePoint,
    MeasureMode,
    Align,
)


def assert_float_approx(actual, expected, rel_tol=1e-6):
    assert abs(actual - expected) <= rel_tol * max(abs(expected), 1), f"{actual} != {expected}"


def longest_word_width(text, width_per_char=10):
    max_length = 0
    current_length = 0
    for c in text:
        if c == " ":
            max_length = max(current_length, max_length)
            current_length = 0
        else:
            current_length += 1
    return max(current_length, max_length) * width_per_char


def calculate_height(text, measured_width, width_per_char=10, height_per_char=10):
    if len(text) * width_per_char <= measured_width:
        return height_per_char

    words = text.split(" ")

    lines = 1
    current_line_length = 0
    for word in words:
        word_width = len(word) * width_per_char
        if word_width > measured_width:
            if current_line_length > 0:
                lines += 1
            lines += 1
            current_line_length = 0
        elif current_line_length + word_width <= measured_width:
            current_line_length += word_width + width_per_char
        else:
            lines += 1
            current_line_length = word_width + width_per_char

    return lines * height_per_char


def make_intrinsic_size_measure(inner_text):
    def intrinsic_size_measure(node, width, width_mode, height, height_mode):
        height_per_char = 10
        width_per_char = 10

        if width_mode == MeasureMode.Exactly:
            measured_width = width
        elif width_mode == MeasureMode.AtMost:
            measured_width = min(len(inner_text) * width_per_char, width)
        else:
            measured_width = len(inner_text) * width_per_char

        flex_direction = node.flex_direction

        if height_mode == MeasureMode.Exactly:
            measured_height = height
        elif height_mode == MeasureMode.AtMost:
            if flex_direction == FlexDirection.Column:
                ref_width = measured_width
            else:
                ref_width = max(longest_word_width(inner_text, width_per_char), measured_width)
            measured_height = min(
                calculate_height(inner_text, ref_width, width_per_char, height_per_char), height
            )
        else:
            if flex_direction == FlexDirection.Column:
                ref_width = measured_width
            else:
                ref_width = max(longest_word_width(inner_text, width_per_char), measured_width)
            measured_height = calculate_height(
                inner_text, ref_width, width_per_char, height_per_char
            )

        return {"width": measured_width, "height": measured_height}

    return intrinsic_size_measure


class TestIntrinsicSize:
    def test_contains_inner_text_long_word(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "LoremipsumdolorsitametconsecteturadipiscingelitSedeleifasdfettortoracauctorFuscerhoncusipsumtemporerosaliquamconsequatPraesentsoda"
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1300)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 700)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1300)
        assert_float_approx(root_child0.layout_height, 10)

    def test_contains_inner_text_no_width_no_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 70)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 70)

    def test_contains_inner_text_no_width_no_height_long_word_in_paragraph(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus loremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumlorem Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 70)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 70)

    def test_contains_inner_text_fixed_width(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.width = YGValuePoint(100)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 1290)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 1900)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 1290)

    def test_contains_inner_text_no_width_fixed_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.height = YGValuePoint(20)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 20)

    def test_contains_inner_text_fixed_width_fixed_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(20)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 1950)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 20)

    def test_contains_inner_text_max_width_max_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.max_width = YGValuePoint(50)
        root_child0.max_height = YGValuePoint(20)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 1950)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 20)

    def test_contains_inner_text_max_width_max_height_column(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.max_width = YGValuePoint(50)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 1890, rel_tol=0.01)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 1890, rel_tol=0.01)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 1890, rel_tol=0.01)

        assert_float_approx(root_child0.layout_left, 1950)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 1890, rel_tol=0.01)

    def test_contains_inner_text_max_width(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.max_width = YGValuePoint(100)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 1290)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 1900)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 1290)

    def test_contains_inner_text_fixed_width_shorter_text(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.width = YGValuePoint(100)
        root_child0.set_measure_func(make_intrinsic_size_measure("Lorem ipsum"))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 1900)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 20)

    def test_contains_inner_text_fixed_height_shorter_text(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.height = YGValuePoint(100)
        root_child0.set_measure_func(make_intrinsic_size_measure("Lorem ipsum"))
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 110)
        assert_float_approx(root_child0.layout_height, 100)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 1890)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 110)
        assert_float_approx(root_child0.layout_height, 100)

    def test_contains_inner_text_max_height(self):
        config = Config()
        root = Node(config)
        root.align_items = Align.FlexStart
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(2000)
        root.height = YGValuePoint(2000)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.max_height = YGValuePoint(20)
        root_child0.set_measure_func(
            make_intrinsic_size_measure(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum."
            )
        )
        root.insert_child(root_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 2000)
        assert_float_approx(root.layout_height, 2000)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 2000)
        assert_float_approx(root_child0.layout_height, 20)

    def test_max_content_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(float("inf"))

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 175)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 150)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 175)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 125)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

    def test_stretch_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 150)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 450)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 350)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 325)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    def test_max_content_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.height = YGValuePoint(float("inf"))

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 175)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 175)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

    def test_max_content_flex_basis_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.flex_basis = YGValuePoint(float("inf"))

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 175)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 175)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

    def test_stretch_flex_basis_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 175)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 175)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.set_width_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 75)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.set_height_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 175)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 175)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_flex_basis_column(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.set_flex_basis_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 175)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 175)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_flex_basis_row(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.set_flex_basis_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 90)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 40)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, -10)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 65)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(90)
        root_child0.set_min_width_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 75)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_min_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(90)
        root_child0.set_min_height_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 100)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, -50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, -100)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(110)
        root_child0.set_max_width_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 90)
        assert_float_approx(root.layout_height, 150)

        assert_float_approx(root_child0.layout_left, -10)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 100)
        assert_float_approx(root_child0.layout_height, 150)

        assert_float_approx(root_child0_child0.layout_left, 50)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 75)
        assert_float_approx(root_child0_child2.layout_top, 100)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_fit_content_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(90)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(110)
        root_child0.set_max_height_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 100)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 90)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 100)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, -50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, -100)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_max_content_flex_basis_row(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.set_flex_basis_max_content()

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(500)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 600)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 500)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 550)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 100)
        assert_float_approx(root.layout_height, 600)

        assert_float_approx(root_child0.layout_left, 50)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 500)

        assert_float_approx(root_child2.layout_left, 75)
        assert_float_approx(root_child2.layout_top, 550)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_max_content_min_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(100)
        root.set_min_width_max_content()

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 175)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 150)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 175)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 125)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_max_content_min_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.height = YGValuePoint(100)
        root.set_min_height_max_content()

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 100)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, -50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, -100)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_max_content_max_width(self):
        config = Config()
        root = Node(config)
        root.flex_direction = FlexDirection.Row
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.width = YGValuePoint(200)
        root.set_max_width_max_content()

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(100)
        root_child1.height = YGValuePoint(50)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(25)
        root_child2.height = YGValuePoint(50)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 175)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 50)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 150)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 175)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 125)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 25)
        assert_float_approx(root_child1.layout_top, 0)
        assert_float_approx(root_child1.layout_width, 100)
        assert_float_approx(root_child1.layout_height, 50)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 0)
        assert_float_approx(root_child2.layout_width, 25)
        assert_float_approx(root_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_max_content_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.flex_wrap = Wrap.Wrap
        root.height = YGValuePoint(200)
        root.set_max_height_max_content()

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(50)
        root_child0.height = YGValuePoint(50)
        root.insert_child(root_child0, 0)

        root_child1 = Node(config)
        root_child1.width = YGValuePoint(50)
        root_child1.height = YGValuePoint(100)
        root.insert_child(root_child1, 1)

        root_child2 = Node(config)
        root_child2.width = YGValuePoint(50)
        root_child2.height = YGValuePoint(25)
        root.insert_child(root_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 175)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 175)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child1.layout_left, 0)
        assert_float_approx(root_child1.layout_top, 50)
        assert_float_approx(root_child1.layout_width, 50)
        assert_float_approx(root_child1.layout_height, 100)

        assert_float_approx(root_child2.layout_left, 0)
        assert_float_approx(root_child2.layout_top, 150)
        assert_float_approx(root_child2.layout_width, 50)
        assert_float_approx(root_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_stretch_flex_basis_row(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 150)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 450)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 350)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 325)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_stretch_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.set_height_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_stretch_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(400)
        root_child0.set_min_width_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 150)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 450)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 350)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 325)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_stretch_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_direction = FlexDirection.Row
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.width = YGValuePoint(600)
        root_child0.set_max_width_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(100)
        root_child0_child1.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(25)
        root_child0_child2.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 50)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 150)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 500)
        assert_float_approx(root.layout_height, 50)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 500)
        assert_float_approx(root_child0.layout_height, 50)

        assert_float_approx(root_child0_child0.layout_left, 450)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 350)
        assert_float_approx(root_child0_child1.layout_top, 0)
        assert_float_approx(root_child0_child1.layout_width, 100)
        assert_float_approx(root_child0_child1.layout_height, 50)

        assert_float_approx(root_child0_child2.layout_left, 325)
        assert_float_approx(root_child0_child2.layout_top, 0)
        assert_float_approx(root_child0_child2.layout_width, 25)
        assert_float_approx(root_child0_child2.layout_height, 50)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_stretch_max_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(600)
        root_child0.set_max_height_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_stretch_min_height(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.height = YGValuePoint(500)

        root_child0 = Node(config)
        root_child0.flex_wrap = Wrap.Wrap
        root_child0.height = YGValuePoint(400)
        root_child0.set_min_height_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.width = YGValuePoint(50)
        root_child0_child0.height = YGValuePoint(50)
        root_child0.insert_child(root_child0_child0, 0)

        root_child0_child1 = Node(config)
        root_child0_child1.width = YGValuePoint(50)
        root_child0_child1.height = YGValuePoint(100)
        root_child0.insert_child(root_child0_child1, 1)

        root_child0_child2 = Node(config)
        root_child0_child2.width = YGValuePoint(50)
        root_child0_child2.height = YGValuePoint(25)
        root_child0.insert_child(root_child0_child2, 2)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 50)
        assert_float_approx(root.layout_height, 500)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 50)
        assert_float_approx(root_child0.layout_height, 500)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 50)
        assert_float_approx(root_child0_child0.layout_height, 50)

        assert_float_approx(root_child0_child1.layout_left, 0)
        assert_float_approx(root_child0_child1.layout_top, 50)
        assert_float_approx(root_child0_child1.layout_width, 50)
        assert_float_approx(root_child0_child1.layout_height, 100)

        assert_float_approx(root_child0_child2.layout_left, 0)
        assert_float_approx(root_child0_child2.layout_top, 150)
        assert_float_approx(root_child0_child2.layout_width, 50)
        assert_float_approx(root_child0_child2.layout_height, 25)

    # Text tests use measure function with long-word text for max_content and fit_content
    TEXT_MAX_CONTENT = "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet"
    TEXT_FIT_CONTENT = "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet"
    TEXT_STRETCH = "Lorem ipsum dolor sit amet"

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_fit_content_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_width_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_FIT_CONTENT))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 870)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 870)
        assert_float_approx(root_child0_child0.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, -670)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 870)
        assert_float_approx(root_child0.layout_height, 30)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 870)
        assert_float_approx(root_child0_child0.layout_height, 30)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_fit_content_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(300)
        root_child0.set_min_width_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_FIT_CONTENT))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 870)
        assert_float_approx(root_child0.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, -670)
        assert_float_approx(root_child0.layout_width, 870)
        assert_float_approx(root_child0.layout_height, 30)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_fit_content_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(1000)
        root_child0.set_max_width_fit_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_FIT_CONTENT))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 30)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 870)
        assert_float_approx(root_child0.layout_height, 30)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, -670)
        assert_float_approx(root_child0.layout_width, 870)
        assert_float_approx(root_child0.layout_height, 30)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_max_content_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_width_max_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_MAX_CONTENT))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 10)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1140)
        assert_float_approx(root_child0.layout_height, 10)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 1140)
        assert_float_approx(root_child0_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, -940)
        assert_float_approx(root_child0.layout_width, 1140)
        assert_float_approx(root_child0.layout_height, 10)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_max_content_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(200)
        root_child0.set_min_width_max_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_MAX_CONTENT))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 10)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1140)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, -940)
        assert_float_approx(root_child0.layout_width, 1140)
        assert_float_approx(root_child0.layout_height, 10)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_max_content_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(2000)
        root_child0.set_max_width_max_content()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_MAX_CONTENT))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 10)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 1140)
        assert_float_approx(root_child0.layout_height, 10)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, -940)
        assert_float_approx(root_child0.layout_width, 1140)
        assert_float_approx(root_child0.layout_height, 10)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_stretch_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.set_width_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_STRETCH))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 20)

        assert_float_approx(root_child0_child0.layout_left, 0)
        assert_float_approx(root_child0_child0.layout_top, 0)
        assert_float_approx(root_child0_child0.layout_width, 200)
        assert_float_approx(root_child0_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_stretch_min_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(100)
        root_child0.set_min_width_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_STRETCH))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 20)

    @pytest.mark.skip(reason="GTEST_SKIP() in C++ source")
    def test_text_stretch_max_width(self):
        config = Config()
        root = Node(config)
        root.position_type = PositionType.Absolute
        root.width = YGValuePoint(200)

        root_child0 = Node(config)
        root_child0.width = YGValuePoint(300)
        root_child0.set_max_width_stretch()
        root.insert_child(root_child0, 0)

        root_child0_child0 = Node(config)
        root_child0_child0.flex_direction = FlexDirection.Row
        root_child0_child0.set_measure_func(make_intrinsic_size_measure(self.TEXT_STRETCH))
        root_child0.insert_child(root_child0_child0, 0)

        root.calculate_layout(float("nan"), float("nan"), Direction.LTR)

        assert_float_approx(root.layout_left, 0)
        assert_float_approx(root.layout_top, 0)
        assert_float_approx(root.layout_width, 200)
        assert_float_approx(root.layout_height, 20)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_top, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 20)

        root.calculate_layout(float("nan"), float("nan"), Direction.RTL)

        assert_float_approx(root_child0.layout_left, 0)
        assert_float_approx(root_child0.layout_width, 200)
        assert_float_approx(root_child0.layout_height, 20)
