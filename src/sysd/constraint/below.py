from .offset_constraint import OffsetConstraint


class Below(OffsetConstraint):
    def apply(self):
        self._target.bounds.origin.y = (
            self._dependency.bounds.origin.y
            + self._dependency.bounds.size.height
            + self._offset
        )
