"""
amzn

http://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

Given an array of integers where each element represents the max number of steps that can be made forward from that
element. Write a function to return the minimum number of jumps to reach the end of the array
(starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9

The idea is to find min_steps[n - 1]. Lets say some elements at indexes a, b and c have values that makes it possible to
reach n - 1 in one hop. So they are potential predecessors to the last hop. Our goal is to choose a predecessor that '
minimises the number of hops required to reach n - 1. which is min (min_steps[a], min_steps[b], min_steps[c]) + 1
"""
from sys import maxint


def min_steps_to_n(array):
    N = len(array)
    min_steps = [maxint for el in array]
    min_steps[0] = 0

    for i in range(1, N):

        for j in range(i):
            max_index_reachable_from_j = array[j] + j

            if max_index_reachable_from_j >= i:
                # array[i] is reachable from j
                min_steps[i] = min(
                    min_steps[i],
                    min_steps[j] + 1
                )

    return min_steps[N - 1]


if __name__ == '__main__':
    print min_steps_to_n([1, 3, 6, 1, 0, 9])

