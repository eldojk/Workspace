"""
http://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
"""


def is_zero_sum_subarray_found(array):
    hm = {}

    sm = 0

    for el in array:
        sm += el

        if hm.get(el) is not None or el == 0 or sm == 0:
            return True

        hm[sm] = True

    return False


if __name__ == '__main__':
    print ''
    print is_zero_sum_subarray_found([4, 2, -3, 1, 6])