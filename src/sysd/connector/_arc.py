import math

import svg

from ..point import Point
from ._connector import Connector


class Arc(Connector):
    _SVG = """
    <svg>
        <path d="{path}" stroke="black" fill="none" />
    </svg>
    """
    _LINE_PATH = "M{ax},{ay}L{bx},{by}"
    _ARC_PATH = "M{ax},{ay}A{rx},{ry},0,0,{clockwise:d},{bx},{by}"

    def __init__(
        self,
        source: Point,
        dest: Point,
        *,
        curvature: float = 0.0,
        clockwise: bool = False
    ):
        super().__init__(source, dest)
        self._curvature = curvature
        self._clockwise = clockwise

    def render(self) -> svg.SVG:
        path_data = [
            svg.M(self._source.x, self._source.y),
            svg.L(self._dest.x, self._dest.y),
        ]
        if self._curvature > 0.0 and self._curvature <= 1.0:
            dx = self._dest.x - self._source.x
            dy = self._dest.y - self._source.y
            min_radius = 0.5 * math.sqrt(dx * dx + dy * dy)
            radius = min_radius / self._curvature
            path_data = [
                svg.M(self._source.x, self._source.y),
                svg.a(
                    radius,
                    radius,
                    0,
                    False,
                    self._clockwise,
                    self._dest.x,
                    self._dest.y,
                ),
            ]
        return svg.SVG(elements=[svg.Path(d=path_data, stroke="black", fill="none")])
