import textwrap

from aoc_2023 import day_01


def test_solve_a():
    puzzle_input = textwrap.dedent(
        """\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
    )
    assert day_01.solve_a(puzzle_input) == 142


def test_b_regex():
    assert day_01.parse_line("7eightwone") == [7, 8, 2, 1]
    assert day_01.parse_line("two1nine") == [2, 1, 9]
    assert day_01.parse_line("eightwothree") == [8, 2, 3]
    assert day_01.parse_line("abcone2threexyz") == [1, 2, 3]
    assert day_01.parse_line("xtwone3four") == [2, 1, 3, 4]
    assert day_01.parse_line("4nineeightseven2") == [4, 9, 8, 7, 2]
    assert day_01.parse_line("zoneight234") == [1, 8, 2, 3, 4]
    assert day_01.parse_line("7pqrstsixteen") == [7, 6]


def test_solve_b():
    puzzle_input = textwrap.dedent(
        """\
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
    )
    assert day_01.solve_b(puzzle_input) == 281
