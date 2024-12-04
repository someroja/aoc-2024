"""
Advent of Code 2024, day 4
"""

import re
from itertools import repeat

import aocd


def solve_a(puzzle_input: str) -> int:
    lines = pad(puzzle_input, 3)
    count = sum(
        len(find_xmas_words(match.start(), line_number, lines))
        for line_number, line in enumerate(lines)
        for match in re.finditer("X", line)
    )
    return count


def pad(puzzle_input: str, amount: int) -> list[str]:
    """
    Add padding around the word puzzle edges to skip checking for... edge cases :)
    """
    lines = puzzle_input.splitlines()
    line_length = len(lines[0])

    # Pad left + right
    lr_padding = "." * amount
    padded_lines = [lr_padding + line + lr_padding for line in lines]

    # Pad top + bottom
    xy_padding = "." * (line_length + 2 * amount)
    for padding in repeat(xy_padding, amount):
        padded_lines.insert(0, padding)
        padded_lines.append(padding)

    return padded_lines


def find_xmas_words(start: int, row: int, lines: list[str]) -> list[str]:
    words = [
        # Left + right
        (lines[row][start - 3 : start + 1])[::-1],  # reversed
        lines[row][start : start + 4],
        # Top + bottom
        lines[row][start]
        + lines[row - 1][start]
        + lines[row - 2][start]
        + lines[row - 3][start],
        lines[row][start]
        + lines[row + 1][start]
        + lines[row + 2][start]
        + lines[row + 3][start],
        # Diagonals:
        # NE
        lines[row][start]
        + lines[row - 1][start + 1]
        + lines[row - 2][start + 2]
        + lines[row - 3][start + 3],
        # NW
        lines[row][start]
        + lines[row - 1][start - 1]
        + lines[row - 2][start - 2]
        + lines[row - 3][start - 3],
        # SE
        lines[row][start]
        + lines[row + 1][start + 1]
        + lines[row + 2][start + 2]
        + lines[row + 3][start + 3],
        # SW
        lines[row][start]
        + lines[row + 1][start - 1]
        + lines[row + 2][start - 2]
        + lines[row + 3][start - 3],
    ]
    return [word for word in words if word == "XMAS"]


def solve_b(puzzle_input: str) -> int:
    lines = pad(puzzle_input, 1)
    count = len(
        [
            match
            for line_number, line in enumerate(lines)
            for match in re.finditer("A", line)
            if is_x_mas(match.start(), line_number, lines)
        ]
    )
    return count


def is_x_mas(start: int, row: int, lines: list[str]) -> bool:
    """
    This isn't actually an XMAS puzzle; it's an X-MAS puzzle!
    """
    diagonals = [
        lines[row - 1][start - 1] + lines[row][start] + lines[row + 1][start + 1],
        lines[row - 1][start + 1] + lines[row][start] + lines[row + 1][start - 1],
    ]
    return all(diagonal == "MAS" or diagonal == "SAM" for diagonal in diagonals)


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=4, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
