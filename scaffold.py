from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from textwrap import dedent


def scaffold(year: int, day: int):
    project_root = Path(__file__).parent.resolve()
    solution_dir = project_root / f"aoc_{year}"
    test_dir = project_root / f"tests/aoc_{year}"

    check_dir(solution_dir)
    check_dir(test_dir)

    solution_file = solution_dir / f"day_{day:02d}.py"
    test_file = test_dir / f"day_{day:02d}_test.py"

    solution_template = dedent(
        f'''\
        """
        Advent of Code {year}, day {day}
        """

        import aocd


        def solve_a(puzzle_input: str) -> int:
            pass


        def solve_b(puzzle_input: str) -> int:
            pass


        if __name__ == "__main__":
            puzzle_input = aocd.get_data(day={day}, year={year})
            print(solve_a(puzzle_input))
            print(solve_b(puzzle_input))
        '''
    )

    test_template = dedent(
        f'''\
        from textwrap import dedent

        import pytest

        from aoc_{year} import day_{day}

        @pytest.fixture
        def puzzle_input() -> str:
            return dedent(
                """\\

                """
            )


        @pytest.mark.skip
        def test_solve_a(puzzle_input: str):
            assert day_{day}.solve_a(puzzle_input) == "??"


        @pytest.mark.skip
        def test_solve_b(puzzle_input: str):
            assert day_{day}.solve_b(puzzle_input) == "??"
        '''
    )

    write_file(solution_file, solution_template)
    write_file(test_file, test_template)


def check_dir(path: Path):
    if not path.exists():
        path.mkdir()
        init = path / "__init__.py"
        init.touch()
        print(f"Created {path}")
    elif not path.is_dir():
        print(f"Skipping {path}: Path exists, but it is not a directory")


def write_file(file: Path, template: str):
    if file.exists():
        print(f"Skipping {file}: File exists")
    else:
        file.write_text(template)
        print(f"Created {file}")


def main():
    parser = ArgumentParser(description="Scaffold Advent of Code solution")
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=datetime.now().year,
        help="year, default is current year",
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        default=datetime.now().day,
        help="day number, default is today",
    )

    # TODO: some validation for year and day
    args = parser.parse_args()

    try:
        scaffold(args.year, args.day)
    except Exception as err:
        parser.error(str(err))


if __name__ == "__main__":
    main()
