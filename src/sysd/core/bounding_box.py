import dataclasses

from .point import Point
from .size import Size


@dataclasses.dataclass
class BoundingBox:
    origin: Point
    size: Size
