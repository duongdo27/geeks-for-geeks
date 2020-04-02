from search.algorithms.linear_search import linear_search


def test_empty_array():
    array = []
    value = 4
    assert linear_search(array, value) == -1


def test_not_found():
    array = [1, 2, 3]
    value = 4
    assert linear_search(array, value) == -1


def test_found():
    array = [1, 2, 3]
    value = 2
    assert linear_search(array, value) == 1
