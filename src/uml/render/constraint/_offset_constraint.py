from ..renderable import Renderable
from ._binary_constraint import BinaryConstraint


class OffsetConstraint(BinaryConstraint):
    def __init__(
        self, node: Renderable, depends_on: Renderable, *, offset: float = 0.0
    ):
        super().__init__(node, depends_on)
        self._offset = offset
