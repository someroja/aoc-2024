"""
Advent of Code 2024, day 12
"""

import aocd

from aoc_utils import grid


def solve_a(puzzle_input: str) -> int:
    garden = grid.create_grid(puzzle_input)
    regions = grid.get_all_regions(garden)
    prices = [len(region.tiles) * grid.get_perimeter(region) for region in regions]
    return sum(prices)


def solve_b(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=12, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
