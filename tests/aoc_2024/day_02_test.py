import textwrap

from aoc_2024 import day_02


def test_solve_a():
    puzzle_input = textwrap.dedent(
        """\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """
    )
    assert day_02.solve_a(puzzle_input) == 2


def test_solve_b():
    puzzle_input = textwrap.dedent(
        """\
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """
    )
    assert day_02.solve_b(puzzle_input) == 4
