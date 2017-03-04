"""
http://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/

consider 0s as -1 so when we find a sum of zero for all elements we know there is equal number of zeros and ones
"""


def compute_left_sum_array(array):
    sum_arr = [0 for i in array]
    curr_sum = 0

    for i in range(len(array)):
        el = array[i]
        if el == 0:
            curr_sum -= 1
        else:
            curr_sum += 1

        sum_arr[i] = curr_sum

    return sum_arr


def store_first_occuring_sums_in_hash(sum_arr):
    _dict = {}
    for i in range(len(sum_arr)):
        el = sum_arr[i]
        if _dict.get(el) is None:
            _dict[el] = i

    return _dict


def find_max_subarray_of_equal_0_and_1(array):
    # compute sum from left
    left_sum_arr = compute_left_sum_array(array)

    # first occurence of each sum is stored in hash
    occur = store_first_occuring_sums_in_hash(left_sum_arr)

    # compute max size of array with sum 0 from index 0
    m = 0
    max_size = 0
    n = 0
    for i in range(len(left_sum_arr)):
        if left_sum_arr[i] == 0:
            max_size = i
            n = i

    # for index starting after zero
    # if we find a sum k in array at index j, and assume we found this same k in index i, where i < j
    # that means adding elements from i + 1 to j hasn't changed the sum, this means the subarray[i+1, j]
    # could be a potential candidate for what we are searching for
    for i in range(len(left_sum_arr)):
        val = left_sum_arr[i]
        first_idx_of_val = occur[val]

        sub_array_size = i - first_idx_of_val

        if sub_array_size > max_size:
            max_size = sub_array_size
            m = first_idx_of_val + 1
            n = i

    return (m, n) if max_size > 0 else 'No such subarray'


if __name__ == '__main__':
    print find_max_subarray_of_equal_0_and_1([1, 0, 1, 1, 1, 0, 0])
    print find_max_subarray_of_equal_0_and_1([1, 1, 1, 1])
    print find_max_subarray_of_equal_0_and_1([0, 0, 1, 1, 0])
