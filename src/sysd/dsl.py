from typing import Optional

from .connector import Elbow, PolyLine
from .constraint import Below, CenterHorizontal, CenterVertical, RightOf
from .core.point import Point
from .core.renderable import Renderable
from .diagram import Diagram
from .symbol import Box, Diamond

_sysd_diagram = Diagram()


def diagram() -> Diagram:
    global _sysd_diagram
    return _sysd_diagram


def start_sysd(title: str):
    global _sysd_diagram
    _sysd_diagram = Diagram(title)


def box(title: str) -> Box:
    global _sysd_diagram
    return _sysd_diagram.add(Box(title))


def diamond() -> Diamond:
    global _sysd_diagram
    return _sysd_diagram.add(Diamond())


def stack(*nodes: Renderable, gutter: float = 0.0):
    for i in range(len(nodes) - 1):
        Below.new(nodes[i + 1], nodes[i], offset=gutter)


def hstack(*nodes: Renderable, gutter: float = 0.0):
    for i in range(len(nodes) - 1):
        RightOf.new(nodes[i + 1], nodes[i], offset=gutter)


def align_center(*nodes: Renderable):
    for i in range(len(nodes) - 1):
        CenterHorizontal.new(nodes[i + 1], nodes[i])


def align_middle(*nodes: Renderable):
    for i in range(len(nodes) - 1):
        CenterVertical.new(nodes[i + 1], nodes[i])


def line(
    source: Point, dest: Point, start_arrow: bool = False, end_arrow: bool = False
):
    global _sysd_diagram
    _sysd_diagram.add(
        PolyLine(source, dest, start_arrow=start_arrow, end_arrow=end_arrow)
    )


def elbow(
    source: Point,
    dest: Point,
    start_arrow: bool = False,
    end_arrow: bool = False,
    flip: bool = False,
    radius: Optional[float] = None,
):
    global _sysd_diagram
    _sysd_diagram.add(Elbow(source, dest, start_arrow, end_arrow, flip, radius))


def add(x: Renderable) -> Renderable:
    global _sysd_diagram
    return _sysd_diagram.add(x)


def end_sysd():
    global _sysd_diagram
    print(_sysd_diagram.render())
