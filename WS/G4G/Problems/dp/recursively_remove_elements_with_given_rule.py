# coding=utf-8
"""
http://www.geeksforgeeks.org/find-minimum-possible-size-of-array-with-given-rules-for-removal/

Given an array of numbers and a constant k, minimize size of array with following rules for removing elements.

Exactly three elements can be removed at one go.
The removed three elements must be adjacent in array, i.e., arr[i], arr[i+1], arr[i+2]. And the second element must be k
greater than first and third element must be k greater than second, i.e., arr[i+1] – arr[i] = k and arr[i+2]-arr[i+1]
= k.
Example:

Input: arr[] = {2, 3, 4, 5, 6, 4}, k = 1
Output: 0
We can actually remove all elements.
First remove 4, 5, 6 => We get {2, 3, 4}
Now remove 2, 3, 4   => We get empty array {}

Input:  arr[] = {2, 3, 4, 7, 6, 4}, k = 1
Output: 3
We can only remove 2 3 4

For every element arr[i] there are two possibilities
1) Either the element is not removed.
2) OR element is removed (if it follows rules of removal). When an element is removed, there are again two possibilities.
…..a) It may be removed directly, i.e., initial arr[i+1] is arr[i]+k and arr[i+2] is arr[i] + 2*k.
…..b) There exist x and y such that arr[x] – arr[i] = k, arr[y] – arr[x] = k, and subarrays “arr[i+1…x-1]” & “arr[x+1…y-1]” can be completely removed.

Below is recursive algorithm based on above idea.

// Returns size of minimum possible size of arr[low..high]
// after removing elements according to given rules
findMinSize(arr[], low, high, k)

// If there are less than 3 elements in arr[low..high]
1) If high-low+1 < 3, return high-low+1

// Consider the case when 'arr[low]' is not considered as
// part of any triplet to be removed.  Initialize result
// using this case
2) result = 1 + findMinSize(arr, low+1, high)

// Case when 'arr[low]' is part of some triplet and removed
// Try all possible triplets that have arr[low]
3) For all i from low+1 to high
    For all j from i+1 to high
      Update result if all of the following conditions are met
      a) arr[i] - arr[low] = k
      b) arr[j] - arr[i]  = k
      c) findMinSize(arr, low+1, i-1, k) returns 0
      d) findMinSize(arr, i+1, j-1, k) also returns 0
      e) Result calculated for this triplet (low, i, j)
         is smaller than existing result.

4) Return result
"""


def recursive_find(array, dp, lo, hi, k):
    if dp[hi][lo] != -1:
        return dp[hi][lo]

    # if length of array is less than 3, can't remove
    if (hi - lo + 1) < 3:
        return hi - lo + 1

    result = 1 + recursive_find(array, dp, lo + 1, hi, k)

    for i in range(lo + 1, hi):
        for j in range(i + 1, hi + 1):

            if (
                array[i] - array[lo] == k and \
                array[j] - array[lo] == 2*k and \
                recursive_find(array, dp, lo + 1, i - 1, k) == 0 and \
                recursive_find(array, dp, i + 1, j - 1, k) == 0
            ):
                result = min(
                    result,
                    recursive_find(array, dp, j + 1, hi, k)
                )

    dp[lo][hi] = result

    return dp[lo][hi]


def recursive_removed_length(array, k):
    dp = [[-1 for i in range(len(array) + 1)] for j in range(len(array) + 1)]
    hi = len(array) - 1
    lo = 0

    return recursive_find(array, dp, lo, hi, k)


if __name__ == '__main__':
    print recursive_removed_length([2, 3, 4, 5, 6, 4], 1)
