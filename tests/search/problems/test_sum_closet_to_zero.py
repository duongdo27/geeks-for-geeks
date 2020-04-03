from search.problems.sum_closest_to_zero import sum_closest_to_zero


def test1():
    array = [1, 2, 3, 4, 5, 6, 7, 9]
    assert sum_closest_to_zero(array) == (1, 2)


def test2():
    array = [1, -2, 3, -4, 6, -7, 7, 9]
    assert sum_closest_to_zero(array) == (-7, 7)


def test3():
    array = [1, 60, -10, 70, -80, 85]
    assert sum_closest_to_zero(array) == (-80, 85)