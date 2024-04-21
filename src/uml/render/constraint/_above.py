from ._offset_constraint import OffsetConstraint


class Above(OffsetConstraint):
    def apply(self):
        self._node.y = self.depends_on.y - self._node.height - self._offset
