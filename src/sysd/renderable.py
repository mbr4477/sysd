from .bounding_box import BoundingBox
from .point import Point
from .render_output import RenderOutput
from .size import Size


class Renderable:
    def __init__(self):
        self.bounds = BoundingBox(Point(0.0, 0.0), Size(0.0, 0.0))

    def render(self) -> RenderOutput:
        """
        Render the renderable.

        :returns: The render output.
        """
        raise NotImplementedError
