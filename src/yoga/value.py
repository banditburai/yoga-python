import math
from dataclasses import dataclass

from yoga.enums import Unit


YGUndefined: float = float("nan")


def YGFloatIsUndefined(value: float) -> bool:
    return math.isnan(value)


@dataclass
class YGValue:
    value: float
    unit: Unit

    def __post_init__(self):
        if isinstance(self.unit, int):
            self.unit = Unit(self.unit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, YGValue):
            return NotImplemented
        if self.unit != other.unit:
            return False
        if self.unit in (
            Unit.Undefined,
            Unit.Auto,
            Unit.FitContent,
            Unit.MaxContent,
            Unit.Stretch,
        ):
            return True
        if self.unit in (Unit.Point, Unit.Percent):
            return self.value == other.value
        return False

    def __neg__(self) -> "YGValue":
        return YGValue(-self.value, self.unit)


YGValueAuto = YGValue(0, Unit.Auto)
YGValueUndefined = YGValue(0, Unit.Undefined)
YGValueZero = YGValue(0, Unit.Point)


def YGValuePoint(value: float) -> YGValue:
    return YGValue(value, Unit.Point)


def YGValuePercent(value: float) -> YGValue:
    return YGValue(value, Unit.Percent)
