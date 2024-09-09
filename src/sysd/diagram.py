from typing import Iterable, List, Optional, TypeVar

import svg

from sysd.core.renderable import Renderable

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

    def render(self) -> svg.SVG:
        return svg.SVG(
            xmlns="http://www.w3.org/2000/svg",
            elements=[x.render() for x in self._renderables],
        )
