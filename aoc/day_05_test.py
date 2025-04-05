from textwrap import dedent

from aoc import day_05

puzzle_input = dedent(
    """\
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """
)


def test_solve_a():
    assert day_05.solve_a(puzzle_input) == 143


def test_is_correct_order():
    ruleData, updateData = puzzle_input.split("\n\n")
    rules = ruleData.splitlines()
    updates = updateData.splitlines()
    assert day_05.is_correct_order(updates[0], rules)
    assert day_05.is_correct_order(updates[1], rules)
    assert day_05.is_correct_order(updates[2], rules)
    assert not day_05.is_correct_order(updates[3], rules)
    assert not day_05.is_correct_order(updates[4], rules)
    assert not day_05.is_correct_order(updates[5], rules)


def test_solve_b():
    assert day_05.solve_b(puzzle_input) == 123


def test_sort_pages():
    rules = puzzle_input.split("\n\n")[0].splitlines()
    # no sorting, already correct
    assert day_05.sort_pages([75, 47, 61, 53, 29], rules) == [75, 47, 61, 53, 29]
    assert day_05.sort_pages([97, 61, 53, 29, 13], rules) == [97, 61, 53, 29, 13]
    assert day_05.sort_pages([75, 29, 13], rules) == [75, 29, 13]
    # sorted
    assert day_05.sort_pages([75, 97, 47, 61, 53], rules) == [97, 75, 47, 61, 53]
    assert day_05.sort_pages([61, 13, 29], rules) == [61, 29, 13]
    assert day_05.sort_pages([97, 13, 75, 29, 47], rules) == [97, 75, 47, 29, 13]
