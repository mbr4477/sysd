from ..point import Point
from ..renderable import Renderable


class Connector(Renderable):
    def __init__(self, source: Point, dest: Point):
        super().__init__()
        self._source = source
        self._dest = dest
