# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/

The idea is to use modified one pass of bubble sort. Maintain a flag for representing
which order(i.e. < or >) currently we need. If the current two elements are not
in that order then swap those elements otherwise not.
Let us see the main logic using three consecutive elements A, B, C. Suppose we are
processing B and C currently and the current relation is ‘<'. But we have B > C.
Since current relation is ‘<' previous relation must be '>‘ i.e., A must be greater than B.
So, the relation is A > B and B > C. We can deduce A > C. So if we swap B and C then the
relation is A > C and C < B. Finally we get the desired order A C B
"""


def zig_zag(array):

    # true means <
    flag = True
    n = len(array)

    for i in range(n - 1):

        if flag:

            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        else:

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        flag = not flag

    return array


if __name__ == '__main__':
    print zig_zag([4, 3, 7, 8, 6, 2, 1])
