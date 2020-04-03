"""
Link: https://www.geeksforgeeks.org/find-the-missing-number/
"""
# pylint: disable=invalid-name


def find_missing_number(array):
    """
    :param array: given integer array from 1 to len(array), missing one of value
    :return: The missing value
    Method: Using sum of list plus missing number subtract the list of the given array
    Complexity: O(n)
    """
    n = len(array)
    expected_sum = (n + 1) * (n + 2) // 2
    return expected_sum - sum(array)
