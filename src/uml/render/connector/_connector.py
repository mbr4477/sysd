from ..renderable import Renderable


class Connector(Renderable):
    def __init__(self, source: Renderable, dest: Renderable):
        super().__init__()
        self._source = source
        self._dest = dest
