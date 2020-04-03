from search.algorithms.sublist_search import sublist_search


def test_empty_array():
    array1 = []
    array2 = [3]
    assert sublist_search(array1, array2) == True


def test_sublist_bigger_than_list():
    array1 = [3, 4]
    array2 = [3]
    assert sublist_search(array1, array2) == False


def test_not_found():
    array1 = [1, 2, 3, 6]
    array2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert sublist_search(array1, array2) == False


def test_found():
    array1 = [1, 2, 3, 5, 8]
    array2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert sublist_search(array1, array2) == True


def test_not_found_wrong_index():
    array1 = [1, 2, 3, 5, 13]
    array2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert sublist_search(array1, array2) == False


def test_found_end():
    array1 = [144, 233, 377, 610]
    array2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert sublist_search(array1, array2) == True


def test_not_found_end():
    array1 = [233, 377, 610, 777]
    array2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert sublist_search(array1, array2) == False
