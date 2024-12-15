from textwrap import dedent

from aoc_2024 import day_12

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


def test_solve_b():
    assert day_12.solve_b(puzzle_input) == 1206
