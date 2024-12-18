from textwrap import dedent

from aoc_2024 import day_17

puzzle_input = dedent(
    """\
    Register A: 729
    Register B: 0
    Register C: 0

    Program: 0,1,5,4,3,0
    """
)


def test_solve_a():
    assert day_17.solve_a(puzzle_input) == "4,6,3,5,6,3,5,2,1,0"


def test_init():
    state = day_17.init(puzzle_input)
    expected = day_17.State(0, 729, 0, 0, [0, 1, 5, 4, 3, 0], [])
    assert state == expected


def test_solve_b():
    puzzle_input_b = dedent(
        """\
        Register A: 2024
        Register B: 0
        Register C: 0

        Program: 0,3,5,4,3,0
        """
    )
    assert day_17.solve_b(puzzle_input_b) == 117440
