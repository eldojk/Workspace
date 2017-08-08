"""
amzn

https://www.youtube.com/watch?v=yCQN096CwWM

columns in rectangle are arrays. starting at first column, the max contiguous sum,
would've been the max rectangular sum if we had only that column. Adding the second
column means we add the values in columns 1 and 2 and find their max contiguous sum ->
also ignoring first column, start and the second one and find the same, -> max will
be max of these ... this is the approach. from columns one to n, add and find max
contiguous sums, start at column 2 and do same, keep track of left and right and
up and down while doing this... Basically this is brute force, theonly way to optimise
is to optimise the max contiguous sum finding step, make it o(n)
"""
from sys import maxint


def sum_arrays(array1, array2):
    arr = []
    for i in range(len(array1)):
        arr.append(array1[i] + array2[i])

    return arr


def get_max_contiguous_sum(array):
    sum_array = [i for i in array]
    start_array = [0 for i in array]

    max_sum = -maxint
    start = 0
    end = 0
    for i in range(1, len(array)):
        if array[i] <= sum_array[i - 1] + array[i]:
            sum_array[i] = sum_array[i - 1] + array[i]
            start_array[i] = start
        else:
            sum_array[i] = array[i]
            start_array[i] = i

        if max_sum < sum_array[i]:
            max_sum = sum_array[i]
            start = start_array[i]
            end = i

    return max_sum, start, end


def get_max_sum_sub_rectangle(rectangle):
    max_sum = -maxint
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0

    for up in range(len(rectangle)):

        sum_arr = [0 for i in range(len(rectangle[0]))]

        for down in range(up, len(rectangle)):

            sum_arr = sum_arrays(sum_arr, rectangle[down])

            sum_found, left_found, right_found = get_max_contiguous_sum(sum_arr)

            if sum_found > max_sum:
                max_sum = sum_found
                max_left = left_found
                max_right = right_found
                max_up = up
                max_down = down

    return max_sum, max_left, max_right, max_up, max_down


if __name__ == '__main__':
    r = [
        [2, 1, -3, -4, 5],
        [0, 6, 3, 4, 1],
        [2, -2, -1, 4, -5],
        [-3, 3, 1, 0, 3]
    ]

    print get_max_sum_sub_rectangle(r)