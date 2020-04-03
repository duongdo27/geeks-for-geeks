from search.problems.find_missing_number import find_missing_number


def test1():
    array = [1, 2, 3, 4, 5, 6, 7, 9]
    assert find_missing_number(array) == 8


def test2():
    array = [1, 2, 3, 4, 6, 7, 8, 9]
    assert find_missing_number(array) == 5