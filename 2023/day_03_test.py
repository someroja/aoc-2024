from textwrap import dedent

import day_03


def test_find_digits():
    matches = day_03.find_digits("467..114..")
    assert matches[0].group() == "467"
    assert matches[1].group() == "114"


def test_find_surrounding_symbols():
    lines = dedent(
        """\
        .*...*..
        .#123#..
        .!!!!!..
        """
    ).splitlines()
    symbols = day_03.find_surrounding_symbols(lines, line_number=1, start=2, end=5)
    assert "".join(symbols) == "**##!!!!!"


def test_solve_a():
    puzzle_input = dedent(
        """\
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        """
    )
    assert day_03.solve_a(puzzle_input) == 4361


def test_solve_b():
    puzzle_input = dedent(
        """\
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        """
    )
    assert day_03.solve_b(puzzle_input) == 467835
