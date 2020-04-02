from search.algorithms.jump_search import jump_search


def test_not_found():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 477
    assert jump_search(array, value) == -1


def test_found():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 55
    assert jump_search(array, value) == 11
