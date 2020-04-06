"""
Link: https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
"""
# pylint: disable=invalid-name
# pylint: disable=inconsistent-return-statements


def find_floor_ceiling(array, number):
    """
    :param array: given non-decreasing sorted integer array
    :param number: a given number
    :return: the floor and ceiling of the given number
    """
    min_value = array[0]
    max_value = array[-1]
    if number < min_value:
        return 'None', min_value
    if number > max_value:
        return max_value, 'None'
    if number in array:
        return number, number
    for idx, value in enumerate(array):
        if value > number:
            return array[idx - 1], array[idx]
