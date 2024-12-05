"""
Advent of Code 2024, day 5
"""

import re

import aocd


def solve_a(puzzle_input: str) -> int:
    ruleData, updateData = puzzle_input.split("\n\n")
    rules = ruleData.splitlines()
    updates = updateData.splitlines()

    middle_pages: list[int] = []

    for update in updates:
        if is_correct_order(update, rules):
            pages = update.split(",")
            index = (len(pages) - 1) // 2
            middle_pages.append(int(pages[index]))

    return sum(middle_pages)


def is_correct_order(update: str, rules: list[str]) -> bool:
    for rule in rules:
        parts = rule.split("|")
        left_part = parts[0]
        right_part = parts[1]
        # right part cannot be before left
        match = re.search(right_part + ",.*" + left_part, update)
        if match is not None:
            return False
    return True


def solve_b(puzzle_input: str) -> int:
    ruleData, updateData = puzzle_input.split("\n\n")
    rules = ruleData.splitlines()
    updates = updateData.splitlines()

    middle_pages: list[int] = []

    for update in updates:
        pages = [int(page) for page in update.split(",")]
        sorted_pages = sort_pages(pages, rules)

        if pages != sorted_pages:
            index = (len(sorted_pages) - 1) // 2
            middle_pages.append(sorted_pages[index])

    return sum(middle_pages)


def sort_pages(pages: list[int], rules: list[str]) -> list[int]:
    sorted_pages = list(pages)

    for rule in rules:
        parts = rule.split("|")
        left_part = int(parts[0])
        right_part = int(parts[1])
        try:
            index_l = sorted_pages.index(left_part)
            index_r = sorted_pages.index(right_part)
            # right part cannot be before left
            if index_r < index_l:
                sorted_pages.insert(index_r, sorted_pages.pop(index_l))
                break
        except ValueError:
            continue

    # if any sorting happened, we need to run another pass
    return pages if pages == sorted_pages else sort_pages(sorted_pages, rules)


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=5, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
