from textwrap import dedent

import pytest

from aoc_2024 import day_19


@pytest.fixture
def puzzle_input() -> str:
    return dedent(
        """\
        r, wr, b, g, bwu, rb, gb, br

        brwrr
        bggr
        gbbr
        rrbgbr
        ubwu
        bwurrg
        brgr
        bbrgwb
        """
    )


def test_solve_a(puzzle_input: str):
    assert day_19.solve_a(puzzle_input) == 6


def test_solve_b(puzzle_input: str):
    assert day_19.solve_b(puzzle_input) == 16
