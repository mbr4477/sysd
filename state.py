import logging
import re

from sysd.connectable import Connectable
from sysd.dsl import diagram
from sysd.render_output import RenderOutput
from sysd.symbol import Box, Diamond

logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class State(Box):
    def render(self) -> RenderOutput:
        out = super().render()
        result = re.search(r"<rect((?:.|\n)*)\/>", out, re.MULTILINE)
        if result is not None:
            out = (
                out[: result.start()]
                + f'<rect {result.groups(1)[0]} rx="10" />'
                + out[result.end() :]
            )
        return out


class InitialState(Connectable):
    def __init__(self):
        super().__init__()
        self._radius = 5
        self.bounds.size.width = 2 * self._radius
        self.bounds.size.height = 2 * self._radius

    def render(self) -> RenderOutput:
        return (
            "<svg"
            f' x="{self.bounds.origin.x}"'
            f' y="{self.bounds.origin.y}"'
            ' overflow="visible">'
            f' <circle cx="{self._radius}" cy="{self._radius}" r="{self._radius}" fill="black"/>'
            "</svg>"
        )


class FinalState(Connectable):
    def __init__(self):
        super().__init__()
        self._radius = 5
        self.bounds.size.width = 2 * self._radius
        self.bounds.size.height = 2 * self._radius

    def render(self) -> RenderOutput:
        return (
            "<svg"
            f' x="{self.bounds.origin.x}"'
            f' y="{self.bounds.origin.y}"'
            ' overflow="visible">'
            f' <circle cx="{self._radius}" cy="{self._radius}" r="{self._radius}" fill="none" stroke="black" />'
            f' <circle cx="{self._radius}" cy="{self._radius}" r="{self._radius*0.6}" fill="black"/>'
            "</svg>"
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
