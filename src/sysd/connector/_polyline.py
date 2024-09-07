import svg

from sysd.point import Point

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

    def render(self) -> svg.SVG:
        return svg.SVG(
            elements=[
                svg.Path(
                    stroke="black",
                    fill="none",
                    d=[
                        svg.M(self._source.x, self._source.y),
                        *[svg.L(x.x, x.y) for x in self._joints],
                        svg.L(self._dest.x, self._dest.y),
                    ],
                )
            ],
        )
