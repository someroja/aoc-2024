"""
Advent of Code 2024, day 7
"""

import re
from itertools import product

import aocd


def solve_a(puzzle_input: str) -> int:
    lines = puzzle_input.splitlines()
    operators = ["+", "*"]
    correct_values = []

    for line in lines:
        test_value, initial_value, *values = [int(d) for d in re.findall(r"\d+", line)]
        possible_configurations = list(product(operators, repeat=len(values)))
        for config in possible_configurations:
            # let's zip config and values to get tuples of operations to apply to the initial value
            operations = list(zip(config, values))
            result = initial_value
            for op in operations:
                match op[0]:
                    case "+":
                        result += op[1]
                    case "*":
                        result *= op[1]
            if result == test_value:
                correct_values.append(result)
                break

    return sum(correct_values)


def solve_b(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=7, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
