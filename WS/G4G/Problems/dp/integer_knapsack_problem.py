"""
https://www.youtube.com/watch?v=8LusJS5-AGo&index=1&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

For each weight, value is the MAX of either:
adding wt : -> value[i] + value_arr[current_wt - weight[i]]
or not adding wt -> value_arr[i]

V	W	0	1	2	3	4	5	6	7
0   0   0   0   0   0   0   0   0   0
1	1	0	1	1	1	1	1	1	1
4	3	0	1	1	4	5	5	5	5
5	4	0	1	1	4	5	6	6	9
7	5	0	1	1	4	5	7	8	9

val[i, w] = max( val[i - 1, w], val[i] + val[i-1, w-w(i)] )

max value of i items and w weight allowed =
Max(choosing the item and not choosing the ith item)
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def best_knapsack_value(values, weights, max_wt):
    values = [0] + values
    weights = [0] + weights
    value_matrix = [[0 for j in range(max_wt + 1)] for i in values]

    for i in range(1, len(values)):
        for j in range(1, max_wt + 1):

            if weights[i] <= j:

                value_matrix[i][j] = max(
                    value_matrix[i - 1][j],
                    values[i] + value_matrix[i - 1][j - weights[i]]
                )

            else:

                value_matrix[i][j] = value_matrix[i - 1][j]

    return value_matrix[len(values) - 1][max_wt]


if __name__ == '__main__':
    print best_knapsack_value([1, 4, 5, 7], [1, 3, 4, 5], 7)