"""
amzn

http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
"""


def min_length_sub_array_with_greater_sum(array, sm):
    n = len(array)
    i = j = 0
    mi = 0
    mj = n
    curr_sum = 0

    while j < n:

        # this if condition handles negatives
        if curr_sum <= 0 and sm > 0:
            curr_sum = 0
            i = j

        curr_sum += array[j]

        while curr_sum > sm:
            if j - i < mj - mi:
                mi = i
                mj = j

            i += 1
            curr_sum -= array[i - 1]

        j += 1

    return (mi, mj) if mj - mi != n else -1


if __name__ == '__main__':
    print min_length_sub_array_with_greater_sum([1, 4, 45, 6, 0, 19], 51)
    print min_length_sub_array_with_greater_sum([1, 10, 5, 2, 7], 9)
    print min_length_sub_array_with_greater_sum([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280)
    print min_length_sub_array_with_greater_sum([1, 2, 4], 8)
    print min_length_sub_array_with_greater_sum([- 8, 1, 4, 2, -6], 6)
