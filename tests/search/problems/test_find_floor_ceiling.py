from search.problems.find_floor_ceiling import find_floor_ceiling


def test_no_floor():
    array = [1, 2, 8, 10, 10, 12, 19]
    number = 0
    assert find_floor_ceiling(array, number) == ('None', 1)


def test_in_array():
    array = [1, 2, 8, 10, 10, 12, 19]
    number = 8
    assert find_floor_ceiling(array, number) == (8, 8)


def test_in_range_array():
    array = [1, 2, 8, 10, 10, 12, 19]
    number = 5
    assert find_floor_ceiling(array, number) == (2, 8)


def test_no_ceiling():
    array = [1, 2, 8, 10, 10, 12, 19]
    number = 20
    assert find_floor_ceiling(array, number) == (19, 'None')
