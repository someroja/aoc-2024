"""
Advent of Code 2024, day 17
"""

import re
from dataclasses import dataclass, replace
from typing import List

import aocd


@dataclass(frozen=True)
class State:
    pointer: int
    a: int
    b: int
    c: int
    program: List[int]
    output: List[int]


def solve_a(puzzle_input: str) -> str:
    init_state = init(puzzle_input)
    final_state = compute(init_state)
    return ",".join([str(value) for value in final_state.output])


def solve_b(puzzle_input: str) -> int:
    # Find initial state to create a quine
    # TODO: Brute-force not really cutting it here...
    init_state = init(puzzle_input)
    a = 0
    while True:
        state = compute(replace(init_state, a=a))
        if state.program == state.output:
            break
        a += 1
    return a


def init(puzzle_input: str) -> State:
    lines = puzzle_input.splitlines()
    a = int(re.findall(r"\d+", lines[0])[0])
    b = int(re.findall(r"\d+", lines[1])[0])
    c = int(re.findall(r"\d+", lines[2])[0])
    program = [int(match) for match in re.findall(r"\d", lines[4])]
    return State(0, a, b, c, program, [])


def compute(state: State) -> State:
    while True:
        pointer, program = state.pointer, state.program

        if pointer >= len(program):
            break

        opcode = program[pointer]
        operand = program[pointer + 1]

        match opcode:
            case 0:
                state = adv(operand, state)
            case 1:
                state = bxl(operand, state)
            case 2:
                state = bst(operand, state)
            case 3:
                state = jnz(operand, state)
            case 4:
                state = bxc(state)
            case 5:
                state = out(operand, state)
            case 6:
                state = bdv(operand, state)
            case 7:
                state = cdv(operand, state)

        if state.pointer == pointer:
            # No jump, so advance pointer
            state = replace(state, pointer=state.pointer + 2)

    return state


def adv(combo_operand: int, state: State) -> State:
    value = evaluate_combo_operand(combo_operand, state)
    return replace(state, a=state.a // (2**value))


def bdv(combo_operand: int, state: State) -> State:
    value = evaluate_combo_operand(combo_operand, state)
    return replace(state, b=state.a // (2**value))


def cdv(combo_operand: int, state: State) -> State:
    value = evaluate_combo_operand(combo_operand, state)
    return replace(state, c=state.a // (2**value))


def bxl(literal_operand: int, state: State) -> State:
    return replace(state, b=state.b ^ literal_operand)


def bst(combo_operand: int, state: State) -> State:
    value = evaluate_combo_operand(combo_operand, state)
    return replace(state, b=value % 8)


def jnz(literal_operand: int, state: State) -> State:
    return state if state.a == 0 else replace(state, pointer=literal_operand)


def bxc(state: State) -> State:
    return replace(state, b=state.b ^ state.c)


def out(combo_operand: int, state: State) -> State:
    value = evaluate_combo_operand(combo_operand, state)
    return replace(state, output=[*state.output, value % 8])


def evaluate_combo_operand(combo_operand: int, state: State) -> int:
    match combo_operand:
        case 7:
            raise ValueError("Combo operand 7 is reserved")
        case 6:
            return state.c
        case 5:
            return state.b
        case 4:
            return state.a
        case _:
            return combo_operand


if __name__ == "__main__":
    puzzle_input = aocd.get_data(day=17, year=2024)
    print(solve_a(puzzle_input))
    print(solve_b(puzzle_input))
