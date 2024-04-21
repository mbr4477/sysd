from ..renderable import Renderable


class Constraint:
    def __init__(self, node: Renderable):
        self._node = node

    def apply(self): ...
