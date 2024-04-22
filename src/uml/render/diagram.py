from typing import Iterable, List, Optional, TypeVar

from .render_output import RenderOutput
from .renderable import Renderable
from .constraint import Constraint

_T = TypeVar("_T", bound=Renderable)


class Diagram(Renderable):
    def __init__(
        self,
        name: Optional[str] = None,
        renderables: Optional[Iterable[Renderable]] = None,
    ):
        self._renderables: List[Renderable] = []
        if renderables:
            self._renderables = list(renderables)

    def add(self, renderable: _T) -> _T:
        self._renderables.append(renderable)
        return renderable

    def constraint(self, constraint: Constraint):
        constraint.apply()

    def render(self) -> RenderOutput:
        out = '<svg xmlns="http://www.w3.org/2000/svg">'
        out += "".join(x.render() for x in self._renderables)
        out += "</svg>"
        return out
