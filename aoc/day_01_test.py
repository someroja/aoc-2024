import textwrap

from aoc import day_01


def test_solve_a():
    puzzle_input = textwrap.dedent(
        """\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """
    )
    assert day_01.solve_a(puzzle_input) == 11


def test_solve_b():
    puzzle_input = textwrap.dedent(
        """\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """
    )
    assert day_01.solve_b(puzzle_input) == 31
