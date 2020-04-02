from search.algorithms.interpolation_search import interpolation_search


def test_empty_array():
    array = []
    value = 4
    assert interpolation_search(array, value) == -1


def test_not_found():
    array = [1, 2, 3]
    value = 4
    assert interpolation_search(array, value) == -1


def test_middle():
    array = [1, 2, 3]
    value = 2
    assert interpolation_search(array, value) == 1


def test_left():
    array = [1, 2, 3, 4, 5]
    value = 1
    assert interpolation_search(array, value) == 0


def test_left2():
    array = [1, 2, 3, 4, 5]
    value = 2
    assert interpolation_search(array, value) == 1


def test_right():
    array = [1, 2, 3, 4, 5]
    value = 4
    assert interpolation_search(array, value) == 3


def test_right2():
    array = [1, 2, 3, 4, 5]
    value = 5
    assert interpolation_search(array, value) == 4


def test_long_sequence():
    array = [1, 2, 3, 4, 5]
    value = 5
    assert interpolation_search(array, value) == 4