from ._offset_constraint import OffsetConstraint


class CenterHorizontal(OffsetConstraint):
    def apply(self):
        self._node.x = (
            self.depends_on.x
            + self.depends_on.width / 2
            - self._node.width / 2
            + self._offset
        )
