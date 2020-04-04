"""
Link: https://www.geeksforgeeks.org/median-of-two-sorted-arrays
"""
# pylint: disable=invalid-name


def median_of_two_sorted_array(array1, array2):
    """
    :param array1: given array 1
    :param array2: given array 2
    :return: The median and merged array
    Method: Use merge sort
    Complexity: O(n)
    """
    if len(array1) != len(array2):
        return "Invalid input"
    i = 0
    j = 0
    n = len(array1)
    for _ in range(n + 1):
        if i == n:
            return (array1[-1] + array2[0]) / 2
        if j == n:
            return (array1[0] + array2[-1]) / 2
        if array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    return (array1[i - 1] + array2[j - 1]) / 2
