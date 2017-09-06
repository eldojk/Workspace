"""
amzn, google

http://www.geeksforgeeks.org/minimum-number-of-swaps-required-for-arranging-pairs-adjacent-to-each-other/

n = 3
pairs[] = {1->3, 2->6, 4->5}  // 1 is partner of 3 and so on
arr[] = {3, 5, 6, 4, 1, 2}

Output: 2
We can get {3, 1, 5, 4, 6, 2} by swapping 5 & 6, and 6 & 1
"""


def swap(array, i1, i2):
    tmp = array[i1]
    array[i1] = array[i2]
    array[i2] = tmp


def update_index(index, a, ai, b, bi):
    index[a] = ai
    index[b] = bi


def min_swaps(array, pairs, index, i, n):

    if i > n:
        return 0

    if pairs[array[i]] == array[i + 1]:
        return min_swaps(array, pairs, index, i + 2, n)

    # swap second with pair of first
    first = array[i]
    second = array[i + 1]
    first_idx = index[first]
    second_idx = index[second]
    pair_first = pairs[first]
    pair_first_idx = index[pair_first]

    swap(array, second_idx, pair_first_idx)

    update_index(index, second, pair_first_idx, pair_first, second_idx)

    first_result = min_swaps(array, pairs, index, i + 2, n)

    swap(array, second_idx, pair_first_idx)

    update_index(index, second, second_idx, pair_first, pair_first_idx)

    # swap first with pair of second
    first = array[i]
    second = array[i + 1]
    first_idx = index[first]
    second_idx = index[second]
    pair_second = pairs[second]
    pair_second_idx = index[pair_second]

    swap(array, first_idx, pair_second_idx)

    update_index(index, first, pair_second_idx, pair_second, first_idx)

    second_result = min_swaps(array, pairs, index, i + 2, n)

    swap(array, first_idx, pair_second_idx)

    update_index(index, first, first_idx, pair_second, pair_second_idx)

    # return min of two cases
    return 1 + min(first_result, second_result)


def populate_indices(array, index):
    for i in range(len(array)):
        index[array[i]] = i


if __name__ == '__main__':
    # appending 0 in beginning and starting from index 1 to satisfy assumptions
    arr = [0, 3, 5, 6, 4, 1, 2]
    _pairs = [0, 3, 6, 1, 5, 4, 2]
    idx = [0 for i in arr]
    populate_indices(arr, idx)

    print min_swaps(arr, _pairs, idx, 1, len(arr) - 1)
