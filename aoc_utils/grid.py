from collections import deque
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Final

type Grid[T] = Sequence[Sequence[T]]

type MapTileValue[T] = Callable[[str], T]


def map_to_str(value: str) -> str:
    return value


def map_to_int(value: str) -> int:
    return int(value)


@dataclass(frozen=True)
class Tile[T]:
    i: int
    j: int
    value: T


@dataclass(frozen=True)
class Region[T]:
    tiles: Sequence[Tile[T]]


@dataclass(frozen=True)
class Position:
    i: int
    j: int


type MatchPredicate[T] = Callable[[Tile[T], Tile[T]], bool]


def match_always[T](_a: Tile[T], _b: Tile[T]) -> bool:
    return True


def match_value[T](a: Tile[T], b: Tile[T]) -> bool:
    return a.value == b.value


type Direction = tuple[int, int]

UP: Final[Direction] = (-1, 0)
DOWN: Final[Direction] = (1, 0)
LEFT: Final[Direction] = (0, -1)
RIGHT: Final[Direction] = (0, 1)


def create_grid[T](
    puzzle_input: str, map_tile_value: MapTileValue[T] = map_to_str
) -> Grid[T]:
    return [
        [map_tile_value(tile) for tile in list(row)]
        for row in puzzle_input.splitlines()
    ]


def get_neighbours[T](
    tile: Tile[T], grid: Grid[T], predicate: MatchPredicate[T] = match_always
) -> Sequence[Tile[T]]:
    neighbours = []
    row_count, col_count = len(grid), len(grid[0])
    for di, dj in [UP, RIGHT, DOWN, LEFT]:
        neighbour_i, neighbour_j = tile.i + di, tile.j + dj
        is_outside_bounds = (
            neighbour_i < 0
            or neighbour_i >= row_count
            or neighbour_j < 0
            or neighbour_j >= col_count
        )
        if is_outside_bounds:
            continue
        neighbour = Tile(neighbour_i, neighbour_j, grid[neighbour_i][neighbour_j])
        if predicate(tile, neighbour):
            neighbours.append(neighbour)
    return neighbours


def get_region[T](
    tile: Tile[T], grid: Grid[T], predicate: MatchPredicate[T] = match_value
) -> Region[T]:
    tiles = set()
    stack = deque([tile])
    while stack:
        current = stack.pop()
        if current not in tiles:
            tiles.add(current)
            stack.extend(
                neighbour
                for neighbour in get_neighbours(current, grid, predicate)
                if neighbour not in tiles
            )
    return Region(list(tiles))


def get_all_regions[T](
    grid: Grid[T], predicate: MatchPredicate[T] = match_value
) -> Sequence[Region[T]]:
    regions = []
    visited_tiles = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tile = Tile(i, j, grid[i][j])
            if tile in visited_tiles:
                continue
            region = get_region(tile, grid, predicate)
            regions.append(region)
            visited_tiles.update(region.tiles)
    return regions


def get_perimeter[T](region: Region[T]) -> int:
    coordinates = {(tile.i, tile.j) for tile in region.tiles}
    perimeter = 0
    for tile in region.tiles:
        for di, dj in [UP, RIGHT, DOWN, LEFT]:
            is_edge = (tile.i + di, tile.j + dj) not in coordinates
            if is_edge:
                perimeter += 1
    return perimeter
