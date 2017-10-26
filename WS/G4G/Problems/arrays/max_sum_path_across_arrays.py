"""
amzn

http://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/

Given two sorted arrays such the arrays may have some common elements.
Find the sum of the maximum sum path to reach from beginning of any array to end of
any of the two arrays. We can switch from one array to another array only at
common elements.

Expected time complexity is O(m+n) where m is the number of elements in ar1[] and
n is the number of elements in ar2[].

Input:  ar1[] = {2, 3, 7, 10, 12, 15, 30, 34}
        ar2[] = {1, 5, 7, 8, 10, 15, 16, 19}
Output: 122
122 is sum of 1, 5, 7, 8, 10, 12, 15, 30, 34
"""


def max_path_sum(array1, array2):
    i = 0
    j = 0

    m = len(array1)
    n = len(array2)

    result = 0
    sum1 = 0
    sum2 = 0

    while i < m and j < n:

        # Add elements of array1[] to sum1
        if array1[i] < array2[j]:
            sum1 += array1[i]
            i += 1

        # Add elements of array2[] to sum1
        elif array1[i] > array2[j]:
            sum2 += array2[j]
            j += 1

        else:
            # we reached a common point
            sum1 += array1[i]
            sum2 += array2[j]

            result += max(sum1, sum2)

            i += 1
            j += 1
            sum1 = 0
            sum2 = 0

    # Add remaining elements of array1[]
    while i < m:
        sum1 += array1[i]
        i += 1
    # Add remaining elements of array2[]
    while j < n:
        sum2 += array2[j]
        j += 1

    result += max(sum1, sum2)
    return result


if __name__ == '__main__':
    print max_path_sum([2, 3, 7, 10, 12, 15, 30, 34], [1, 5, 7, 8, 10, 15, 16, 19])
