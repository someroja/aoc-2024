import textwrap

import day_02


def test_parse_id():
    assert day_02.parse_id("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue") == 1
    assert day_02.parse_id("Game 23: 3 blue, 4 red; 1 red, 2 green, 6 blue") == 23
    assert day_02.parse_id("Game 999: 3 blue, 4 red; 1 red, 2 green, 6 blue") == 999


def test_parse_cube_counts():
    puzzle_input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue"
    expected = {"red": [4, 1], "green": [2], "blue": [3, 6]}
    assert day_02.parse_cube_counts(puzzle_input) == expected


def test_possible_game():
    game = day_02.to_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert day_02.is_possible(game, max_red=12, max_green=13, max_blue=14)


def test_impossible_game():
    game = day_02.to_game(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    assert not day_02.is_possible(game, max_red=12, max_green=13, max_blue=14)


def test_solve_a():
    puzzle_input = textwrap.dedent(
        """\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
    )
    assert day_02.solve_a(puzzle_input) == 8


def test_calculate_power():
    game_1 = day_02.to_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert day_02.calculate_power(game_1) == 48

    game_2 = day_02.to_game(
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    )
    assert day_02.calculate_power(game_2) == 12

    game_3 = day_02.to_game(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    assert day_02.calculate_power(game_3) == 1560


def test_solve_b():
    puzzle_input = textwrap.dedent(
        """\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
    )
    assert day_02.solve_b(puzzle_input) == 2286
