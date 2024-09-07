from ..renderable import Renderable
from ._constraint import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, target: Renderable, dependency: Renderable):
        super().__init__(target)
        self._dependency = dependency

    @classmethod
    def new(cls, target: Renderable, dependency: Renderable):
        cls(target, dependency).apply()
