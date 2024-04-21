from __future__ import annotations

import glob
import os
from typing import Dict, Iterable

from PIL import ImageFont


class FontBook:
    Singleton: FontBook

    def __init__(self, ttf_paths: Iterable[str]):
        self._paths = ttf_paths
        self._families = {
            os.path.basename(x).rsplit(".", 1)[0].replace(" ", ""): x
            for x in self._paths
        }
        self._font_cache: Dict[int, ImageFont.FreeTypeFont] = {}
        self.families = list(self._families.keys())

    def get_rendered_width(self, font_family: str, font_size: int, text: str) -> int:
        key = hash(font_family + str(font_size))
        if key not in self._font_cache:
            self._font_cache[key] = ImageFont.truetype(
                self._families[font_family], font_size
            )
        font = self._font_cache[key]
        return font.getlength(text)

    @staticmethod
    def init(root_dir: str):
        files = glob.glob(os.path.join(root_dir, "**", "*.ttf"), recursive=True)
        FontBook.Singleton = FontBook(files)
