# coding=utf-8
"""
http://www.geeksforgeeks.org/find-shortest-distance-guard-bank/

Given a matrix that is filled with ‘O’, ‘G’, and ‘W’ where ‘O’ represents open space, ‘G’ represents guards and ‘W’
represents walls in a Bank. Replace all of the O’s in the matrix with their shortest distance from a guard, without
being able to go through any walls. Also, replace the guards with 0 and walls with -1 in output matrix.

Expected Time complexity is O(MN) for a M x N matrix.

Examples:

O ==> Open Space
G ==> Guard
W ==> Wall

Input:
  O  O  O  O  G
  O  W  W  O  O
  O  O  O  W  O
  G  W  W  W  O
  O  O  O  O  G

Output:
  3  3  2  1  0
  2 -1 -1  2  1
  1  2  3 -1  2
  0 -1 -1 -1  1
  1  2  2  1  0

The idea is to do BFS. We first enqueue all cells containing the guards and loop till queue is not empty. For each
iteration of the loop, we dequeue the front cell from the queue and for each of its four adjacent cells, if cell is an
open area and its distance from guard is not calculated yet, we update its distance and enqueue it.
Finally after BFS procedure is over, we print the distance matrix.
"""
from Queue import Queue

from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_valid(i, j, m, n):
    return 0 <= i < m and 0 <= j < n


def get_neighbours(i, j, m, n, matrix):
    nei = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
    valid_neighbours = [neighbour for neighbour in nei if is_valid(neighbour[0], neighbour[1], m, n)]
    walls_filtered = [nei for nei in valid_neighbours if matrix[nei[0]][nei[1]] == 'O']

    return walls_filtered


def get_shortest_dists(matrix, m, n):
    q = Queue()

    output_matrix = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'G':
                q.put((i, j, 0))
                output_matrix[i][j] = 0

    while not q.empty():
        el = q.get()
        dist = el[2]
        i = el[0]
        j = el[1]

        for neighbour in get_neighbours(i, j, m, n, matrix):
            x = neighbour[0]
            y = neighbour[1]

            if output_matrix[x][y] != -1:
                continue

            q.put((x, y, dist + 1))
            output_matrix[x][y] = dist + 1

    return output_matrix


if __name__ == '__main__':
    k = [['O', 'O', 'O', 'O', 'G'],
         ['O', 'W', 'W', 'O', 'O'],
         ['O', 'O', 'O', 'W', 'O'],
         ['G', 'W', 'W', 'W', 'O'],
         ['O', 'O', 'O', 'O', 'G']]
    output = get_shortest_dists(k, 5, 5)

    print_matrix(output)
