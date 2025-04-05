"""
Advent of Code 2024, day 7
"""

from typing import NamedTuple

import aocd
import numpy as np
from numpy.typing import NDArray

TopoMap = NDArray[np.int_]


class Position(NamedTuple):
    i: np.int_
    j: np.int_
    height: np.int_


Trail = list[Position]


def solve_a(puzzle_input: str) -> int:
    topo_map = get_topo_map(puzzle_input)
    trailheads = find_trailheads(topo_map)
    scores = []
    for trailhead in trailheads:
        peaks = find_all_peaks(trailhead, topo_map)
        scores.append(len(peaks))
    return sum(scores)


def get_topo_map(puzzle_input: str) -> TopoMap:
    lines = puzzle_input.splitlines()
    topo_map = np.array([list(line) for line in lines]).astype(np.int_)
    return topo_map


def find_trailheads(topo_map: TopoMap) -> list[Position]:
    coords = np.nonzero(topo_map == 0)
    trailhead_positions = [
        Position(i, j, np.int_(0)) for i, j in list(zip(coords[0], coords[1]))
    ]
    return trailhead_positions


def find_all_peaks(pos: Position, topo_map: TopoMap) -> set[Position]:
    peaks = set()

    for neighbour in get_neighbours(pos, topo_map):
        if neighbour.height == 9:
            peaks.add(neighbour)
        else:
            peaks.update(find_all_peaks(neighbour, topo_map))

    return peaks


def get_neighbours(pos: Position, topo_map: TopoMap) -> list[Position]:
    neighbours = []

    # Hiking trails never include diagonal steps - only up, down, left, or right
    directions = np.array([[1, 0], [-1, 0], [0, -1], [0, 1]])

    for direction in directions:
        # For a good hiking trail neighbour has to increase by a height of exactly 1
        # (and it has to be on the map as well!)
        i, j = np.array([pos.i, pos.j]) + direction
        if 0 <= i < topo_map.shape[0] and 0 <= j < topo_map.shape[1]:
            # We are on the map, so we can index the height
            height = np.int_(topo_map[i][j])
            if height == pos.height + 1:
                neighbours.append(Position(i, j, height))

    return neighbours


def solve_b(puzzle_input: str) -> int:
    topo_map = get_topo_map(puzzle_input)
    trailheads = find_trailheads(topo_map)
    ratings = []
    for trailhead in trailheads:
        trails = find_all_trails(trailhead, topo_map)
        ratings.append(len(trails))
    return sum(ratings)


def find_all_trails(
    current: Position, topo_map: TopoMap, trail: Trail | None = None
) -> list[Trail]:
    if trail is None:
        trail = [current]

    trails = []

    if current.height == 9:
        # Return a good trail
        trails.append(trail)
    else:
        for neighbour in get_neighbours(current, topo_map):
            trails.extend(find_all_trails(neighbour, topo_map, [*trail, neighbour]))

    return trails


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=10, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
