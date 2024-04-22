from ..bounding_box import BoundingBox
from ._binary_constraint import BinaryConstraint


class OffsetConstraint(BinaryConstraint):
    def __init__(
        self, node: BoundingBox, depends_on: BoundingBox, *, offset: float = 0.0
    ):
        super().__init__(node, depends_on)
        self._offset = offset
