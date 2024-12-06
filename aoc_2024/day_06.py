"""
Advent of Code 2024, day 6
"""

from itertools import cycle

import aocd


def solve_a(puzzle_input: str) -> int:
    path = get_path(puzzle_input)
    # we want to know how distinct positions there are
    return len(set(path))


def get_path(puzzle_input: str) -> list[tuple[int, int, str]]:
    # use the padding trick again
    lab_map = [["!", *row, "!"] for row in puzzle_input.splitlines()]
    pad_row = list("!" * len(lab_map[0]))
    lab_map.insert(0, pad_row)
    lab_map.append(pad_row)

    start = find_guard(lab_map)
    path = walk(start, lab_map)

    return path


def find_guard(lab_map: list[list[str]]) -> tuple[int, int]:
    # maybe there can be multiple guards in the lab?
    guards = [
        (i, j)
        for i, row in enumerate(lab_map)
        for j, value in enumerate(row)
        if value == "^"  # assuming guards start facing north
    ]
    return guards[0]


def walk(
    start: tuple[int, int], lab_map: list[list[str]]
) -> list[tuple[int, int, str]]:
    directions = cycle(["^", ">", "v", "<"])
    direction = next(directions)
    i = start[0]
    j = start[1]
    path = [(i, j, direction)]
    ahead = "?"

    while ahead != "!":
        next_i, next_j = next_step(i, j, direction)
        ahead = lab_map[next_i][next_j]
        if ahead == "." or ahead == "^":
            i = next_i
            j = next_j
            path.append((i, j, direction))
        elif ahead == "#":
            direction = next(directions)

    return path


def next_step(i: int, j: int, direction: str) -> tuple[int, int]:
    match direction:
        case "^":
            return i - 1, j
        case "v":
            return i + 1, j
        case "<":
            return i, j - 1
        case ">":
            return i, j + 1
        case _:
            return i, j


def solve_b(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=6, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
