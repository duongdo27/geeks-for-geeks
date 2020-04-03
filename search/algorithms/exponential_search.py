"""
Link: https://www.geeksforgeeks.org/exponential-search/
"""
# pylint: disable=inconsistent-return-statements
# pylint: disable=invalid-name
from search.algorithms.binary_search import binary_recursive_search


def exponential_search(array, value):
    """
    :param array: list of values
    :param value: value to search for
    :return: index of the value
    If not found, return -1

    Time complexity: O(sqrt(n))
    """
    n = len(array)
    if n == 0:
        return -1

    # Loop through the lis
    idx = 0
    while True:
        number = array[idx]
        # Found the value
        if number == value:
            return idx

        # If jump through the value, run binary search from the last index/2 to current index
        if number > value:
            return binary_recursive_search(array, value, idx // 2, idx - 1)

        # Not found through the whole list
        if idx >= n - 1:
            return -1

        # Exponent by 2
        idx = min(idx * 2 + 1, n - 1)
