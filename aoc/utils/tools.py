from collections import defaultdict
from collections.abc import Callable, Iterable


def to_sections(puzzle_input: str) -> list[str]:
    return puzzle_input.split("\n\n")


def groupby[T, K](
    iterable: Iterable[T], key: Callable[[T], K] = lambda item: item
) -> dict[K, list[T]]:
    groups = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    return dict(groups)
