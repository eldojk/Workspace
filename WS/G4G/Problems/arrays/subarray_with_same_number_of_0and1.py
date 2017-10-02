"""
amzn

http://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/

consider 0s as -1 so when we find a sum of zero for all elements we know
there is equal number of zeros and ones
"""


def max_size_sub_array_with_eq_0_and_1(array):
    hm = {}
    curr_sum = 0
    max_size = 0
    max_i = max_j = 0

    for i in range(len(array)):
        el = array[i]

        if el == 1:
            curr_sum += 1
        else:
            curr_sum -= 1

        if curr_sum in hm:
            first_idx = hm[curr_sum]
            size = i - first_idx

            if size > max_size:
                max_size = size
                max_i = first_idx + 1
                max_j = i

        else:
            hm[curr_sum] = i

    return (max_i, max_j) if max_size > 0 else 'No such sub array'


if __name__ == '__main__':
    print ''
    print max_size_sub_array_with_eq_0_and_1([1, 0, 1, 1, 1, 0, 0])
    print max_size_sub_array_with_eq_0_and_1([1, 1, 1, 1])
    print max_size_sub_array_with_eq_0_and_1([0, 0, 1, 1, 0])
