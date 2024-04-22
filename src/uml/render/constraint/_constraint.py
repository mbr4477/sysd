from ..bounding_box import BoundingBox


class Constraint:
    def __init__(self, node: BoundingBox):
        self._node = node

    def apply(self): ...
