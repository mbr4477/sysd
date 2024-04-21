from ._offset_constraint import OffsetConstraint


class CenterVertical(OffsetConstraint):
    def apply(self):
        self._node.y = (
            self.depends_on.y
            + self.depends_on.height / 2
            - self._node.height / 2
            + self._offset
        )
