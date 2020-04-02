from search.algorithms.binary_search import binary_search


def test_empty_array():
    array = []
    value = 4
    assert binary_search(array, value) == -1


def test_not_found():
    array = [1, 2, 3]
    value = 4
    assert binary_search(array, value) == -1


def test_middle():
    array = [1, 2, 3]
    value = 2
    assert binary_search(array, value) == 1


def test_left():
    array = [1, 2, 3, 4, 5]
    value = 1
    assert binary_search(array, value) == 0


def test_left2():
    array = [1, 2, 3, 4, 5]
    value = 2
    assert binary_search(array, value) == 1


def test_right():
    array = [1, 2, 3, 4, 5]
    value = 4
    assert binary_search(array, value) == 3


def test_right2():
    array = [1, 2, 3, 4, 5]
    value = 5
    assert binary_search(array, value) == 4
