"""
Advent of Code 2024, day 6
"""

import copy
from itertools import cycle
from typing import NamedTuple

import aocd
from utils import grid

type LabMap = grid.Grid[str]


class Step(NamedTuple):
    i: int
    j: int
    direction: grid.Direction


def solve_a(puzzle_input: str) -> int:
    lab_map = grid.create_grid(puzzle_input)
    steps = get_guard_steps(lab_map)[0]
    # we want to know how many distinct positions there are
    return len({(step.i, step.j) for step in steps})


def solve_b(puzzle_input: str) -> int:
    lab_map = grid.create_grid(puzzle_input)
    steps = get_guard_steps(lab_map)[0]
    obstruction_options = []

    # brute-force by trying all possible steps for obstacles
    # (skip the guard's starting position as they would notice!)
    for step in steps:
        if lab_map[step.i][step.j] == "^":
            continue
        altered_lab = copy.deepcopy(lab_map)
        altered_lab[step.i][step.j] = "#"
        status = get_guard_steps(altered_lab)[1]
        if status == "loop":
            obstruction_options.append(step)

    # again, we want to know how many distinct positions there are
    return len({(step.i, step.j) for step in obstruction_options})


def get_guard_steps(lab_map: LabMap) -> tuple[list[Step], str]:
    row_count, col_count = len(lab_map), len(lab_map[0])

    directions = cycle([grid.UP, grid.RIGHT, grid.DOWN, grid.LEFT])
    direction = next(directions)

    start_i, start_j, _ = grid.get_tiles(lab_map, lambda tile: tile.value == "^")[0]
    start = Step(start_i, start_j, direction)
    current = (start.i, start.j)
    steps = [start]
    status = "ok"

    while True:
        i, j = current[0] + direction[0], current[1] + direction[1]
        step = Step(i, j, direction)
        is_on_map = 0 <= i < row_count and 0 <= j < col_count
        if step in steps:
            status = "loop"
            break
        elif not is_on_map:
            break
        elif lab_map[i][j] == "#":
            # obstacle! just get next direction and try again
            direction = next(directions)
        else:
            steps.append(step)
            current = (i, j)

    return steps, status


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=6, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
