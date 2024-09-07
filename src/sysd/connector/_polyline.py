import math
from typing import List

import svg

from sysd.point import Point

from ._connector import Connector


class PolyLine(Connector):
    def __init__(
        self,
        source: Point,
        dest: Point,
        *joints: Point,
        start_arrow: bool = False,
        end_arrow: bool = False
    ):
        super().__init__(source, dest, start_arrow, end_arrow)
        self._joints = joints

    def render(self) -> svg.SVG:
        arrows: List[svg.Path] = []
        if self._end_arrow:
            prev_point = self._joints[-1] if self._joints else self._source
            angle_rad = math.atan2(
                self._dest.y - prev_point.y, self._dest.x - prev_point.x
            )
            arrows.append(self._render_end_arrow(angle_rad))

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
                ),
                *arrows,
            ],
        )
