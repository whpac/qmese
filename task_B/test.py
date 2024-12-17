import pytest
from b import isBalanced

@pytest.mark.parametrize("tree, expected", [
    (None, True),
    ([None, None], True),
    ([[None, None], [None, None]], True),
    ([[[None, None], None], [None, None]], True),
    ([[[None, None], [None, None]], [None, None]], True),
    ([[[None, None], None], None], False),
    ([[None, [None, None]], [None, None]], True),
    ([[None, [None, None]], None], False),
    ([[[None, None], [None, None]], [[None, None], [None, None]]], True),
    ([[[None, None], [None, None]], [None, None]], True)
])
def test_isBalanced(tree, expected):
    assert isBalanced(tree) == expected