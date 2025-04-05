"""
Advent of Code 2024, day 1
"""

import re

import aocd


def solve_a(puzzle_input: str) -> int:
    left_numbers, right_numbers = parse_input(puzzle_input)
    id_pairs = list(zip(sorted(left_numbers), sorted(right_numbers)))
    distances = [abs(left - right) for left, right in id_pairs]
    return sum(distances)


def solve_b(puzzle_input: str) -> int:
    left_numbers, right_numbers = parse_input(puzzle_input)
    scores = [number * right_numbers.count(number) for number in left_numbers]
    return sum(scores)


def parse_input(puzzle_input: str) -> tuple[list[int], list[int]]:
    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for line in puzzle_input.splitlines():
        numbers = [int(match) for match in re.findall(r"\d+", line)]
        left_numbers.append(numbers[0])
        right_numbers.append(numbers[-1])

    return (left_numbers, right_numbers)


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=1, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
