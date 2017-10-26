"""
amzn

http://www.geeksforgeeks.org/count-minimum-steps-get-given-desired-array/

Consider an array with n elements and value of all the elements is zero. We can perform
following operations on the array.

Incremental operations:Choose 1 element from the array and increment its value by 1.
Doubling operation: Double the values of all the elements of array.


Take the target array first.

Initialize result as 0.

If all are even, divide all elements by 2
and increment result by 1.

Find all odd elements, make them even by
reducing them by 1. and for every reduction,
increment result by 1.

Finally we get all zeros in target array.
"""


def min_steps_to_desired(array):
    result = 0
    n = len(array)

    while True:
        # checking if array is full of zeroes
        is_non_zero_found = False
        for i in range(n):
            if array[i] != 0:
                is_non_zero_found = True
                break

        if not is_non_zero_found:
            break

        # make any odds even
        for i in range(n):
            if array[i] % 2 != 0:
                array[i] -= 1
                result += 1

        # divide if non zero even are present
        div_reqd = False
        for i in range(n):
            if array[i] > 0:
                array[i] /= 2
                div_reqd = True

        if div_reqd:
            result += 1

    return result


if __name__ == '__main__':
    print min_steps_to_desired([16, 16, 16])
    print min_steps_to_desired([2, 1])
    print min_steps_to_desired([2, 3])
