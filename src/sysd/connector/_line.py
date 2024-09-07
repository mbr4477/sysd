from ..render_output import RenderOutput
from ._connector import Connector


class Line(Connector):
    _SVG = """
    <svg>
        <path d="M{src_x},{src_y}L{dst_x},{dst_y}" stroke="black" />
    </svg>
    """

    def render(self) -> RenderOutput:
        return Line._SVG.format(
            src_x=self._source.x,
            src_y=self._source.y,
            dst_x=self._dest.x,
            dst_y=self._dest.y,
        )
