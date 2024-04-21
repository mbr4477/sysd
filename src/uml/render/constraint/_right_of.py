from ._offset_constraint import OffsetConstraint


class RightOf(OffsetConstraint):
    def apply(self):
        self._node.x = self.depends_on.x + self.depends_on.width + self._offset
