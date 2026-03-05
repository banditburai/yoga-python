import pytest
from yoga import (
    Node,
    Config,
    MeasureMode,
)


class TestNodeCallback:
    def test_has_measure_func_initial(self):
        n = Node()
        assert n.has_measure_func() == False

    def test_has_measure_func_with_measure_fn(self):
        n = Node()

        def measure(node, width, width_mode, height, height_mode):
            return {"width": 0, "height": 0}

        n.set_measure_func(measure)
        assert n.has_measure_func() == True

    def test_measure_with_measure_fn(self):
        n = Node()

        def measure(node, width, width_mode, height, height_mode):
            return {
                "width": width * float(width_mode),
                "height": height / float(height_mode),
            }

        n.set_measure_func(measure)
        w, h = n.measure(23, MeasureMode.Exactly, 24, MeasureMode.AtMost)
        assert w == 23
        assert h == 12

    def test_has_measure_func_after_unset(self):
        n = Node()

        def measure(node, width, width_mode, height, height_mode):
            return {"width": 0, "height": 0}

        n.set_measure_func(measure)
        n.set_measure_func(None)
        assert n.has_measure_func() == False

    def test_has_baseline_func_initial(self):
        n = Node()
        assert n.has_baseline_func() == False

    def test_has_baseline_func_with_baseline_fn(self):
        n = Node()

        def baseline(node, width, height):
            return 0.0

        n.set_baseline_func(baseline)
        assert n.has_baseline_func() == True

    def test_baseline_with_baseline_fn(self):
        n = Node()

        def baseline(node, width, height):
            return width + height

        n.set_baseline_func(baseline)
        assert n.baseline(1.25, 2.5) == 3.75

    def test_has_baseline_func_after_unset(self):
        n = Node()

        def baseline(node, width, height):
            return 0.0

        n.set_baseline_func(baseline)
        n.set_baseline_func(None)
        assert n.has_baseline_func() == False
