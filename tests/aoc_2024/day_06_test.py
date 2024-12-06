import textwrap

from aoc_2024 import day_06

puzzle_input = textwrap.dedent(
    """\
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """
)


def test_solve_a():
    assert day_06.solve_a(puzzle_input) == 41


def test_solve_b():
    assert day_06.solve_b(puzzle_input) == 31
