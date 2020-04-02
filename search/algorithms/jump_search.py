"""
Link: https://www.geeksforgeeks.org/jump-search/
"""
from linear_search import linear_search


def jump_search(array, value):
    """
    :param array: list of values
    :param value: value to search for
    :param step: number of step to jump
    :return: index of the value
    If not found, return -1

    Time complexity: O(n)
    """
    step = 5
    last_index = 0
    for i in range(0, len(array), step):
        if array[i] == value:
            return i
        elif array[i] > value:
            linear_search(array[last_index:i], value)
        last_index = i



