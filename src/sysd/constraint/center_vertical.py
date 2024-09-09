from .offset_constraint import OffsetConstraint


class CenterVertical(OffsetConstraint):
    def apply(self):
        self._target.bounds.origin.y = (
            self._dependency.bounds.origin.y
            + self._dependency.bounds.size.height / 2
            - self._target.bounds.size.height / 2
            + self._offset
        )
