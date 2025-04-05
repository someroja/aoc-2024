from aoc import day_03


def test_solve_a():
    puzzle_input = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    assert day_03.solve_a(puzzle_input) == 161


def test_solve_b():
    puzzle_input = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert day_03.solve_b(puzzle_input) == 48
