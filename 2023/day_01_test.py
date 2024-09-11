import day_01


def test_solve_a():
    input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    assert day_01.solve_a(input) == 142


def test_b_regex():
    assert day_01.parse_line("7eightwone") == [7, 8, 2, 1]
    assert day_01.parse_line("two1nine") == [2, 1, 9]
    assert day_01.parse_line("eightwothree") == [8, 2, 3]
    assert day_01.parse_line("abcone2threexyz") == [1, 2, 3]
    assert day_01.parse_line("xtwone3four") == [2, 1, 3, 4]
    assert day_01.parse_line("4nineeightseven2") == [4, 9, 8, 7, 2]
    assert day_01.parse_line("zoneight234") == [1, 8, 2, 3, 4]
    assert day_01.parse_line("7pqrstsixteen") == [7, 6]


def test_solve_b():
    input = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    assert day_01.solve_b(input) == 281
