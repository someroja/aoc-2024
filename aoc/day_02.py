"""
Advent of Code 2024, day 2
"""

import re

import aocd


def solve_a(puzzle_input: str) -> int:
    safe_lines = [line for line in puzzle_input.splitlines() if is_safe(parse(line))]
    return len(safe_lines)


def parse(line: str) -> list[int]:
    return [int(match) for match in re.findall(r"\d+", line)]


def is_safe(numbers: list[int]) -> bool:
    is_ascending = numbers[0] < numbers[-1]
    return all(
        [
            (a < b if is_ascending else a > b) and is_safe_delta(a, b)
            for a, b in zip(numbers, numbers[1:])
        ]
    )


def is_safe_delta(a: int, b: int) -> bool:
    delta = abs(a - b)
    return delta >= 1 and delta <= 3


def solve_b(puzzle_input: str) -> int:
    safe_lines = [line for line in puzzle_input.splitlines() if is_safe_dampened(line)]
    return len(safe_lines)


def is_safe_dampened(line: str) -> bool:
    numbers = parse(line)
    # Problem Dampener and brute force...
    dampening_attempts = [
        numbers[:skipped] + numbers[skipped + 1 :] for skipped in range(len(numbers))
    ]
    return is_safe(numbers) or any(is_safe(attempt) for attempt in dampening_attempts)


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=2, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
