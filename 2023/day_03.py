"""
Advent of Code 2023, day 3
"""

import aocd

from re import Match, finditer


def solve():
    input = aocd.get_data(day=3, year=2023)
    print("Part 1:", solve_a(input))
    print("Part 2:", solve_b(input))


def solve_a(input: str) -> int:
    lines = input.splitlines()
    matches_per_line = [find_digits(line) for line in lines]
    part_numbers = [
        int(match.group())
        for line_number, matches in enumerate(matches_per_line)
        for match in matches
        if has_surrounding_symbols(lines, line_number, match.start(), match.end())
    ]
    return sum(part_numbers)


def solve_b(input: str) -> int:
    pass


def find_digits(line: str) -> list[Match[str]]:
    return list(finditer(r"\d+", line))


def find_surrounding_symbols(
    lines: list[str], line_number: int, start: int, end: int
) -> list[str]:
    parts: list[str] = []

    if line_number > 0:
        top_part = lines[line_number - 1][max(start - 1, 0) : end + 1]
        parts.append(top_part)

    left_part = lines[line_number][max(start - 1, 0) : start]
    parts.append(left_part)

    right_part = lines[line_number][end : end + 1]
    parts.append(right_part)

    if line_number < len(lines) - 1:
        bottom_part = lines[line_number + 1][max(start - 1, 0) : end + 1]
        parts.append(bottom_part)

    symbols = [c for c in "".join(parts) if not c.isdigit() and c != "."]
    return symbols


def has_surrounding_symbols(
    lines: list[str], line_number: int, start: int, end: int
) -> bool:
    return len(find_surrounding_symbols(lines, line_number, start, end)) > 0


if __name__ == "__main__":
    solve()
