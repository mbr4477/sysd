from ..point import Point
from ._polyline import PolyLine


class Line(PolyLine):
    def __init__(
        self,
        source: Point,
        dest: Point,
        start_arrow: bool = False,
        end_arrow: bool = False,
    ):
        super().__init__(source, dest, start_arrow=start_arrow, end_arrow=end_arrow)
