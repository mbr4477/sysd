from typing import Optional

from sysd.core import Point

from .polyline import PolyLine


class Elbow(PolyLine):
    def __init__(
        self,
        source: Point,
        dest: Point,
        start_arrow: bool = False,
        end_arrow: bool = False,
        flip: bool = False,
        radius: Optional[float] = None,
    ):
        super().__init__(
            source,
            dest,
            Point(source.x, dest.y) if flip else Point(dest.x, source.y),
            start_arrow=start_arrow,
            end_arrow=end_arrow,
            radius=radius,
        )
