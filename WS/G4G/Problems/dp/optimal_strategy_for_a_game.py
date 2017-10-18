"""
amzn

#tricky
http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/

https://people.cs.clemson.edu/~bcdean/dp_practice/dp_10.swf

F(i, j)  represents the maximum value the user can collect from
         i'th coin to j'th coin.

if I choose ith coin, from remaining i + 1 to j the opponent with either choose i + 1 th or j th coin
if she chooses i + 1 th coin, i get ro choose from i + 2, j coin, else she chooses j, I get to choose
from i + 1, j - 1. Assuming opponent is as smart as we are, she is going to choose a coin such that
the value we get after her choice is made is the minimum. So the best we can hope for is to guarantee
that we get min of i + 2 to j and i + 1 to j - 1

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ),
                   Vj + min(F(i+1, j-1), F(i, j-2) ))
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1

    5   3   7   10
5   5   5   10  15
3       3   7   13
7           7   10
10              10
"""


def maximum_value_we_can_guarantee(array):
    dp = [[0 for i in array] for j in array]
    N = len(array)

    for i in range(N):
        dp[i][i] = array[i]

        j = i + 1
        if j < N:
            dp[i][j] = max(array[i], array[j])

    for l in range(2, N):
        for i in range(N):

            j = i + l

            if j < N:
                """
                jotting down some stuff:
                we don't run out of bounds, since max and min go as high as i + 2 and j - 2. Here j starts at i + 2
                and the above condition checks validity of j. and the j - 2 part is only as low as i as j starts at
                i + 2
                """
                dp[i][j] = max(
                    array[i] + min(
                        dp[i + 2][j], dp[i + 1][j - 1],  # picked ith coin
                    ),
                    array[j] + min(
                        dp[i + 1][j - 1], dp[i][j - 2]  # picked jth coin
                    )
                )

    return dp[0][N - 1]


if __name__ == '__main__':
    print maximum_value_we_can_guarantee([5, 3, 7, 10])
    print maximum_value_we_can_guarantee([8, 15, 3, 7])
