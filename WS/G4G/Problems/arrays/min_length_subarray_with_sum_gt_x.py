"""
amzn

http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
"""


def min_length_sub_array_sum(array, x):
    if array is None or len(array) == 0:
        return -1

    if len(array) == 1 and x >= array[0]:
        return -1

    start = end = 0
    curr_sum = 0
    n = len(array)
    min_len = n + 1

    while end < n:

        while curr_sum <= x and end < n:

            # handling -ve numbers
            if curr_sum <= 0 and x > 0:
                start = end
                curr_sum = 0

            curr_sum += array[end]
            end += 1

        while curr_sum > x and start < n:

            if end - start < min_len:
                min_len = end - start

            curr_sum -= array[start]
            start += 1

    return min_len if min_len != n + 1 else -1


if __name__ == '__main__':
    print min_length_sub_array_sum([1, 4, 45, 6, 0, 19], 51)
    print min_length_sub_array_sum([1, 10, 5, 2, 7], 9)
    print min_length_sub_array_sum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280)
    print min_length_sub_array_sum([1, 2, 4], 8)
    print min_length_sub_array_sum([- 8, 1, 4, 2, -6], 6)
