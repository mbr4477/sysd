from ._offset_constraint import OffsetConstraint


class CenterHorizontal(OffsetConstraint):
    def apply(self):
        self._target.bounds.origin.x = (
            self._dependency.bounds.origin.x
            + self._dependency.bounds.size.width / 2
            - self._target.bounds.size.width / 2
            + self._offset
        )
