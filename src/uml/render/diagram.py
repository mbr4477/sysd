from typing import Iterable, List, Optional

from .render_output import RenderOutput
from .renderable import Renderable


class Diagram(Renderable):
    def __init__(self, name: str, renderables: Optional[Iterable[Renderable]] = None):
        self._renderables: List[Renderable] = []
        if renderables:
            self._renderables = list(renderables)

    def add(self, renderable: Renderable):
        self._renderables.append(renderable)

    def render(self) -> RenderOutput:
        out = '<svg xmlns="http://www.w3.org/2000/svg">'
        out += "".join(x.render() for x in self._renderables)
        out += "</svg>"
        return out
