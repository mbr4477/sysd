from .bounding_box import BoundingBox
from .point import Point


class Rect(BoundingBox):
    @property
    def north(self) -> Point:
        return Point(self.x + self.width / 2, self.y)

    @property
    def northeast(self) -> Point:
        return Point(self.x + self.width, self.y)

    @property
    def east(self) -> Point:
        return Point(self.x + self.width, self.y + self.height / 2)

    @property
    def southeast(self) -> Point:
        return Point(self.x + self.width, self.y + self.height)

    @property
    def south(self) -> Point:
        return Point(self.x + self.width / 2, self.y + self.height)

    @property
    def southwest(self) -> Point:
        return Point(self.x, self.y + self.height)

    @property
    def west(self) -> Point:
        return Point(self.x, self.y + self.height / 2)

    @property
    def northwest(self) -> Point:
        return Point(self.x, self.y)
