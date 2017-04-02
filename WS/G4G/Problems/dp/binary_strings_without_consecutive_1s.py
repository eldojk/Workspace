# coding=utf-8
"""
http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/

This problem can be solved using Dynamic Programming. Let a[i] be the number of binary strings of length i which do not
contain any two consecutive 1’s and which end in 0. Similarly, let b[i] be the number of such strings which end in 1.
We can append either 0 or 1 to a string ending in 0, but we can only append 0 to a string ending in 1. This yields the
recurrence relation:

a[i] = a[i - 1] + b[i - 1]
b[i] = a[i - 1]
The base cases of above recurrence are a[1] = b[1] = 1. The total number of strings of length i is just a[i] + b[i].

Following is the implementation of above solution. In the following implementation, indexes start from 0. So a[i]
represents the number of binary strings for input length i+1. Similarly, b[i] represents binary strings for input
length i+1.
"""


def num_strings(num):
    ending_in_0 = [0 for i in range(num + 1)]
    ending_in_1 = [0 for i in range(num + 1)]

    ending_in_0[1] = 1
    ending_in_1[1] = 1

    for i in range(2, num + 1):
        ending_in_0[i] = ending_in_0[i - 1] + ending_in_1[i - 1]  # append 0 to all strings ending in 0 and 1
        ending_in_1[i] = ending_in_0[i - 1]  # append 1 to all strings ending in 0

    return ending_in_0[num] + ending_in_1[num]


if __name__ == '__main__':
    print num_strings(3)
