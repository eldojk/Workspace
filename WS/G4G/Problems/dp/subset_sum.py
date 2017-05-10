"""
amzn

http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to
given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) ||        - don't include nth element
                           isSubsetSum(set, n-1, sum-set[n-1])  - include nth element

  0 1 2 3 4 5 6
0 t t t t t t t
1 f f f f f f f
2 f f f f f f t
3 f t t t t t t
4 f f f t t t t
5 f f f f f t t
6 f f f f f f t
7 f f f t t t t
8 f f f f f t t
9 f f f f f t t

"""


def print_matrix_boolean(m):
    r_size = len(m[0])
    for i in range(len(m)):
        for j in range(r_size):
            if m[i][j] == True:
                print 't',
            else:
                print 'f',
        print''


def is_exists_valid_sum(elements, sm):
    dp = [[False for i in range(len(elements) + 1)] for j in range(sm + 1)]

    for i in range(len(elements) + 1):
        dp[0][i] = True

    for i in range(sm + 1):
        for j in range(1, len(elements) + 1):

            if elements[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] or dp[i - elements[j - 1]][j - 1]

    # print_matrix_boolean(dp)
    return dp[sm][len(elements)]


if __name__ == '__main__':
    print is_exists_valid_sum([3, 34, 4, 12, 5, 2], 9)
