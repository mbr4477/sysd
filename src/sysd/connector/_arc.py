
import math

from ..point import Point
from ..render_output import RenderOutput
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

    def render(self) -> RenderOutput:
        params = dict(
            ax=self._source.x, ay=self._source.y, bx=self._dest.x, by=self._dest.y
        )
        path = Arc._LINE_PATH.format(**params)
        if self._curvature > 0.0 and self._curvature <= 1.0:
            dx = self._dest.x - self._source.x
            dy = self._dest.y - self._source.y
            min_radius = 0.5 * math.sqrt(dx * dx + dy * dy)
            radius = min_radius / self._curvature
            path = Arc._ARC_PATH.format(
                **params,
                rx=radius,
                ry=radius,
                clockwise=self._clockwise,
            )
        return Arc._SVG.format(path=path)
