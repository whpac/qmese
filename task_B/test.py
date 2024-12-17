import pytest
from b import isBalanced

@pytest.mark.parametrize("tree, expected", [
    (None, True),  # Empty tree
    ([None, None], True),  # Single node tree
    ([[None, None], [None, None]], True),  # Balanced tree with two levels
    ([[[None, None], None], [None, None]], True),  # Balanced tree with three levels
    ([[[None, None], [None, None]], [None, None]], True),  # Balanced tree with three levels
    ([[[None, None], None], None], False),  # Unbalanced tree with three levels
    ([[None, [None, None]], [None, None]], True),  # Balanced tree with three levels
    ([[None, [None, None]], None], False),  # Unbalanced tree with three levels
    ([[[None, None], [None, None]], [[None, None], [None, None]]], True),  # Balanced tree with four levels
    ([[[None, None], [None, None]], [None, None]], True)  # Balanced tree with three levels
])
def test_isBalanced(tree, expected):
    assert isBalanced(tree) == expected