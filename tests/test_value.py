import pytest
from yoga.value import YGValue
from yoga.enums import Unit


class TestYGValue:
    def test_supports_equality(self):
        assert YGValue(12.5, Unit.Percent) == YGValue(12.5, Unit.Percent)
        assert YGValue(12.5, Unit.Percent) != YGValue(56.7, Unit.Percent)
        assert YGValue(12.5, Unit.Percent) != YGValue(12.5, Unit.Point)
        assert YGValue(12.5, Unit.Percent) != YGValue(12.5, Unit.Auto)
        assert YGValue(12.5, Unit.Percent) != YGValue(12.5, Unit.Undefined)

        assert YGValue(float("nan"), Unit.Undefined) == YGValue(float("nan"), Unit.Undefined)
        assert YGValue(0, Unit.Auto) == YGValue(-1, Unit.Auto)
