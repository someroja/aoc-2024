"""
Advent of Code 2024, day 2
"""

import re

import aocd


def solve_a(puzzle_input: str) -> int:
    safe_count = 0

    for line in puzzle_input.splitlines():
        numbers = [int(match) for match in re.findall(r"\d+", line)]
        is_ascending = numbers[0] < numbers[-1]
        is_safe = all(
            [is_safe_delta(a, b, is_ascending) for a, b in zip(numbers, numbers[1:])]
        )
        if is_safe:
            safe_count += 1

    return safe_count


def is_safe_delta(a: int, b: int, is_ascending: bool) -> bool:
    if is_ascending:
        return a < b and b <= a + 3
    else:
        return a > b and a <= b + 3


def solve_b(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=2, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
