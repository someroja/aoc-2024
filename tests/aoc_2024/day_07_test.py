import textwrap

from aoc_2024 import day_07

puzzle_input = textwrap.dedent(
    """\
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    """
)


def test_solve_a():
    assert day_07.solve_a(puzzle_input) == 3749


def test_solve_b():
    assert day_07.solve_b(puzzle_input) == 11387
