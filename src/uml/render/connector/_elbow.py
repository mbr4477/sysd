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
        dx = self._dest.x - self._source.x
        return Elbow._SVG.format(
            ax=self._source.x + self._source.width * dx / math.fabs(dx),
            ay=self._source.y + self._source.height / 2,
            bx=self._dest.x + self._dest.width / 2,
            by=self._source.y + self._source.height / 2,
            cx=self._dest.x + self._dest.width / 2,
            cy=self._dest.y,
        )
