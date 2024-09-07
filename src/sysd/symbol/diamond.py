from ..connectable import Connectable
import svg


class Diamond(Connectable):
    def __init__(self):
        super().__init__()
        self.bounds.size.width = 20
        self.bounds.size.height = 20

    def render(self) -> svg.SVG:
        w = self.bounds.size.width
        hw = 0.5 * w
        h = self.bounds.size.height
        hh = 0.5 * h
        return svg.SVG(
            x=self.bounds.origin.x,
            y=self.bounds.origin.y,
            overflow="visible",
            elements=[  # type: ignore
                svg.Path(
                    stroke="black",
                    fill="none",
                    d=[
                        svg.M(hw, 0),
                        svg.L(w, hh),
                        svg.L(hw, h),
                        svg.L(0, hh),
                        svg.L(hw, 0),
                    ],
                )
            ],
        )
