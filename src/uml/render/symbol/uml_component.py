from ...render import FontBook, Renderable, RenderOutput
from ..rect import Rect


class UMLComponent(Renderable, Rect):
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
        <text 
            x="{label_x}" 
            y="15" 
            text-anchor="middle" 
            font-family="{font_family}"
            font-size="8">
            &lt;&lt;component&gt;&gt;
        </text>
        <text 
            x="{label_x}" 
            y="30" 
            text-anchor="middle" 
            font-size="10"
            font-family="{font_family}"
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

    def __init__(self, title: str):
        super().__init__()
        self.height = 50
        self._title = title
        self._font_family = FontBook.Singleton.default_family
        self._update_layout()

    def _update_layout(self):
        self.width = 50 + FontBook.Singleton.get_length(
            self.font_family, 10, self.title
        )

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value
        self._update_layout()

    @property
    def font_family(self) -> str:
        return self._font_family

    @font_family.setter
    def font_family(self, value: str):
        self._font_family = value
        self._update_layout()

    def render(self) -> RenderOutput:
        return UMLComponent._SVG.format(
            title=self.title,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            font_family=self.font_family,
            label_x=self.width * 0.5,
            icon_x=self.width - 15,
            icon_y=5,
        )
