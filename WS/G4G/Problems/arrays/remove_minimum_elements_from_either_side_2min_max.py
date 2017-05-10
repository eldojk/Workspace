"""
amzn

http://www.geeksforgeeks.org/remove-minimum-elements-either-side-2min-max/
Number of removals should be minimum.

arr[] = {4, 5, 100, 9, 10, 11, 12, 15, 200}
Output: 4
We need to remove 4 elements (4, 5, 100, 200)
so that 2*min becomes more than max.


arr[] = {4, 7, 5, 6}
Output: 0
We don't need to remove any element as
4*2 > 7 (Note that min = 4, max = 8)

arr[] = {20, 7, 5, 6}
Output: 1
We need to remove 20 so that 2*min becomes
more than max

arr[] = {20, 4, 1, 3}
Output: 3
We need to remove any three elements from ends
like 20, 4, 1 or 4, 1, 3 or 20, 3, 1 or 20, 4, 1

INSTEAD OF DP -> this can be used
The idea is to find the maximum sized subarray such that 2*min > max. We run two nested loops, the outer loop chooses a
starting point and the inner loop chooses ending point for the current starting point. We keep track of longest
subarray with the given property.
"""
from sys import maxint


def remove_min(array):
    start = 0
    end = 0

    for i in range(len(array)):
        _min = maxint
        _max = -maxint
        for j in range(i, len(array)):
            val = array[j]

            if val < _min:
                _min = val
            if val > _max:
                _max = val

            if 2 * _min > _max and (end - start < j - i):
                start = i
                end = j

    return len(array) - (end - start + 1)


if __name__ == '__main__':
    print remove_min([4, 5, 100, 9, 10, 11, 12, 15, 200])
