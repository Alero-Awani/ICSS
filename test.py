from app import Trie, cheapest_operator
import pytest

operators = Trie()
operators.insert({"1":0.92})

@pytest.mark.parametrize("test_input,expected", [("1",0.92)])
def test_trie_insert(test_input, expected):
    """test insert function """
    assert operators.lookup('1734567890') == expected


@pytest.mark.parametrize("test_input,expected", [("1",0.92)])
def test_trie_lookup(test_input, expected):
    # trie.insert({'1': 0.92})
    assert operators.lookup(test_input) == expected
    assert operators.lookup(test_input) is expected
    # assert trie.lookup('') is None
    


def test_cheapest_operator():
    operators_all = {
            'operatorA': operators,
        }
    number = '234567890'
    cheapest = cheapest_operator(number=number, operators=operators_all)
    assert cheapest[0] is None
