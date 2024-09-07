import logging

import svg

from sysd.connectable import Connectable
from sysd.dsl import diagram
from sysd.symbol import Box, Diamond

logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class State(Box):
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
                    r=self._radius * 0.6,
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
