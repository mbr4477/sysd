from ._offset_constraint import OffsetConstraint


class Below(OffsetConstraint):
    def apply(self):
        self._node.y = self.depends_on.y + self.depends_on.height + self._offset
