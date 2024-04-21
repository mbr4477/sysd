import math

from uml.render.render_output import RenderOutput

from ._connector import Connector


class Elbow(Connector):
    _SVG = """
    <svg>
        <path d="M{ax},{ay}L{bx},{by}L{cx},{cy}" stroke="black" fill="none"/>
    </svg>
    """

    def render(self) -> RenderOutput:
        start_x = self._source.x + self._source.width / 2
        start_y = self._source.y + self._source.height / 2
        end_x = self._dest.x + self._dest.width / 2
        end_y = self._dest.y + self._dest.height / 2
        dx = end_x - start_x
        dy = end_y - start_y
        start_x += 0.5 * self._source.width * dx / math.fabs(dx)
        end_y -= 0.5 * self._dest.height * dy / math.fabs(dy)
        return Elbow._SVG.format(
            ax=start_x, ay=start_y, bx=end_x, by=start_y, cx=end_x, cy=end_y
        )
