from typing import List

import svg

from ..bounding_box import BoundingBox
from ..connectable import Connectable
from ..font import FontBook
from ..size import Size
from ..text_align import Align


class Box(Connectable):
    def __init__(self, title: str):
        super().__init__()
        self._title = title
        self._font_family = FontBook._instance.default_family
        self._font_size = 10
        self._text_align = Align.CENTER
        self._line_height = self._font_size
        self._line_bboxes: List[BoundingBox] = []
        self._update_layout()

    @property
    def text_size(self) -> Size:
        return Size(
            max([x.size.width for x in self._line_bboxes]),
            self._line_height * len(self._line_bboxes),
        )

    def _update_layout(self):
        self._line_bboxes = []
        for line in self.title.split("\n"):
            bbox = FontBook.default().get_bbox(self.font_family, self._font_size, line)
            self._line_bboxes.append(bbox)
        self.bounds.size.width = 20 + self.text_size.width
        self.bounds.size.height = 20 + self.text_size.height

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

    def render(self) -> svg.SVG:
        def align_center(line_bbox: BoundingBox) -> float:
            return 0.5 * (self.bounds.size.width - line_bbox.size.width)

        def align_left(line_bbox: BoundingBox) -> float:
            return 0.5 * (self.bounds.size.width - self.text_size.width)

        def align_right(line_bbox: BoundingBox) -> float:
            return (
                0.5 * (self.bounds.size.width + self.text_size.width)
                - line_bbox.size.width
            )

        tspans = [
            svg.TSpan(
                x=align_center(bbox),
                y=0.5 * (self.bounds.size.height - self.text_size.height)
                + i * self._line_height,
                text=x,
            )
            for i, (x, bbox) in enumerate(
                zip(self._title.split("\n"), self._line_bboxes)
            )
        ]
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
                svg.Text(
                    font_size=self._font_size,
                    font_family=self.font_family,
                    font_weight="normal",
                    elements=tspans,  # type: ignore
                ),
            ],
        )
