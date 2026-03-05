# yoga-python

Python bindings for [Facebook's Yoga](https://github.com/facebook/yoga) layout engine — a cross-platform implementation of [CSS Flexbox](https://www.w3.org/TR/css-flexbox-1/).

Yoga computes a layout tree of nodes with flexbox styles and outputs pixel-perfect positions. This package wraps the full C++ engine via [pybind11](https://github.com/pybind/pybind11), giving you the same layout behavior you get in React Native, Litho, and other Yoga-backed frameworks — directly from Python.

## Installation

```bash
pip install yoga-python
```

Building from source requires a C++20 compiler, CMake 3.15+, and pybind11:

```bash
pip install scikit-build-core pybind11
pip install .
```

## Quick start

```python
from yoga import (
    Node, Config, Direction, FlexDirection, Justify,
    Align, Edge, YGValuePoint, YGValuePercent,
)

root = Node()
root.flex_direction = FlexDirection.Row
root.width = YGValuePoint(300)
root.height = YGValuePoint(200)
root.set_padding(Edge.All, 10)

child_a = Node()
child_a.flex_grow = 1
child_a.set_margin(Edge.Right, 10)
root.insert_child(child_a, 0)

child_b = Node()
child_b.flex_grow = 2
root.insert_child(child_b, 1)

root.calculate_layout(300, 200, Direction.LTR)

print(f"child_a: {child_a.layout_left}, {child_a.layout_top}, "
      f"{child_a.layout_width}x{child_a.layout_height}")
# child_a: 10.0, 10.0, 86.66666412353516x180.0

print(f"child_b: {child_b.layout_left}, {child_b.layout_top}, "
      f"{child_b.layout_width}x{child_b.layout_height}")
# child_b: 106.66666412353516, 10.0, 183.33334350585938x180.0
```

## API overview

### Node

The primary object. Create nodes, configure their styles, build a tree, then call `calculate_layout`.

```python
node = Node()           # default config
node = Node(config)     # with explicit config
```

**Style properties** (set directly as attributes):

| Property | Type | Example |
|---|---|---|
| `flex_direction` | `FlexDirection` | `node.flex_direction = FlexDirection.Row` |
| `justify_content` | `Justify` | `node.justify_content = Justify.Center` |
| `align_items` | `Align` | `node.align_items = Align.Stretch` |
| `align_self` | `Align` | `node.align_self = Align.FlexEnd` |
| `align_content` | `Align` | `node.align_content = Align.SpaceBetween` |
| `flex_wrap` | `Wrap` | `node.flex_wrap = Wrap.Wrap` |
| `overflow` | `Overflow` | `node.overflow = Overflow.Hidden` |
| `display` | `Display` | `node.display = Display.Flex` |
| `position_type` | `PositionType` | `node.position_type = PositionType.Absolute` |
| `flex_grow` | `float` | `node.flex_grow = 1.0` |
| `flex_shrink` | `float` | `node.flex_shrink = 0.0` |
| `flex_basis` | `YGValue` | `node.flex_basis = YGValuePoint(100)` |
| `width` / `height` | `YGValue` | `node.width = YGValuePercent(50)` |
| `min_width` / `max_width` | `YGValue` | `node.min_width = YGValuePoint(80)` |
| `min_height` / `max_height` | `YGValue` | `node.max_height = YGValuePoint(400)` |
| `aspect_ratio` | `float` | `node.aspect_ratio = 16 / 9` |
| `box_sizing` | `BoxSizing` | `node.box_sizing = BoxSizing.ContentBox` |
| `direction` | `Direction` | `node.direction = Direction.LTR` |

**Edge-based properties** (margin, padding, border, position):

```python
node.set_margin(Edge.Left, 10)           # points
node.set_margin(Edge.Top, YGValuePercent(5))  # percent
node.set_padding(Edge.All, 20)
node.set_border(Edge.Bottom, 1)
node.set_position(Edge.Left, YGValuePoint(50))
```

**Tree manipulation:**

```python
node.insert_child(child, index)
node.remove_child(child)
node.remove_all_children()
node.set_children([child_a, child_b])
node.child_count                     # int
node.get_child(index)                # Node
```

**Layout:**

```python
node.calculate_layout(width, height, Direction.LTR)

node.layout_left       # float
node.layout_top        # float
node.layout_width      # float
node.layout_height     # float
node.layout_direction  # Direction
node.layout_margin(Edge.Left)   # float
node.layout_padding(Edge.Top)   # float
node.layout_border(Edge.Right)  # float
```

**Measure functions** for leaf nodes with custom content sizing:

```python
def measure(node, width, width_mode, height, height_mode):
    return {"width": 100, "height": 50}

node.set_measure_func(measure)
```

**Baseline functions** for custom baseline alignment:

```python
def baseline(node, width, height):
    return height * 0.8

node.set_baseline_func(baseline)
```

### Config

```python
config = Config()
config.use_web_defaults = True
config.point_scale_factor = 2.0
config.errata = Errata.StretchFlexBasis
```

### Values

```python
YGValuePoint(100)       # 100px
YGValuePercent(50)      # 50%
YGValueAuto             # auto
YGValueUndefined        # undefined
```

## Enums

All Yoga enums are available as Python `IntEnum` types:

`Direction`, `FlexDirection`, `Justify`, `Align`, `PositionType`, `Wrap`, `Overflow`, `Display`, `Edge`, `Unit`, `MeasureMode`, `Dimension`, `BoxSizing`, `Gutter`, `Errata`, `NodeType`, `LogLevel`, `ExperimentalFeature`

## Development

```bash
git clone https://github.com/banditburai/yoga-python.git
cd yoga-python
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Lint
ruff check
ruff format --check
```

## Test coverage

The test suite is a 1:1 port of the [Yoga C++ test suite](https://github.com/facebook/yoga/tree/main/tests) — 822 tests covering all layout modes, edge cases, and behaviors. Tests that the C++ suite itself skips (`GTEST_SKIP`) are also skipped in Python.

## License

MIT — same as [Yoga](https://github.com/facebook/yoga/blob/main/LICENSE).
