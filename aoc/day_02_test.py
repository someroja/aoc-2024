import textwrap

from aoc import day_02


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


def test_is_safe_dampened():
    assert day_02.is_safe_dampened("1 2 3 4")
    assert day_02.is_safe_dampened("99 1 2 3 4")
    assert day_02.is_safe_dampened("1 2 3 4 99")
    assert day_02.is_safe_dampened("1 2 99 3 4")

    assert day_02.is_safe_dampened("4 3 2 1")
    assert day_02.is_safe_dampened("99 4 3 2 1")
    assert day_02.is_safe_dampened("4 3 2 1 99")
    assert day_02.is_safe_dampened("4 3 99 2 1")

    assert not day_02.is_safe_dampened("1 1 1 2 3 4")
    assert not day_02.is_safe_dampened("1 2 3 4 4 4")
    assert not day_02.is_safe_dampened("1 2 1 2")
    assert not day_02.is_safe_dampened("1 2 1 2 1")

    assert day_02.is_safe_dampened("7 6 4 2 1")
    assert not day_02.is_safe_dampened("1 2 7 8 9")
    assert not day_02.is_safe_dampened("9 7 6 2 1")
    assert day_02.is_safe_dampened("1 3 2 4 5")
    assert day_02.is_safe_dampened("8 6 4 4 1")
    assert day_02.is_safe_dampened("1 3 6 7 9")
