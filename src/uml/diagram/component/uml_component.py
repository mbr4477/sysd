from ...render import FontBook, Renderable, RenderOutput

UML_COMPONENT = """
<svg
    x="{x}" 
    y="{y}"
    overflow="visible">
    <rect
        width="{width}" 
        height="{height}"
        fill="white"
        stroke="black"/>
    <text 
        x="{label_x}" 
        y="15" 
        text-anchor="middle" 
        font-family="Inter"
        font-size="8">
        &lt;&lt;component&gt;&gt;
    </text>
    <text 
        x="{label_x}" 
        y="30" 
        text-anchor="middle" 
        font-size="10"
        font-family="Inter"
        font-weight="bold">
        {title}
    </text>
    <svg 
        x="{icon_x}" 
        y="{icon_y}"
        overflow="visible">
        <rect 
            width="10" 
            height="17" 
            fill="white" 
            stroke="black"/>
        <rect
            x="-4" 
            y="3" 
            width="8" 
            height="4" 
            fill="white" 
            stroke="black"/>
        <rect
            x="-4"
            y="10"
            width="8"
            height="4"
            fill="white"
            stroke="black"/>
    </svg>
</svg>
"""


class UMLComponent(Renderable):
    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.height = 50

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value
        self.width = 50 + FontBook.Singleton.get_rendered_width("Inter-Bold", 10, value)

    def render(self) -> RenderOutput:
        return UML_COMPONENT.format(
            title=self.title,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            label_x=self.width * 0.5,
            icon_x=self.width - 15,
            icon_y=5,
        )
