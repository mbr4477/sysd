from ..bounding_box import BoundingBox
from ._constraint import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, node: BoundingBox, depends_on: BoundingBox):
        super().__init__(node)
        self.depends_on = depends_on
