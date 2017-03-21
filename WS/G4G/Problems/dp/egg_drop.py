"""
http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
https://www.youtube.com/watch?v=amdKmQlATmQ

		0	1	2	3	4
	1	0	1	2	3	4
	2	0	1	2	2	3

	2 and 2
	        egg breaks       not break
			e - 1, n - 1, | e, n - k
	1 -  1 + [ [1, 1 - 1], [2, 2 - 1] ] = [0 , 1] = 2
	2 -  1 + [ [1, 2 - 1], [2, 2 - 2] ] = [1, 0] = 2
	min(2, 2)


	For each egg > 1:
		for each floor from 2...k
			minimise over:
				drop from floors 1.. k
"""
from sys import maxint
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def egg_drops_min_trials(floors, eggs):
    dp = [range(floors + 1) for e in range(eggs + 1)]

    for i in range(floors + 1):
        dp[0][i] = 0

    # start from 2nd egg
    for i in range(2, eggs + 1):

        # from 2nd floor
        for j in range(2, floors + 1):
            dp[i][j] = maxint

            # start dropping from 1 to j'th floor as x
            for x in range(1, j + 1):
                result = 1 + max(
                    dp[i - 1][x - 1],  # egg breaks
                    dp[i][j - x]  # doesn't break
                )

                if result < dp[i][j]:
                    dp[i][j] = result

    return dp[eggs][floors]


if __name__ == '__main__':
    print egg_drops_min_trials(4, 2)
