from __future__ import annotations

import glob
import os
import sys
from typing import Dict, Iterable

import fontTools.ttLib
from PIL import ImageFont

from .bounding_box import BoundingBox
from .point import Point
from .size import Size


class FontBook:
    _instance: FontBook

    def __init__(self, ttf_paths: Iterable[str]):
        self._paths = ttf_paths
        self._families = {
            str(fontTools.ttLib.TTFont(x)["name"].names[1]): x for x in self._paths  # type: ignore
        }
        self._font_cache: Dict[int, ImageFont.FreeTypeFont] = {}
        self.families = list(self._families.keys())
        self.default_family = next(iter(self._families))

    def get_bbox(self, font_family: str, font_size: int, text: str) -> BoundingBox:
        key = hash(font_family + str(font_size))
        if key not in self._font_cache:
            self._font_cache[key] = ImageFont.truetype(
                self._families[font_family], font_size
            )
        font = self._font_cache[key]
        left, top, right, bottom = font.getbbox(text)
        return BoundingBox(Point(left, top), Size(right - left, bottom - top))

    @staticmethod
    def init(*root_dirs: str):
        dirs = list(root_dirs)
        if sys.platform == "darwin":
            dirs.append("/System/Library/Fonts")
            dirs.append(os.path.join(os.path.expanduser("~"), "Library", "Fonts"))
        files = [
            f
            for x in dirs
            for f in glob.glob(os.path.join(x, "**", "*.ttf"), recursive=True)
        ]
        FontBook._instance = FontBook(files)

    @staticmethod
    def default() -> FontBook:
        return FontBook._instance
