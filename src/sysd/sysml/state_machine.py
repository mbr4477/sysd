from __future__ import annotations

import svg

from sysd.core import Connectable, Point
from sysd.dsl import diagram, line
from sysd.symbol import Box, Diamond


class Transition:
    def __init__(self, source_port: int, dest_port: int):
        self._source = None
        self._dest = None
        self._source_port = source_port
        self._dest_port = dest_port

    def __rsub__(self, other) -> Transition:
        if not isinstance(other, Connectable):
            raise ValueError

        self._source = other
        return self

    def __sub__(self, other) -> Transition:
        if not isinstance(other, Connectable):
            raise ValueError

        self._dest = other
        if self._dest is not None and self._source is not None:
            line(
                self._source.ports[self._source_port],
                self._dest.ports[self._dest_port],
                end_arrow=True,
            )
        return self

    def __gt__(self, other) -> Transition:
        if not isinstance(other, Connectable):
            raise ValueError

        self._dest = other
        if self._dest is not None and self._source is not None:
            line(
                self._source.ports[self._source_port],
                self._dest.ports[self._dest_port],
                end_arrow=True,
            )
        return self


class State(Box):
    local_ports = Box.local_ports + [
        Point(0.25, 0.0),
        Point(0.75, 0.0),
        Point(0.75, 1.0),
        Point(0.25, 1.0),
    ]

    def __init__(self, title: str):
        super().__init__(title)
        self.bounds.size.width = 100
        self.label.bounds.origin.x = 50

    def render(self) -> svg.SVG:
        out = super().render()
        assert out.elements and isinstance(out.elements[0], svg.Rect)
        rect = out.elements[0]
        rect.rx = 10
        return out


class InitialState(Connectable):
    def __init__(self):
        super().__init__()
        self._radius = 5
        self.bounds.size.width = 2 * self._radius
        self.bounds.size.height = 2 * self._radius

    def render(self) -> svg.SVG:
        return svg.SVG(
            x=self.bounds.origin.x,
            y=self.bounds.origin.y,
            overflow="visible",
            elements=[
                svg.Circle(
                    cx=self._radius, cy=self._radius, r=self._radius, fill="black"
                )
            ],
        )


class FinalState(Connectable):
    local_ports = [
        Point(0.5, 0.0),
        Point(0.8535, 0.1464),
        Point(1.0, 0.5),
        Point(0.8535, 0.8535),
        Point(0.5, 1.0),
        Point(0.1464, 0.8535),
        Point(0.0, 0.5),
        Point(0.1464, 0.1464),
    ]

    def __init__(self):
        super().__init__()
        self._radius = 5
        self.bounds.size.width = 2 * self._radius
        self.bounds.size.height = 2 * self._radius

    def render(self) -> svg.SVG:
        return svg.SVG(
            x=self.bounds.origin.x,
            y=self.bounds.origin.y,
            overflow="visible",
            elements=[
                svg.Circle(
                    cx=self._radius,
                    cy=self._radius,
                    r=self._radius,
                    fill="none",
                    stroke="black",
                ),
                svg.Circle(
                    cx=self._radius,
                    cy=self._radius,
                    r=self._radius * 0.5,
                    fill="black",
                    stroke="none",
                ),
            ],
        )


class Choice(Diamond):
    def __init__(self):
        super().__init__()
        self.bounds.size.width = 10
        self.bounds.size.height = 10


def state(title: str) -> State:
    return diagram().add(State(title))


def initial_state() -> InitialState:
    return diagram().add(InitialState())


def final_state() -> FinalState:
    return diagram().add(FinalState())


def choice() -> Choice:
    return diagram().add(Choice())
