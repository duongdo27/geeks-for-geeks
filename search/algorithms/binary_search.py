"""
Link: https://www.geeksforgeeks.org/binary-search/
"""
# pylint: disable=inconsistent-return-statements


def binary_recursive_search(array, value, left, right):
    """
    :param array: list of values
    :param value: value to search for
    :param left: value in the left margin
    :param right: value in the right margin
    :return: index of the value
    If not found, return -1

    Time complexity: O(log(n))
    """
    # base case when recursive list minimized to empty
    if left > right:
        return -1

    # Choose the middle value
    mid = (left + right) // 2

    # Found the value
    if value == array[mid]:
        return mid

    # if value less than the middle point, recursive the left part
    if value < array[mid]:
        return binary_recursive_search(array, value, left, mid - 1)

    # if value bigger than the middle point, recursive the right part
    if value > array[mid]:
        return binary_recursive_search(array, value, mid + 1, right)


def binary_search(array, value):
    """
    :param array: list of values
    :param value: value to search for
    :return: index of the value
    If not found, return -1

    Time complexity: O(log(n))
    """
    return binary_recursive_search(array, value, 0, len(array) - 1)
