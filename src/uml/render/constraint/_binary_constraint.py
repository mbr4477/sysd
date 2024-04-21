from ..renderable import Renderable
from ._constraint import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, node: Renderable, depends_on: Renderable):
        super().__init__(node)
        self.depends_on = depends_on
