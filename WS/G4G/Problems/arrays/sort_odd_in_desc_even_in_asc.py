"""
msft

http://www.geeksforgeeks.org/sort-even-numbers-ascending-order-sort-odd-numbers-descending-order/
"""
from DS.algos.sort.merge_sort import merge_sort


def partition_odd_and_even(array):
    i = 0
    j = 0

    while j < len(array):
        if array[j] % 2 != 0:
            array[i], array[j] = array[j], array[i]
            i += 1

        j += 1

    return array, i


def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        j -= 1
        i += 1


def custom_sort(array):
    n = len(array)
    i = 0
    l = n - 1

    array, k = partition_odd_and_even(array)
    j = k - 1

    merge_sort(array, i, j)
    merge_sort(array, k, l)
    reverse(array, i, j)

    return array


"""
another way

Make all odd numbers negative.
Sort all numbers.
Revert the changes made in step 1 to get original elements back.
"""


if __name__ == '__main__':
    print custom_sort([1, 3, 2, 7, 5, 4])
