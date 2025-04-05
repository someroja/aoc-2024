from textwrap import dedent

import pytest

from aoc.utils.grid import (
    Grid,
    Tile,
    create_grid,
    get_all_regions,
    get_neighbours,
    get_perimeter,
    get_region,
    get_tiles,
    match_value,
)


@pytest.fixture
def abcde_grid() -> Grid[str]:
    return create_grid(
        dedent(
            """\
            AAAA
            BBCD
            BBCC
            EEEC
            """
        )
    )


@pytest.fixture
def ox_grid() -> Grid[str]:
    return create_grid(
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


@pytest.fixture
def number_grid() -> Grid[int]:
    return create_grid(
        dedent(
            """\
            00000
            01020
            00000
            03040
            00000
            """
        ),
        int,
    )


def test_get_all_regions(abcde_grid: Grid[str], ox_grid: Grid[str]):
    assert len(get_all_regions(abcde_grid)) == 5
    assert len(get_all_regions(ox_grid)) == 5


@pytest.mark.parametrize(
    "tile,expected_area",
    [
        (Tile(0, 0, "A"), 4),
        (Tile(1, 1, "B"), 4),
        (Tile(2, 2, "C"), 4),
        (Tile(1, 3, "D"), 1),
        (Tile(3, 1, "E"), 3),
    ],
)
def test_get_region(abcde_grid: Grid[str], tile: Tile[str], expected_area: int):
    region = get_region(tile, abcde_grid)
    assert len(region.tiles) == expected_area


@pytest.mark.parametrize(
    "tile,expected_count",
    [
        (Tile(0, 0, "A"), 1),
        (Tile(1, 1, "B"), 2),
        (Tile(2, 2, "C"), 2),
        (Tile(1, 3, "D"), 0),
        (Tile(3, 1, "E"), 2),
    ],
)
def test_get_neighbours(abcde_grid: Grid[str], tile: Tile[str], expected_count: int):
    neighbours = get_neighbours(tile, abcde_grid, match_value)
    assert len(neighbours) == expected_count


@pytest.mark.parametrize(
    "tile,expected",
    [
        (Tile(0, 0, "A"), 10),
        (Tile(1, 1, "B"), 8),
        (Tile(2, 2, "C"), 10),
        (Tile(1, 3, "D"), 4),
        (Tile(3, 1, "E"), 8),
    ],
)
def test_get_perimeter(abcde_grid: Grid[str], tile: Tile[str], expected: int):
    region = get_region(tile, abcde_grid)
    assert get_perimeter(region) == expected


def test_get_tiles(abcde_grid: Grid[str], ox_grid: Grid[str]):
    assert len(get_tiles(abcde_grid)) == 16
    assert len(get_tiles(abcde_grid, lambda tile: tile.value == "A")) == 4
    assert len(get_tiles(abcde_grid, lambda tile: tile.value == "B")) == 4
    assert len(get_tiles(abcde_grid, lambda tile: tile.value == "C")) == 4
    assert len(get_tiles(abcde_grid, lambda tile: tile.value == "D")) == 1
    assert len(get_tiles(abcde_grid, lambda tile: tile.value == "E")) == 3
    assert len(get_tiles(ox_grid)) == 25
    assert len(get_tiles(ox_grid, lambda tile: tile.value == "X")) == 4


def test_number_grid(number_grid: Grid[int]):
    nonzeros = [
        tile.value for tile in get_tiles(number_grid, lambda tile: tile.value > 0)
    ]
    assert sorted(nonzeros) == [1, 2, 3, 4]
