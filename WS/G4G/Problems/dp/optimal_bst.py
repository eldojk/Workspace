"""
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the
number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches
is as small as possible.

Assuming there are n elements the root can be decided as k where k in range(i, j).

cost(i,j) = min ( cost(i, r-1) + freq[r]*level + cost(r+1, j) ) for r in range(i, j)
since level is a variable which we don't know while creating matrix lets re-write this as

cost(i, j) = sum of freq[i .. j] + min( cost(i, r-1) + cost(r+1, j) ) for r in range(i, j + 1)

^ this way the sum of freq gets computed once for all elements at root,
at level 2, it sum[i.. r-1] and sum[r+1 to j] gets computed again. Hence its added 2 times here :)
isn't that clever?

http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/

keys[] = {10, 12}, freq[] = {34, 50}

    0   1
0   34  118
1       50

"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def get_cost(cost_matrix, r, i, j):
    if r == i:
        return cost_matrix[i + 1][j]
    elif r == j:
        return cost_matrix[i][j - 1]
    else:
        return cost_matrix[i][r - 1] + cost_matrix[r + 1][j]


def optimal_bst(keys, freq):
    cost_matrix = [[0 for i in keys] for j in keys]

    for i in range(len(keys)):
        cost_matrix[i][i] = freq[i]

    max_index = len(freq) - 1

    for l in range(1, len(keys)):
        for i in range(len(keys)):

            j = i + l

            if j <= max_index:
                # cost(i, j)      = sum freq[i .. j]   + min( cost(i, r-1) + cost(r+1, j) ) for r in range(i, j + 1)
                cost_matrix[i][j] = sum(freq[i:j + 1]) + min([get_cost(cost_matrix, r, i, j) for r in range(i, j + 1)])

    # print_matrix(cost_matrix)
    return cost_matrix[0][len(keys) - 1]


if __name__ == '__main__':
    print optimal_bst([10, 12], [34, 50])
