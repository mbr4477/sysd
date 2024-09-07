from ..point import Point
from ._polyline import PolyLine


class Line(PolyLine):
    def __init__(self, source: Point, dest: Point):
        super().__init__(source, dest)
