from textwrap import dedent

import pytest

from aoc import day_12

puzzle_input = dedent(
    """\
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
    """
)


def test_solve_a():
    assert day_12.solve_a(puzzle_input) == 1930


@pytest.mark.skip
def test_solve_b():
    assert day_12.solve_b(puzzle_input) == 1206
