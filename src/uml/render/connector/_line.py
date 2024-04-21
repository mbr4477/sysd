import math

from uml.render.render_output import RenderOutput

from ._connector import Connector


class Line(Connector):
    _SVG = """
    <svg>
        <path d="M{sx},{sy}L{ex},{ey}" stroke="black" />
    </svg>
    """

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
        return Line._SVG.format(sx=sx, sy=sy, ex=ex, ey=ey)
