from search.problems.median_two_sorted_array import median_of_two_sorted_array


def test_one_less_two():
    array1 = [1, 2, 3, 4, 5]
    array2 = [6, 7, 8, 9, 10]
    assert median_of_two_sorted_array(array1, array2) == 5.5


def test_two_less_one():
    array2 = [1, 2, 3, 4, 5, 6]
    array1 = [7, 8, 9, 10, 11, 12]
    assert median_of_two_sorted_array(array1, array2) == 6.5


def test_normal():
    array1 = [1, 12, 15, 26, 38]
    array2 = [2, 13, 17, 30, 45]
    assert median_of_two_sorted_array(array1, array2) == 16.0


def test_invalid():
    array1 = [1, 12, 15, 26, 38, 50]
    array2 = [2, 13, 17, 30, 45]
    assert median_of_two_sorted_array(array1, array2) == "Invalid input"
