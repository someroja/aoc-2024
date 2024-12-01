"""
Advent of Code 2023, day 1
"""

import re

import aocd


def solve():
    puzzle_input = aocd.get_data(day=1, year=2023)
    print("Part 1:", solve_a(puzzle_input))
    print("Part 2:", solve_b(puzzle_input))


def solve_a(puzzle_input: str) -> int:
    lines = puzzle_input.splitlines()
    calibration_sum = sum([calibration_value(line) for line in lines])
    return calibration_sum


def calibration_value(line: str) -> int:
    digits = [c for c in line if c.isdigit()]
    first = digits[0]
    last = digits[-1]
    return int(first + last)


def solve_b(puzzle_input: str) -> int:
    lines = [parse_line(line) for line in puzzle_input.splitlines()]
    calibration_sum = sum([int(f"{line[0]}{line[-1]}") for line in lines])
    return calibration_sum


def parse_line(line: str) -> list[int]:
    # We need overlapping matches, so cannot use findall as it returns all non-overlapping matches :(
    return [
        parse_digit(match.group(1))
        for match in re.finditer(
            "(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))", line
        )
    ]


def parse_digit(s: str) -> int:
    match s:
        case "1" | "one":
            return 1
        case "2" | "two":
            return 2
        case "3" | "three":
            return 3
        case "4" | "four":
            return 4
        case "5" | "five":
            return 5
        case "6" | "six":
            return 6
        case "7" | "seven":
            return 7
        case "8" | "eight":
            return 8
        case "9" | "nine":
            return 9
        case _:
            raise ValueError("Not a valid digit")


if __name__ == "__main__":
    solve()
