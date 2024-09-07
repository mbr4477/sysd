from typing import List, Sequence

from .point import Point
from .renderable import Renderable


class Connectable(Renderable):
    local_ports: Sequence[Point] = [
        Point(0.5, 0.0),
        Point(1.0, 0.5),
        Point(0.5, 1.0),
        Point(0.0, 0.5),
    ]

    @property
    def ports(self) -> List[Point]:
        w = self.bounds.size.width
        h = self.bounds.size.height
        x = self.bounds.origin.x
        y = self.bounds.origin.y
        return [Point(x + p.x * w, y + p.y * h) for p in self.local_ports]
