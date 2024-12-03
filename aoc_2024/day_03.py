"""
Advent of Code 2024, day 3
"""

import re

import aocd


def solve_a(puzzle_input: str) -> int:
    results: list[int] = []
    for line in puzzle_input.splitlines():
        mul_instructions = re.findall(r"mul\(\d+,\d+\)", line)
        for mul in mul_instructions:
            numbers = [int(match) for match in re.findall(r"\d+", mul)]
            results.append(numbers[0] * numbers[1])
    return sum(results)


def solve_b(puzzle_input: str) -> int:
    results: list[int] = []
    enabled = True
    for line in puzzle_input.splitlines():
        instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for instruction in instructions:
            match instruction:
                case "do()":
                    enabled = True
                case "don't()":
                    enabled = False
                # Has to be mul
                case _:
                    if enabled:
                        numbers = [
                            int(match) for match in re.findall(r"\d+", instruction)
                        ]
                        results.append(numbers[0] * numbers[1])
    return sum(results)


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=3, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
