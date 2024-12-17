import pytest
from a import getDistance

@pytest.mark.parametrize("graph, destNode, expected", [
    ([
        [False, True, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, True],
        [False, False, False, False, True],
        [False, False, False, False, False]
    ], 4, 2),
    ([
        [False, True, True, False],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, False, False]
    ], 3, 2),
    ([
        [False, True, False, False, False],
        [False, False, True, False, False],
        [False, False, False, True, False],
        [False, False, False, False, True],
        [False, False, False, False, False]
    ], 4, 4),
    ([
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, False, False]
    ], 2, 2),
    ([
        [False, True, True, True],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ], 3, 1),
    ([
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, False, False]
    ], 1, 1),
    ([
        [False, True, True, False],
        [False, False, False, True],
        [False, False, False, True],
        [False, False, False, False]
    ], 3, 2),
    ([
        [False, True, False, False],
        [False, False, True, True],
        [False, False, False, True],
        [False, False, False, False]
    ], 3, 2),
    ([
        [False, True, True, True],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ], 2, 1),
    ([
        [False, True, True, False],
        [False, False, False, True],
        [False, False, False, False],
        [False, False, False, False]
    ], 1, 1)
])
def test_getDistance(graph, destNode, expected):
    assert getDistance(graph, destNode) == expected