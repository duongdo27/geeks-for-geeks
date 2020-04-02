"""
Link: https://www.geeksforgeeks.org/linear-search/
"""


def linear_search(array, value):
    """
    :param array: list of values
    :param value: value to search for
    :return: index of the value
    If not found, return -1
    """
    for idx, ele in enumerate(array):
        if ele == value:
            return idx
    return -1
