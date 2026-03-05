import math
import pytest
from yoga import YGFloatIsUndefined


class FloatOptional:
    def __init__(self, value):
        if value is None or (isinstance(value, float) and math.isnan(value)):
            self._value = float("nan")
        else:
            self._value = float(value)

    @staticmethod
    def undefined():
        return FloatOptional(float("nan"))

    def unwrap(self):
        return self._value

    def isUndefined(self):
        return YGFloatIsUndefined(self._value)

    def __eq__(self, other):
        if isinstance(other, FloatOptional):
            if self.isUndefined() and other.isUndefined():
                return True
            if self.isUndefined() or other.isUndefined():
                return False
            return self._value == other._value
        elif isinstance(other, float):
            if self.isUndefined() and YGFloatIsUndefined(other):
                return True
            if self.isUndefined() or YGFloatIsUndefined(other):
                return False
            return self._value == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __gt__(self, other):
        if isinstance(other, FloatOptional):
            if self.isUndefined() or other.isUndefined():
                return False
            return self._value > other._value
        elif isinstance(other, float):
            if self.isUndefined() or YGFloatIsUndefined(other):
                return False
            return self._value > other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, FloatOptional):
            if self.isUndefined() or other.isUndefined():
                return False
            return self._value < other._value
        elif isinstance(other, float):
            if self.isUndefined() or YGFloatIsUndefined(other):
                return False
            return self._value < other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, FloatOptional):
            if self.isUndefined() and other.isUndefined():
                return True
            if self.isUndefined() or other.isUndefined():
                return False
            return self._value >= other._value
        elif isinstance(other, float):
            if self.isUndefined() and YGFloatIsUndefined(other):
                return True
            if self.isUndefined() or YGFloatIsUndefined(other):
                return False
            return self._value >= other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, FloatOptional):
            if self.isUndefined() and other.isUndefined():
                return True
            if self.isUndefined() or other.isUndefined():
                return False
            return self._value <= other._value
        elif isinstance(other, float):
            if self.isUndefined() and YGFloatIsUndefined(other):
                return True
            if self.isUndefined() or YGFloatIsUndefined(other):
                return False
            return self._value <= other
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, FloatOptional):
            if self.isUndefined() or other.isUndefined():
                return FloatOptional.undefined()
            return FloatOptional(self._value + other._value)
        elif isinstance(other, float):
            if self.isUndefined() or YGFloatIsUndefined(other):
                return FloatOptional.undefined()
            return FloatOptional(self._value + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)


def maxOrDefined(a: FloatOptional, b: FloatOptional) -> FloatOptional:
    if a.isUndefined():
        return b
    if b.isUndefined():
        return a
    if a >= b:
        return a
    return b


empty = FloatOptional.undefined()
zero = FloatOptional(0.0)
one = FloatOptional(1.0)
positive = FloatOptional(1234.5)
negative = FloatOptional(-9876.5)


class TestFloatOptional:
    def test_value(self):
        assert YGFloatIsUndefined(empty.unwrap())
        assert zero.unwrap() == 0.0
        assert one.unwrap() == 1.0
        assert positive.unwrap() == 1234.5
        assert negative.unwrap() == -9876.5

        assert empty.isUndefined()
        assert not zero.isUndefined()
        assert not one.isUndefined()
        assert not positive.isUndefined()
        assert not negative.isUndefined()

    def test_equality(self):
        assert empty == empty
        assert empty == float("nan")
        assert not (empty == zero)
        assert not (empty == negative)
        assert not (empty == 12.3)

        assert zero == zero
        assert zero == 0.0
        assert not (zero == positive)
        assert not (zero == -5555.5)

        assert one == one
        assert one == 1.0
        assert not (one == positive)

        assert positive == positive
        assert positive == positive.unwrap()
        assert not (positive == one)

        assert negative == negative
        assert negative == negative.unwrap()
        assert not (negative == zero)

    def test_inequality(self):
        assert not (empty != empty)
        assert not (empty != float("nan"))
        assert empty != zero
        assert empty != negative
        assert empty != 12.3

        assert not (zero != zero)
        assert not (zero != 0.0)
        assert zero != positive
        assert zero != -5555.5

        assert not (one != one)
        assert not (one != 1.0)
        assert one != positive

        assert not (positive != positive)
        assert not (positive != positive.unwrap())
        assert positive != one

        assert not (negative != negative)
        assert not (negative != negative.unwrap())
        assert negative != zero

    def test_greater_than_with_undefined(self):
        assert not (empty > empty)
        assert not (empty > zero)
        assert not (empty > one)
        assert not (empty > positive)
        assert not (empty > negative)
        assert not (zero > empty)
        assert not (one > empty)
        assert not (positive > empty)
        assert not (negative > empty)

    def test_greater_than(self):
        assert zero > negative
        assert not (zero > zero)
        assert not (zero > positive)
        assert not (zero > one)

        assert one > negative
        assert one > zero
        assert not (one > positive)

        assert negative > FloatOptional(-float("inf"))

    def test_less_than_with_undefined(self):
        assert not (empty < empty)
        assert not (zero < empty)
        assert not (one < empty)
        assert not (positive < empty)
        assert not (negative < empty)
        assert not (empty < zero)
        assert not (empty < one)
        assert not (empty < positive)
        assert not (empty < negative)

    def test_less_than(self):
        assert negative < zero
        assert not (zero < zero)
        assert not (positive < zero)
        assert not (one < zero)

        assert negative < one
        assert zero < one
        assert not (positive < one)

        assert FloatOptional(-float("inf")) < negative

    def test_greater_than_equals_with_undefined(self):
        assert empty >= empty
        assert not (empty >= zero)
        assert not (empty >= one)
        assert not (empty >= positive)
        assert not (empty >= negative)
        assert not (zero >= empty)
        assert not (one >= empty)
        assert not (positive >= empty)
        assert not (negative >= empty)

    def test_greater_than_equals(self):
        assert zero >= negative
        assert zero >= zero
        assert not (zero >= positive)
        assert not (zero >= one)

        assert one >= negative
        assert one >= zero
        assert not (one >= positive)

        assert negative >= FloatOptional(-float("inf"))

    def test_less_than_equals_with_undefined(self):
        assert empty <= empty
        assert not (zero <= empty)
        assert not (one <= empty)
        assert not (positive <= empty)
        assert not (negative <= empty)
        assert not (empty <= zero)
        assert not (empty <= one)
        assert not (empty <= positive)
        assert not (empty <= negative)

    def test_less_than_equals(self):
        assert negative <= zero
        assert zero <= zero
        assert not (positive <= zero)
        assert not (one <= zero)

        assert negative <= one
        assert zero <= one
        assert not (positive <= one)

        assert FloatOptional(-float("inf")) <= negative

    def test_addition(self):
        assert zero + one == one
        assert negative + positive == FloatOptional(negative.unwrap() + positive.unwrap())
        assert empty + zero == empty
        assert empty + empty == empty
        assert negative + empty == empty

    def test_max_or_defined(self):
        assert maxOrDefined(empty, empty) == empty
        assert maxOrDefined(empty, positive) == positive
        assert maxOrDefined(negative, empty) == negative
        assert maxOrDefined(negative, FloatOptional(-float("inf"))) == negative
        assert maxOrDefined(FloatOptional(1.0), FloatOptional(1.125)) == FloatOptional(1.125)

    def test_unwrap(self):
        assert YGFloatIsUndefined(empty.unwrap())
        assert zero.unwrap() == 0.0
        assert FloatOptional(123456.78).unwrap() == 123456.78
