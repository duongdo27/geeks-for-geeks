from search.algorithms.jump_search import jump_search


def test_empty_array():
    array = []
    value = 4
    assert jump_search(array, value) == -1


def test_not_found():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 477
    assert jump_search(array, value) == -1


def test_not_found_bigger():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 777
    assert jump_search(array, value) == -1


def test_found():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 55
    assert jump_search(array, value) == 10


def test_found_first():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 0
    assert jump_search(array, value) == 0


def test_found_step():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 5
    assert jump_search(array, value) == 5


def test_found_last():
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    value = 610
    assert jump_search(array, value) == 15
