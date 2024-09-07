from .connector import Elbow, Line
from .constraint import Below, CenterHorizontal, CenterVertical, RightOf
from .diagram import Diagram
from .point import Point
from .renderable import Renderable
from .symbol import Box, Diamond

sysd_diagram = Diagram()


def diagram() -> Diagram:
    global sysd_diagram
    return sysd_diagram


def startd(title: str):
    global sysd_diagram
    sysd_diagram = Diagram(title)


def box(title: str) -> Box:
    global sysd_diagram
    return sysd_diagram.add(Box(title))


def diamond() -> Diamond:
    global sysd_diagram
    return sysd_diagram.add(Diamond())


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
    global sysd_diagram
    sysd_diagram.add(Line(source, dest, start_arrow, end_arrow))


def elbow(
    source: Point,
    dest: Point,
    start_arrow: bool = False,
    end_arrow: bool = False,
    flip: bool = False,
):
    global sysd_diagram
    sysd_diagram.add(Elbow(source, dest, start_arrow, end_arrow, flip))


def endd():
    global sysd_diagram
    print(sysd_diagram.render())
