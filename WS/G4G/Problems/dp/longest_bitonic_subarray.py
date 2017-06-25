"""
msft

http://www.geeksforgeeks.org/maximum-length-bitonic-subarray/
"""


def longest_increasing_subarray_ending_at_i(array):
    result = [1 for i in array]

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            result[i] = result[i - 1] + 1

    return result


def longest_decreasing_subarray_starting_at_i(array):
    result = [1 for i in array]
    n = len(array)
    i = n - 2

    while i >= 0:
        if array[i] > array[i + 1]:
            result[i] = result[i + 1] + 1

        i -= 1

    return result


def longest_bitonic_subarray_length(array):
    lis = longest_increasing_subarray_ending_at_i(array)
    lds = longest_decreasing_subarray_starting_at_i(array)

    res = 0
    for i in range(len(array)):
        res = max(res,
                  lis[i] + lds[i] - 1)

    return res


if __name__ == '__main__':
    print longest_bitonic_subarray_length([12, 4, 78, 90, 45, 23])