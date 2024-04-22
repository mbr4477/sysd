from ..bounding_box import BoundingBox
from ..renderable import Renderable


class Connector(Renderable):
    def __init__(self, source: BoundingBox, dest: BoundingBox):
        super().__init__()
        self._source = source
        self._dest = dest
