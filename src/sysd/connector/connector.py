import math

import svg

from sysd.core import Point, Renderable


class Connector(Renderable):
    def __init__(
        self,
        source: Point,
        dest: Point,
        start_arrow: bool = False,
        end_arrow: bool = False,
    ):
        super().__init__()
        self._source = source
        self._dest = dest
        self._start_arrow = start_arrow
        self._end_arrow = end_arrow

    def _render_end_arrow(self, angle_rad: float) -> svg.Path:
        arrow_points = [Point(-8, 4), Point(0, 0), Point(-8, -4)]
        for p in arrow_points:
            out_x = math.cos(angle_rad) * p.x - math.sin(angle_rad) * p.y
            out_y = math.sin(angle_rad) * p.x + math.cos(angle_rad) * p.y
            p.x = out_x + self._dest.x
            p.y = out_y + self._dest.y

        return svg.Path(
            d=[
                svg.M(arrow_points[0].x, arrow_points[0].y),
                *[svg.L(x.x, x.y) for x in arrow_points[1:]],
            ],
            stroke="black",
            fill="none",
        )
