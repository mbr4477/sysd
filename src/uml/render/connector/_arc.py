import math

from uml.render.render_output import RenderOutput

from ..bounding_box import BoundingBox
from ._connector import Connector


class Arc(Connector):
    _SVG = """
    <svg>
        <path d="{path}" stroke="black" fill="none" />
    </svg>
    """
    _LINE_PATH = "M{sx},{sy}L{ex},{ey}"
    _ARC_PATH = "M{sx},{sy}A{rx},{ry},0,0,{clockwise:d},{ex},{ey}"

    def __init__(
        self,
        source: BoundingBox,
        dest: BoundingBox,
        *,
        curvature: float = 0.0,
        clockwise: bool = False
    ):
        super().__init__(source, dest)
        self._curvature = curvature
        self._clockwise = clockwise

    def render(self) -> RenderOutput:
        start_x = self._source.x + self._source.width / 2
        start_y = self._source.y + self._source.height / 2
        end_x = self._dest.x + self._dest.width / 2
        end_y = self._dest.y + self._dest.height / 2
        dx = end_x - start_x
        dy = end_y - start_y
        start_t = 0.5 * min(
            self._source.width / math.fabs(dx) if dx != 0 else math.inf,
            self._source.height / math.fabs(dy) if dy != 0 else math.inf,
        )
        end_t = 0.5 * min(
            self._dest.width / math.fabs(dx) if dx != 0 else math.inf,
            self._dest.height / math.fabs(dy) if dy != 0 else math.inf,
        )
        sx = start_x + start_t * dx
        sy = start_y + start_t * dy
        ex = start_x + (1 - end_t) * dx
        ey = start_y + (1 - end_t) * dy
        path = Arc._LINE_PATH.format(sx=sx, sy=sy, ex=ex, ey=ey)
        if self._curvature > 0.0 and self._curvature <= 1.0:
            min_t = 1 - (start_t + end_t)
            min_dx = min_t * dx
            min_dy = min_t * dy
            min_radius = 0.5 * math.sqrt(min_dx * min_dx + min_dy * min_dy)
            radius = min_radius / self._curvature
            path = Arc._ARC_PATH.format(
                sx=sx,
                sy=sy,
                ex=ex,
                ey=ey,
                rx=radius,
                ry=radius,
                clockwise=self._clockwise,
            )
        return Arc._SVG.format(path=path)
