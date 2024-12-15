from collections import deque
from typing import Callable, Final, Generic, List, NamedTuple, Tuple, TypeVar

T = TypeVar("T")


Grid = List[List[T]]


class Position(NamedTuple, Generic[T]):
    i: int
    j: int
    value: T


MatchPredicate = Callable[[Position[T], Position[T]], bool]

Direction = Tuple[int, int]

UP: Final[Direction] = (-1, 0)
DOWN: Final[Direction] = (1, 0)
LEFT: Final[Direction] = (0, -1)
RIGHT: Final[Direction] = (0, 1)


def create_grid(puzzle_input: str) -> Grid[str]:
    return [list(line) for line in puzzle_input.splitlines()]


def match_always(_a: Position[T], _b: Position[T]) -> bool:
    return True


def match_value(a: Position, b: Position) -> bool:
    return a.value == b.value


def get_neighbours(
    pos: Position[T], grid: Grid[T], predicate: MatchPredicate[T] = match_always
) -> List[Position[T]]:
    neighbours = []
    row_count, col_count = len(grid), len(grid[0])
    for di, dj in [UP, RIGHT, DOWN, LEFT]:
        neighbour_i, neighbour_j = pos.i + di, pos.j + dj
        is_outside_bounds = (
            neighbour_i < 0
            or neighbour_i >= row_count
            or neighbour_j < 0
            or neighbour_j >= col_count
        )
        if is_outside_bounds:
            continue
        neighbour = Position(neighbour_i, neighbour_j, grid[neighbour_i][neighbour_j])
        if predicate(pos, neighbour):
            neighbours.append(neighbour)
    return neighbours


def get_region(
    pos: Position[T], grid: Grid[T], predicate: MatchPredicate[T] = match_value
) -> List[Position[T]]:
    region = set()
    stack = deque([pos])
    while stack:
        current = stack.pop()
        if current not in region:
            region.add(current)
            stack.extend(
                neighbour
                for neighbour in get_neighbours(current, grid, predicate)
                if neighbour not in region
            )
    return list(region)


def get_all_regions(
    grid: Grid[T], predicate: MatchPredicate[T] = match_value
) -> List[List[Position[T]]]:
    regions = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pos = Position(i, j, grid[i][j])
            if pos in visited:
                continue
            region = get_region(pos, grid, predicate)
            regions.append(region)
            visited.update(region)
    return regions


def get_perimeter(region: List[Position[T]]) -> int:
    coordinates = {(pos.i, pos.j) for pos in region}
    perimeter = 0
    for pos in region:
        for di, dj in [UP, RIGHT, DOWN, LEFT]:
            is_edge = (pos.i + di, pos.j + dj) not in coordinates
            if is_edge:
                perimeter += 1
    return perimeter

