"""
Advent of Code 2024, day 19
"""

import aocd


def solve_a(puzzle_input: str) -> int:
    patterns, designs = parse(puzzle_input)
    possible_desings = [
        design for design in designs if count_arrangements(design, patterns) > 0
    ]
    return len(possible_desings)


def solve_b(puzzle_input: str) -> int:
    patterns, designs = parse(puzzle_input)
    total = sum(count_arrangements(design, patterns) for design in designs)
    return total


def parse(puzzle_input: str) -> tuple[list[str], list[str]]:
    patterns_input, designs_input = puzzle_input.split("\n\n")
    patterns = patterns_input.split(", ")
    designs = designs_input.splitlines()
    return patterns, designs


def count_arrangements(design: str, patterns: list[str]) -> int:
    n = len(design) + 1
    arrangement_counts = [0] * n

    # Only one way to do nothing :)
    arrangement_counts[0] = 1

    for i in range(n):
        count = arrangement_counts[i]
        if count > 0:
            for pattern in patterns:
                if design[i:].startswith(pattern):
                    arrangement_counts[i + len(pattern)] += count

    return arrangement_counts[-1]


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=19, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
