from sysd.point import Point

from ..render_output import RenderOutput
from ._connector import Connector


class PolyLine(Connector):
    _SVG = """
    <svg>
        <path d="M{src_x},{src_y}{joints}L{dst_x},{dst_y}" stroke="black" fill="none" />
    </svg>
    """

    def __init__(self, source: Point, dest: Point, *joints: Point):
        super().__init__(source, dest)
        self._joints = joints

    def render(self) -> RenderOutput:
        return self._SVG.format(
            src_x=self._source.x,
            src_y=self._source.y,
            joints=(
                ""
                if not self._joints
                else "".join([f"L{x.x},{x.y}" for x in self._joints])
            ),
            dst_x=self._dest.x,
            dst_y=self._dest.y,
        )
