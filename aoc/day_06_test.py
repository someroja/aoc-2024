import textwrap

import pytest

from aoc import day_06


@pytest.fixture
def puzzle_input() -> str:
    return textwrap.dedent(
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


def test_solve_a(puzzle_input: str):
    assert day_06.solve_a(puzzle_input) == 41


def test_solve_b(puzzle_input: str):
    assert day_06.solve_b(puzzle_input) == 6
