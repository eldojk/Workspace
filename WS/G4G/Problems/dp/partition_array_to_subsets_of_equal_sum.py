"""
amzn

http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/

Let isSubsetSum(arr, n, sum/2) be the function that returns true if
there is a subset of arr[0..n-1] with sum equal to sum/2

The isSubsetSum problem can be divided into two sub problems
 a) isSubsetSum() without considering last element
    (reducing n to n-1)
 b) isSubsetSum considering the last element
    (reducing sum/2 by arr[n-1] and n to n-1)
If any of the above the above sub problems return true, then return true.
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                              isSubsetSum (arr, n-1, sum/2 - arr[n-1])

is_sum(0, 4, 5) = is_sum(0, 4-1, 5) or # not including 5
				  is_sum(0, 4-1, 5-array[4-1])

   0    3    1    1    2    2    1
0 True True True True True True True
1 False False True True True True True
2 False False False True True True True
3 False True True True True True True
4 False False True True True True True
5 False False False True True True True
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_subset_sum_possible(array, sm):
    dp = [[False for i in range(len(array) + 1)] for j in range(sm + 1)]

    for i in range(len(array) + 1):
        dp[0][i] = True

    for i in range(1, sm + 1):
        for j in range(1, len(array) + 1):

            if array[j - 1] > i:
                dp[i][j] = dp[i][j - 1]  # without including nth element
            else:
                dp[i][j] = dp[i][j - 1] or dp[i - array[j - 1]][j - 1]  # include and not include

    print_matrix(dp)
    return dp[sm][len(array)]


if __name__ == '__main__':
    print is_subset_sum_possible([3, 1, 1, 2, 2, 1], 5)
