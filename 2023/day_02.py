"""
Advent of Code 2023, day 2
"""

import aocd

from re import match, findall
from collections import defaultdict
from dataclasses import dataclass


def solve():
    input = aocd.get_data(day=2, year=2023)
    print("Part 1:", solve_a(input))
    print("Part 2:", solve_b(input))


def solve_a(input: str) -> int:
    games = [to_game(line) for line in input.splitlines()]
    possible_games = [
        game
        for game in games
        if is_possible(game, max_red=12, max_green=13, max_blue=14)
    ]
    return sum([game.id for game in possible_games])


def solve_b(input: str) -> int:
    games = [to_game(line) for line in input.splitlines()]
    powers = [calculate_power(game) for game in games]
    return sum(powers)


@dataclass
class Game:
    id: int
    cube_counts: dict[str, list[int]]


def to_game(line: str) -> Game:
    id = parse_id(line)
    cube_counts = parse_cube_counts(line)
    return Game(id, cube_counts)


def parse_id(line: str) -> int:
    return int(match(r"Game (\d+):", line).group(1))


def parse_cube_counts(line: str) -> dict[str, list[int]]:
    matches = findall(r"(\d+) (red|green|blue)", line)
    cube_counts = defaultdict(list)
    for count, colour in matches:
        cube_counts[colour].append(int(count))
    return cube_counts


def is_possible(game: Game, max_red: int, max_green: int, max_blue: int) -> bool:
    return (
        all(count <= max_red for count in game.cube_counts["red"])
        and all(count <= max_green for count in game.cube_counts["green"])
        and all(count <= max_blue for count in game.cube_counts["blue"])
    )


def calculate_power(game: Game) -> int:
    red = max(game.cube_counts["red"])
    green = max(game.cube_counts["green"])
    blue = max(game.cube_counts["blue"])
    return red * green * blue


if __name__ == "__main__":
    solve()
