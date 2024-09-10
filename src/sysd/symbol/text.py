from typing import List

import svg

from sysd.core.bounding_box import BoundingBox
from sysd.core.connectable import Connectable
from sysd.core.font import FontBook
from sysd.core.size import Size
from sysd.core.anchor import Anchor


class Text(Connectable):
    def __init__(
        self,
        text: str,
        font_size: int = 10,
        font_family: str = "Arial",
        h_anchor: Anchor = Anchor.MIDDLE,
        v_anchor: Anchor = Anchor.MIDDLE,
    ):
        super().__init__()
        self._text = text
        self._font_family = font_family
        self._font_size = font_size
        self._halign = h_anchor
        self._valign = v_anchor
        self._line_height = self._font_size
        self._line_bboxes: List[BoundingBox] = []
        self._update_layout()

    @property
    def _text_size(self) -> Size:
        return Size(
            max([x.size.width for x in self._line_bboxes]),
            self._line_height * len(self._line_bboxes),
        )

    def _update_layout(self):
        self._line_bboxes = []
        for line in self._text.split("\n"):
            bbox = FontBook.default().get_bbox(self._font_family, self._font_size, line)
            self._line_bboxes.append(bbox)
        self.bounds.size.width = self._text_size.width
        self.bounds.size.height = self._text_size.height

    def render(self) -> svg.SVG:
        def align_center(line_bbox: BoundingBox) -> float:
            return 0.5 * (-line_bbox.size.width)

        def align_left(_: BoundingBox) -> float:
            return 0.0

        def align_right(line_bbox: BoundingBox) -> float:
            return -line_bbox.size.width

        align_func = align_center
        if self._halign == Anchor.START:
            align_func = align_left
        elif self._halign == Anchor.END:
            align_func = align_right

        y_start = 0.0
        if self._valign == Anchor.MIDDLE:
            y_start = -self._text_size.height / 2
        elif self._valign == Anchor.END:
            y_start = -self._text_size.height
        # breakpoint()
        tspans = [
            svg.TSpan(
                x=align_func(bbox),
                y=y_start + (i + 1) * self._line_height - bbox.origin.y,
                text=x,
            )
            for i, (x, bbox) in enumerate(
                zip(self._text.split("\n"), self._line_bboxes)
            )
        ]
        return svg.SVG(
            x=self.bounds.origin.x,
            y=self.bounds.origin.y,
            overflow="visible",
            elements=[  # type: ignore
                svg.Text(
                    font_size=self._font_size,
                    font_family=self._font_family,
                    font_weight="normal",
                    elements=tspans,  # type: ignore
                ),
            ],
        )
