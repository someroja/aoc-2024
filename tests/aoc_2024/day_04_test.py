import textwrap

from aoc_2024 import day_04


def test_solve_a():
    puzzle_input = textwrap.dedent(
        """\
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
        """
    )
    assert day_04.solve_a(puzzle_input) == 18


def test_find_xmas_words():
    lines = [
        "S..S..S",
        ".A.A.A.",
        "..MMM..",
        "SAMXMAS",
        "..MMM..",
        ".A.A.A.",
        "S..S..S",
    ]
    words = day_04.find_xmas_words(3, 3, lines)
    assert len(words) == 8


def test_solve_b():
    puzzle_input = textwrap.dedent(
        """\
        .M.S......
        ..A..MSMS.
        .M.S.MAA..
        ..A.ASMSM.
        .M.S.M....
        ..........
        S.S.S.S.S.
        .A.A.A.A..
        M.M.M.M.M.
        ..........
        """
    )
    assert day_04.solve_b(puzzle_input) == 9


def test_is_xmas():
    assert day_04.is_x_mas(1, 1, ["M.S", ".A.", "M.S"])
    assert day_04.is_x_mas(1, 1, ["S.S", ".A.", "M.M"])
    assert day_04.is_x_mas(1, 1, ["S.M", ".A.", "S.M"])
