"""
Link: https://www.geeksforgeeks.org/sublist-search-search-a-linked-list-in-another-list/
"""
# pylint: disable=invalid-name


def check_is_contained(array1, array2, start_idx):
    """
    :param array1: sublist
    :param array2: list
    :param start_idx: the start index used to search
    :return: Whether list contains sublist
    Time complexity: O(n * m)
    """
    n = len(array2)
    for idx, value in enumerate(array1):
        if start_idx + idx >= n:
            return False
        if value != array2[start_idx + idx]:
            return False
    return True


def sublist_search(array1, array2):
    """
    :param array1: sublist
    :param array2: list
    :return: Whether list contains sublist
    Time complexity: O(n * m)
    """
    # Empty array
    if len(array1) == 0:
        return True

    for start_idx in range(len(array2)):
        if check_is_contained(array1, array2, start_idx):
            return True
    return False
