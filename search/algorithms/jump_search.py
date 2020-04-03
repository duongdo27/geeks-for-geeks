"""
Link: https://www.geeksforgeeks.org/jump-search/
"""
# pylint: disable=invalid-name
import math


def jump_search(array, value):
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

    # Choose the step to jump
    step = int(math.sqrt(n))

    # Loop through the list with step
    idx = 0
    while True:
        # Found the value
        if array[idx] == value:
            return idx

        # If jump through the value, run linear search from the last jump index to current index
        if array[idx] > value:
            for offset in range(1, step):
                if array[idx - offset] == value:
                    return idx - offset
            return -1

        # Not found through the whole list
        if idx >= n - 1:
            return -1

        # Increment by step
        idx = min(idx + step, n - 1)
