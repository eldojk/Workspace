"""
amzn, msft

http://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

in an x, y grid, starting at 0,0 how many ways can u reach x,y if you can only move down and right

CITC 9.2 #317



		0	1	2	3
	0	0	0	0	0
0	0	1	1	1	1
1	0	1	2	3	4
2	0	1	3	6	10
3	0	1	4	10	20
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def get_number_of_ways(x, y):
    if x == 0 or y == 0:
        return 1

    matrix = [[0 for i in range(y + 2)] for j in range(x + 2)]

    for i in range(1, y + 2):
        matrix[1][i] = 1

    for j in range(1, x + 2):
        matrix[j][1] = 1

    for i in range(2, x + 2):
        for j in range(2, y + 2):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    print_matrix(matrix)
    return matrix[x + 1][y + 1]


if __name__ == '__main__':
    print get_number_of_ways(3, 3)
