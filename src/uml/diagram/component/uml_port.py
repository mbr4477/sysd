from ...render import Renderable, RenderOutput


class UMLPort(Renderable):
    _SVG = """
    <svg
        x="{x}"
        y="{y}"
        overflow="visible">
        <rect
            width="{width}"
            height="{height}"
            fill="white"
            stroke="black"/>
    </svg>
    """

    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.width = 7
        self.height = 7

    def render(self) -> RenderOutput:
        return UMLPort._SVG.format(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
        )
