"""
amzn

http://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
http://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/
"""


def store_first_occurring_sums_in_hash(left_sum_array):
    hm = {}

    for i in range(len(left_sum_array)):
        if left_sum_array[i] in hm:
            continue

        hm[left_sum_array[i]] = i

    return hm


def compute_left_sum_array(array):
    left_sum_array = [0 for i in array]

    sum_so_far = 0
    for i in range(len(array)):
        sum_so_far += array[i]
        left_sum_array[i] = sum_so_far

    return left_sum_array


def sub_array_with_some_0(array):
    left_sum_array = compute_left_sum_array(array)
    occur = store_first_occurring_sums_in_hash(left_sum_array)

    m = 0
    n = 0
    max_size = 0
    for i in range(len(left_sum_array)):
        sum_being_considered = left_sum_array[i]
        first_occurence = occur[sum_being_considered]

        diff = i - first_occurence

        if diff > max_size:
            max_size = diff
            m = first_occurence + 1
            n = i

    return (m, n) if max_size > 0 else 'No such sub array'


if __name__ == '__main__':
    print sub_array_with_some_0([4, 2, -3, 1, 6])
    print sub_array_with_some_0([4, 2, 0, 1, 6])
    print sub_array_with_some_0([-3, 2, 3, 1, 6])
    print sub_array_with_some_0([15, -2, 2, -8, 1, 7, 10, 23])
