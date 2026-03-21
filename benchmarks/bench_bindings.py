"""Focused microbenchmarks for yoga-python binding hot paths.

Run with:
  uv run python benchmarks/bench_bindings.py
"""

from __future__ import annotations

import statistics
import time

import yoga


def _bench(fn, *, iterations: int, warmup: int) -> dict[str, int]:
    for _ in range(warmup):
        fn()
    times: list[int] = []
    for _ in range(iterations):
        start = time.perf_counter_ns()
        fn()
        times.append(time.perf_counter_ns() - start)
    times.sort()
    return {
        "median_ns": times[len(times) // 2],
        "mean_ns": int(statistics.mean(times)),
    }


def main() -> None:
    node = yoga.Node()
    vals = {
        "width": 80,
        "height": 24,
        "flex_grow": 1.0,
        "flex_shrink": 1.0,
        "flex_direction": "row",
        "justify_content": "space-between",
        "align_items": "center",
        "overflow": "hidden",
        "position_type": "relative",
        "padding_top": 1.0,
        "padding_right": 2.0,
        "padding_bottom": 1.0,
        "padding_left": 2.0,
    }

    def fast_same() -> None:
        yoga.configure_node_fast(node, **vals)

    def fast_toggle() -> None:
        fast_toggle.state = not fast_toggle.state
        yoga.configure_node_fast(node, **(vals if fast_toggle.state else {**vals, "width": 81}))

    fast_toggle.state = False

    def python_setters_same() -> None:
        node.width = 80
        node.height = 24
        node.flex_grow = 1.0
        node.flex_shrink = 1.0
        node.flex_direction = yoga.FlexDirection.Row
        node.justify_content = yoga.Justify.SpaceBetween
        node.align_items = yoga.Align.Center
        node.overflow = yoga.Overflow.Hidden
        node.position_type = yoga.PositionType.Relative
        node.set_padding(yoga.Edge.Top, 1.0)
        node.set_padding(yoga.Edge.Right, 2.0)
        node.set_padding(yoga.Edge.Bottom, 1.0)
        node.set_padding(yoga.Edge.Left, 2.0)

    def python_setters_toggle() -> None:
        python_setters_toggle.state = not python_setters_toggle.state
        node.width = 80 if python_setters_toggle.state else 81
        python_setters_same()

    python_setters_toggle.state = False

    parent = yoga.Node()
    children = [yoga.Node() for _ in range(500)]
    for child in children:
        child.width = 1

    def set_children_batch() -> None:
        parent.set_children(children)

    def rebuild_insertions() -> None:
        parent.remove_all_children()
        for i, child in enumerate(children):
            parent.insert_child(child, i)

    cases = [
        ("configure_node_fast same", fast_same, 5000, 200),
        ("configure_node_fast toggled", fast_toggle, 5000, 200),
        ("python setters same", python_setters_same, 5000, 200),
        ("python setters toggled", python_setters_toggle, 5000, 200),
        ("set_children(500)", set_children_batch, 200, 20),
        ("remove_all+insert 500", rebuild_insertions, 200, 20),
    ]
    for label, fn, iterations, warmup in cases:
        result = _bench(fn, iterations=iterations, warmup=warmup)
        print(f"{label:<28} median={result['median_ns']:>8,}ns mean={result['mean_ns']:>8,}ns")

    parent.free_recursive()
    node.free()


if __name__ == "__main__":
    main()
