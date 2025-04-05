"""
Advent of Code 2024, day 8
"""

from itertools import permutations

import aocd
from utils import grid, tools


def solve_a(puzzle_input: str) -> int:
    antinodes = set()
    antenna_map = grid.create_grid(puzzle_input)
    antennas_by_freq = tools.groupby(
        grid.get_tiles(antenna_map, lambda tile: tile.value.isalnum()),
        lambda tile: tile.value,
    )

    for antennas in antennas_by_freq.values():
        for antenna_a, antenna_b in permutations(antennas, 2):
            delta_i = antenna_b.i - antenna_a.i
            delta_j = antenna_b.j - antenna_a.j

            antinode_a = antenna_a.i - delta_i, antenna_a.j - delta_j
            if grid.is_in_bounds(antinode_a, antenna_map):
                antinodes.add(antinode_a)

            antinode_b = antenna_b.i + delta_i, antenna_b.j + delta_j
            if grid.is_in_bounds(antinode_b, antenna_map):
                antinodes.add(antinode_b)

    return len(antinodes)


def solve_b(puzzle_input: str) -> int:
    antinodes = set()
    antenna_map = grid.create_grid(puzzle_input)
    antennas_by_freq = tools.groupby(
        grid.get_tiles(antenna_map, lambda tile: tile.value.isalnum()),
        lambda tile: tile.value,
    )

    for antennas in antennas_by_freq.values():
        for antenna_a, antenna_b in permutations(antennas, 2):
            delta_i = antenna_b.i - antenna_a.i
            delta_j = antenna_b.j - antenna_a.j

            # go backwards from A
            current = (antenna_a.i, antenna_a.j)
            while grid.is_in_bounds(current, antenna_map):
                antinodes.add(current)
                current = current[0] - delta_i, current[1] - delta_j

            # go forwards from B
            current = (antenna_b.i, antenna_b.j)
            while grid.is_in_bounds(current, antenna_map):
                antinodes.add(current)
                current = current[0] + delta_i, current[1] + delta_j

    return len(antinodes)


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=8, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
