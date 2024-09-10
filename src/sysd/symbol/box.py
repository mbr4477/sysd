import svg

from sysd.core.connectable import Connectable

from .text import Text


class Box(Connectable):
    def __init__(self, title: str):
        super().__init__()
        self.label = Text(title)
        self.bounds.size.width = self.label.bounds.size.width + 20
        self.bounds.size.height = self.label.bounds.size.height + 20
        self.label.bounds.origin.x = self.bounds.size.width / 2
        self.label.bounds.origin.y = self.bounds.size.height / 2

    def render(self) -> svg.SVG:
        return svg.SVG(
            x=self.bounds.origin.x,
            y=self.bounds.origin.y,
            overflow="visible",
            elements=[  # type: ignore
                svg.Rect(
                    width=self.bounds.size.width,
                    height=self.bounds.size.height,
                    fill="white",
                    stroke="black",
                    class_=["block"],
                ),
                self.label.render(),
            ],
        )
