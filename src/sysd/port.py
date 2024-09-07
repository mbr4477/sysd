import math
from typing import Tuple

from .point import Point
from .renderable import Renderable


def north(x: LayoutMember) -> Point:
    return Point(x.bounds.origin.x + x.bounds.size.width / 2, x.bounds.origin.y)


def south(x: LayoutMember) -> Point:
    return Point(
        x.bounds.origin.x + x.bounds.size.width / 2,
        x.bounds.origin.y + x.bounds.size.height,
    )


def east(x: LayoutMember) -> Point:
    return Point(
        x.bounds.origin.x + x.bounds.size.width,
        x.bounds.origin.y + x.bounds.size.height / 2,
    )


def west(x: LayoutMember) -> Point:
    return Point(x.bounds.origin.x, x.bounds.origin.y + x.bounds.size.height / 2)


def edge_points(source: LayoutMember, dest: LayoutMember) -> Tuple[Point, Point]:
    src_x = source.bounds.origin.x + source.bounds.size.width / 2
    src_y = source.bounds.origin.y + source.bounds.size.height / 2
    dst_x = dest.bounds.origin.x + dest.bounds.size.width / 2
    dst_y = dest.bounds.origin.y + dest.bounds.size.height / 2
    dx = dst_x - src_x
    dy = dst_y - src_y
    inv_dx = 1 / dx if dx != 0 else math.inf
    inv_dy = 1 / dy if dy != 0 else math.inf
    start_t = min(
        0.5 * source.bounds.size.width * inv_dx,
        0.5 * source.bounds.size.height * inv_dy,
    )
    end_t = 1 - min(
        0.5 * dest.bounds.size.width * inv_dx,
        0.5 * dest.bounds.size.height * inv_dy,
    )
    return Point(src_x + dx * start_t, src_y + dy * start_t), Point(
        src_x + dx * end_t, src_y + dy * end_t
    )
