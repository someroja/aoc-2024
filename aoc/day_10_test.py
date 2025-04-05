import textwrap

import numpy as np

from aoc import day_10

puzzle_input = textwrap.dedent(
    """\
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
)


def test_solve_a():
    assert day_10.solve_a(puzzle_input) == 36


def test_find_trailheads():
    topo_map = day_10.get_topo_map(puzzle_input)
    assert len(day_10.find_trailheads(topo_map)) == 9


def test_get_neighbours_from_trailhead():
    topo_map = day_10.get_topo_map(puzzle_input)
    trailhead = day_10.Position(np.int_(0), np.int_(2), np.int_(0))
    neighbours = day_10.get_neighbours(trailhead, topo_map)
    assert len(neighbours) == 2
    assert day_10.Position(np.int_(0), np.int_(3), np.int_(1)) in neighbours
    assert day_10.Position(np.int_(1), np.int_(2), np.int_(1)) in neighbours


def test_get_neighbours_from_peak():
    topo_map = day_10.get_topo_map(puzzle_input)
    peak = day_10.Position(np.int_(9), np.int_(4), np.int_(9))
    neighbours = day_10.get_neighbours(peak, topo_map)
    assert len(neighbours) == 0


def test_find_all_peaks_small():
    topo_map = day_10.get_topo_map(
        textwrap.dedent(
            """\
        0123
        1234
        8765
        9876
        """
        )
    )
    trailhead = day_10.Position(np.int_(0), np.int_(0), np.int_(0))
    peaks = day_10.find_all_peaks(trailhead, topo_map)
    assert len(peaks) == 1


def test_find_all_peaks():
    topo_map = day_10.get_topo_map(puzzle_input)
    trailhead = day_10.Position(np.int_(0), np.int_(2), np.int_(0))
    peaks = day_10.find_all_peaks(trailhead, topo_map)
    assert len(peaks) == 5


def test_solve_b():
    assert day_10.solve_b(puzzle_input) == 81


def test_find_all_trails():
    topo_map = day_10.get_topo_map(puzzle_input)
    trailhead = day_10.Position(np.int_(0), np.int_(2), np.int_(0))
    trails = day_10.find_all_trails(trailhead, topo_map)
    assert len(trails) == 20
