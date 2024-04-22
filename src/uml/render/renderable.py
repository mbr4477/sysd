from .bounding_box import BoundingBox
from .render_output import RenderOutput


class Renderable(BoundingBox):
    def __init__(self):
        super().__init__()
        self.x = 0.0
        self.y = 0.0
        self._width = 0.0
        self._height = 0.0

    def update_layout(self):
        pass

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value
        self.update_layout()

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value
        self.update_layout()

    def render(self) -> RenderOutput: ...
