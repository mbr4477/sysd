
from ..connectable import Connectable
from ..render_output import RenderOutput


class Diamond(Connectable):
    def __init__(self):
        super().__init__()
        self.bounds.size.width = 20
        self.bounds.size.height = 20

    def render(self) -> RenderOutput:
        w = self.bounds.size.width
        hw = 0.5 * w
        h = self.bounds.size.height
        hh = 0.5 * h
        return f"""
        <svg
            x="{self.bounds.origin.x}" 
            y="{self.bounds.origin.y}"
            overflow="visible">
            <path d="M{hw},0L{w},{hh}L{hw},{h}L0,{hh}L{hw},0" stroke="black" fill="none"/>
        </svg>
        """
