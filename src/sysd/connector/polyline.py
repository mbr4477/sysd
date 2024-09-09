import math
from typing import List, Optional

import svg

from sysd.core import Point

from .connector import Connector


class PolyLine(Connector):
    def __init__(
        self,
        source: Point,
        dest: Point,
        *joints: Point,
        start_arrow: bool = False,
        end_arrow: bool = False,
        radius: Optional[float] = None,
    ):
        super().__init__(source, dest, start_arrow, end_arrow)
        self._joints = joints
        self._radius = radius

    @property
    def points(self) -> List[Point]:
        return [self._source] + list(self._joints) + [self._dest]

    def render(self) -> svg.SVG:
        arrows: List[svg.Path] = []
        if self._end_arrow:
            prev_point = self._joints[-1] if self._joints else self._source
            angle_rad = math.atan2(
                self._dest.y - prev_point.y, self._dest.x - prev_point.x
            )
            arrows.append(self._render_end_arrow(angle_rad))

        path = []
        if self._joints and self._radius:
            path.append(svg.M(self._source.x, self._source.y))
            for start, middle, end in zip(
                [self._source] + list(self._joints[:-1]),
                self._joints,
                list(self._joints[1:]) + [self._dest],
            ):
                in_dx = middle.x - start.x
                in_dy = middle.y - start.y
                out_dx = end.x - middle.x
                out_dy = end.y - middle.y
                seg_a_len = math.sqrt(in_dx**2 + in_dy**2)
                seg_b_len = math.sqrt(out_dx**2 + out_dy**2)
                dot_prod = (start.x - middle.x) * (end.x - middle.x) + (
                    start.y - middle.y
                ) * (end.y - middle.y)
                angle_rad = math.acos(dot_prod / (seg_a_len * seg_b_len))
                sector_rad = math.pi - angle_rad
                buffer_dist = math.tan(sector_rad / 2) * self._radius
                in_x = middle.x - in_dx / seg_a_len * buffer_dist
                in_y = middle.y - in_dy / seg_a_len * buffer_dist
                out_x = middle.x + out_dx / seg_b_len * buffer_dist
                out_y = middle.y + out_dy / seg_b_len * buffer_dist
                path += [
                    svg.L(in_x, in_y),
                    svg.a(
                        self._radius,
                        self._radius,
                        0.0,
                        False,
                        in_dx > in_dy,
                        out_x - in_x,
                        out_y - in_y,
                    ),
                ]
            path.append(svg.L(self._dest.x, self._dest.y))
        else:
            path = [
                svg.M(self._source.x, self._source.y),
                *[svg.L(x.x, x.y) for x in self._joints],
                svg.L(self._dest.x, self._dest.y),
            ]

        return svg.SVG(
            elements=[
                svg.Path(
                    stroke="black",
                    fill="none",
                    d=path,
                ),
                *arrows,
            ],
        )
