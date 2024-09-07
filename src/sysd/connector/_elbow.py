from sysd.point import Point

from ._polyline import PolyLine


class Elbow(PolyLine):
    def __init__(self, source: Point, dest: Point, flip: bool = False):
        super().__init__(
            source, dest, Point(source.x, dest.y) if flip else Point(dest.x, source.y)
        )
