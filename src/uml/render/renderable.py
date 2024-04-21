from __future__ import annotations

import abc

from .render_output import RenderOutput


class Renderable(abc.ABC):
    def __init__(self):
        super().__init__()
        self.x = 0.0
        self.y = 0.0
        self._width = 0.0
        self._height = 0.0

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def render(self) -> RenderOutput: ...
