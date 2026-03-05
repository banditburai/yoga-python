import pytest
from yoga import (
    YGValue,
    YGValueAuto,
    YGValuePercent,
    YGValuePoint,
    YGValueUndefined,
    YGValueZero,
    Unit,
    Node,
)


class TestStyleValuePool:
    def test_undefined_at_init(self):
        v = YGValueUndefined
        assert v.unit == Unit.Undefined
        assert v.value == 0.0

    def test_auto_at_init(self):
        v = YGValueAuto
        assert v.unit == Unit.Auto
        assert v.value == 0.0

    def test_store_small_int_points(self):
        v = YGValuePoint(10)
        assert v.unit == Unit.Point
        assert v.value == 10.0

    def test_store_small_negative_int_points(self):
        v = YGValuePoint(-10)
        assert v.unit == Unit.Point
        assert v.value == -10.0

    def test_store_small_int_percent(self):
        v = YGValuePercent(10)
        assert v.unit == Unit.Percent
        assert v.value == 10.0

    def test_store_large_int_percent(self):
        v = YGValuePercent(262144)
        assert v.unit == Unit.Percent
        assert v.value == 262144.0

    def test_store_large_int_after_small_int(self):
        v1 = YGValuePercent(10)
        assert v1.unit == Unit.Percent
        assert v1.value == 10.0

        v2 = YGValuePercent(262144)
        assert v2.unit == Unit.Percent
        assert v2.value == 262144.0

    def test_store_small_int_after_large_int(self):
        v1 = YGValuePercent(262144)
        assert v1.unit == Unit.Percent
        assert v1.value == 262144.0

        v2 = YGValuePercent(10)
        assert v2.unit == Unit.Percent
        assert v2.value == 10.0

    def test_store_small_int_number(self):
        v = YGValuePoint(10.0)
        assert v.unit == Unit.Point
        assert v.value == 10.0

    def test_store_undefined(self):
        v = YGValueUndefined
        assert v.unit == Unit.Undefined

    def test_store_undefined_after_small_int(self):
        v1 = YGValuePoint(10)
        assert v1.unit == Unit.Point
        assert v1.value == 10.0

        v2 = YGValueUndefined
        assert v2.unit == Unit.Undefined

    def test_store_undefined_after_large_int(self):
        v1 = YGValuePoint(262144)
        assert v1.unit == Unit.Point
        assert v1.value == 262144.0

        v2 = YGValueUndefined
        assert v2.unit == Unit.Undefined

    def test_store_keywords(self):
        node = Node()
        node.flex_grow = 1.0

        assert node.flex_grow == 1.0
