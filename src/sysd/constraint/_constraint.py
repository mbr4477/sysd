from ..renderable import Renderable


class Constraint:
    def __init__(self, target: Renderable):
        self._target = target

    def apply(self): ...

    @classmethod
    def new(cls, target: Renderable):
        cls(target).apply()
