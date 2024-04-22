from .bounding_box import BoundingBox


class Point(BoundingBox):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__(x, y)
