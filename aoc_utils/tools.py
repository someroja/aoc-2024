from collections import defaultdict
from collections.abc import Callable, Iterable


def groupby[T, K](
    iterable: Iterable[T], key: Callable[[T], K] = lambda item: item
) -> dict[K, list[T]]:
    groups = defaultdict(list)
    for item in iterable:
        groups[key(item)].append(item)
    return dict(groups)
