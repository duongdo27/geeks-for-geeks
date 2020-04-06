"""
Link: https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
"""
# pylint: disable=invalid-name


def sum_closest_to_zero(array):
    """
    :param array: given integer array
    :return: Two elements such that their sum is closest to zero.
    Method: 1
    Complexity: O(n)
    """
    if len(array) == 0:
        return 0
    array = sorted(array)
    min_left = left = 0
    min_right = right = len(array) - 1
    min_sum = max(array) * 2 + 1
    while left < right:
        total = array[left] + array[right]
        if total == 0:
            return array[left], array[right]
        if abs(total) < abs(min_sum):
            print(min_sum, array[left], array[right])
            min_sum = total
            min_left = left
            min_right = right
            print(min_sum)
        elif total > 0:
            right -= 1
        else:
            left += 1
    return array[min_left], array[min_right]
