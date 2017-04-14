# coding=utf-8
"""
http://www.geeksforgeeks.org/longest-zig-zag-subsequence/

The longest Zig-Zag subsequence problem is to find length of the longest subsequence of given sequence such that all
elements of this are alternating.
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy one of the following relation :

  x1 < x2 > x3 < x4 > x5 < …. xn or
  x1 > x2 < x3 > x4 < x5 > …. xn


Let A is given array of length n of integers. We define a 2D array Z[n][2] such that Z[i][0] contains longest Zig-Zag
subsequence ending at index i and last element is greater than its previous element and Z[i][1] contains longest Zig-Zag
subsequence ending at index i and last element is smaller than its previous element, then we have following recurrence
relation between them,

Z[i][0] = Length of the longest Zig-Zag subsequence
          ending at index i and last element is greater
          than its previous element
Z[i][1] = Length of the longest Zig-Zag subsequence
          ending at index i and last element is smaller
          than its previous element

Recursive Formulation:
   Z[i][0] = max (Z[i][0], Z[j][1] + 1);
             for all j < i and A[j] < A[i]
   Z[i][1] = max (Z[i][1], Z[j][0] + 1);
             for all j < i and A[j] > A[i]
"""


def longest_sequence_length(array):
    dp = [[1 for i in array] for j in range(2)]

    max_len = 1
    for i in range(1, len(array)):
        for j in range(i):

            if array[j] < array[i]:

                dp[0][i] = max(
                    dp[0][i],
                    dp[1][j] + 1
                )

                max_len = max(max_len, dp[0][i])

            elif array[j] > array[i]:

                dp[1][i] = max(
                    dp[1][i],
                    dp[0][j] + 1
                )

                max_len = max(max_len, dp[1][i])

    return max_len


if __name__ == '__main__':
    print longest_sequence_length([10, 22, 9, 33, 49, 50, 31, 60])
    print longest_sequence_length([1, 5, 4])
