from ._offset_constraint import OffsetConstraint


class RightOf(OffsetConstraint):
    def apply(self):
        self._target.bounds.origin.x = (
            self._dependency.bounds.origin.x
            + self._dependency.bounds.size.width
            + self._offset
        )
