from ..renderable import Renderable
from ._binary_constraint import BinaryConstraint


class OffsetConstraint(BinaryConstraint):
    def __init__(
        self, target: Renderable, dependency: Renderable, *, offset: float = 0.0
    ):
        super().__init__(target, dependency)
        self._offset = offset

    @classmethod
    def new(cls, target: Renderable, dependency: Renderable, *, offset: float = 0.0):
        cls(target, dependency, offset=offset).apply()
