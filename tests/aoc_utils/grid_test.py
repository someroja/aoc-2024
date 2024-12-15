from textwrap import dedent

import pytest

from aoc_utils import grid

abcde_grid = grid.create_grid(
    dedent(
        """\
            AAAA
            BBCD
            BBCC
            EEEC
            """
    )
)

ox_grid = grid.create_grid(
    dedent(
        """\
            OOOOO
            OXOXO
            OOOOO
            OXOXO
            OOOOO
            """
    )
)


@pytest.mark.parametrize(
    "test_grid,expected",
    [
        (abcde_grid, 5),
        (ox_grid, 5),
    ],
)
def test_get_all_regions(test_grid: grid.Grid[grid.T], expected: int):
    regions = grid.get_all_regions(test_grid)
    assert len(regions) == expected


@pytest.mark.parametrize(
    "pos,expected",
    [
        (grid.Position(0, 0, "A"), 4),
        (grid.Position(1, 1, "B"), 4),
        (grid.Position(2, 2, "C"), 4),
        (grid.Position(1, 3, "D"), 1),
        (grid.Position(3, 1, "E"), 3),
    ],
)
def test_get_region(pos: grid.Position, expected: int):
    region = grid.get_region(pos, abcde_grid)
    assert len(region) == expected


@pytest.mark.parametrize(
    "pos,expected",
    [
        (grid.Position(0, 0, "A"), 1),
        (grid.Position(1, 1, "B"), 2),
        (grid.Position(2, 2, "C"), 2),
        (grid.Position(1, 3, "D"), 0),
        (grid.Position(3, 1, "E"), 2),
    ],
)
def test_get_neighbours(pos: grid.Position, expected: int):
    neighbours = grid.get_neighbours(pos, abcde_grid, grid.match_value)
    assert len(neighbours) == expected


@pytest.mark.parametrize(
    "pos,expected",
    [
        (grid.Position(0, 0, "A"), 10),
        (grid.Position(1, 1, "B"), 8),
        (grid.Position(2, 2, "C"), 10),
        (grid.Position(1, 3, "D"), 4),
        (grid.Position(3, 1, "E"), 8),
    ],
)
def test_get_perimeter(pos: grid.Position, expected: int):
    region = grid.get_region(pos, abcde_grid)
    assert len(grid.get_perimeter(region)) == expected
