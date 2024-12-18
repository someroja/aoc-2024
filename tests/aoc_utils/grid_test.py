from textwrap import dedent

import pytest

from aoc_utils.grid import (
    Grid,
    Tile,
    create_grid,
    get_all_regions,
    get_neighbours,
    get_perimeter,
    get_region,
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


def test_get_all_regions_abcde_grid(abcde_grid: Grid[str]):
    regions = get_all_regions(abcde_grid)
    assert len(regions) == 5


def test_get_all_regions_ox_grid(ox_grid: Grid[str]):
    regions = get_all_regions(ox_grid)
    assert len(regions) == 5


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
