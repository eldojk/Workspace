"""
msft

http://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/

If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60],
your program should be able to find that the subarray lies between the indexes 3 and 8
"""


def get_element_out_of_place_right(array):
    """
    Find index of the right most element which is
    less than a previously seen element

    :param array:
    :return:
    """
    i = 1
    n = len(array)
    max_seen_so_far = array[0]
    right_index = 0

    while i < n:
        if array[i] < max_seen_so_far:
            right_index = i

        else:
            max_seen_so_far = array[i]

        i += 1

    return right_index


def get_element_out_of_place_left(array):
    """
    Find index of left most element which is greater
    than an element on the right

    :param array:
    :return:
    """
    n = len(array)
    i = n - 2
    min_seen_so_far = array[n - 1]
    left_index = i

    while i >= 0:
        if array[i] > min_seen_so_far:
            left_index = i

        else:
            min_seen_so_far = array[i]

        i -= 1

    return left_index


def min_sub_array(array):
    i = get_element_out_of_place_left(array)
    j = get_element_out_of_place_right(array)

    print i, j


if __name__ == '__main__':
    min_sub_array([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])
    min_sub_array([0, 1, 15, 25, 6, 7, 30, 40, 50])
