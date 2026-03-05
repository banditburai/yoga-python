from enum import IntEnum

YGUndefined: float = float("nan")


class Direction(IntEnum):
    Inherit = 0
    LTR = 1
    RTL = 2


class Unit(IntEnum):
    Undefined = 0
    Point = 1
    Percent = 2
    Auto = 3
    MaxContent = 4
    FitContent = 5
    Stretch = 6


class FlexDirection(IntEnum):
    Column = 0
    ColumnReverse = 1
    Row = 2
    RowReverse = 3


class Justify(IntEnum):
    FlexStart = 0
    Center = 1
    FlexEnd = 2
    SpaceBetween = 3
    SpaceAround = 4
    SpaceEvenly = 5


class Overflow(IntEnum):
    Visible = 0
    Hidden = 1
    Scroll = 2


class Align(IntEnum):
    Auto = 0
    FlexStart = 1
    Center = 2
    FlexEnd = 3
    Stretch = 4
    Baseline = 5
    SpaceBetween = 6
    SpaceAround = 7
    SpaceEvenly = 8


class PositionType(IntEnum):
    Static = 0
    Relative = 1
    Absolute = 2


class Display(IntEnum):
    Flex = 0
    None_ = 1
    Contents = 2


class Wrap(IntEnum):
    NoWrap = 0
    Wrap = 1
    WrapReverse = 2


class BoxSizing(IntEnum):
    BorderBox = 0
    ContentBox = 1


class MeasureMode(IntEnum):
    Undefined = 0
    Exactly = 1
    AtMost = 2


class Dimension(IntEnum):
    Width = 0
    Height = 1


class Edge(IntEnum):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
    Start = 4
    End = 5
    Horizontal = 6
    Vertical = 7
    All = 8


class NodeType(IntEnum):
    Default = 0
    Text = 1


class LogLevel(IntEnum):
    Error = 0
    Warn = 1
    Info = 2
    Debug = 3
    Verbose = 4
    Fatal = 5


class ExperimentalFeature(IntEnum):
    WebFlexBasis = 0


class Gutter(IntEnum):
    Column = 0
    Row = 1
    All = 2


class Errata(IntEnum):
    None_ = 0
    StretchFlexBasis = 1
    AbsolutePositionWithoutInsetsExcludesPadding = 2
    AbsolutePercentAgainstInnerSize = 4
    All = 2147483647
    Classic = 2147483646
