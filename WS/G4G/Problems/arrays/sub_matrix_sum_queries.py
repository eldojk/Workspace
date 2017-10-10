"""
amzn

http://www.geeksforgeeks.org/submatrix-sum-queries/
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


class MatrixQueries(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.aux = None
        self.get_sum_matrix()

    def get_sum_matrix(self):
        m = len(self.matrix)
        n = len(self.matrix[0])

        self.aux = [[0 for i in self.matrix[0]] for j in self.matrix]

        for i in range(m):

            r_sum = 0
            for j in range(n):

                r_sum += self.matrix[i][j]
                self.aux[i][j] = r_sum

                if i > 0:
                    self.aux[i][j] += self.aux[i - 1][j]

        # print_matrix(self.aux)

    def get_sum(self, x1, y1, x2, y2):
        oox2y2 = self.aux[x2][y2]

        oox1y2 = 0
        oox1y1 = 0
        oox2y1 = 0

        if x1 > 0:
            oox1y2 = self.aux[x1 - 1][y2]

        if y1 > 0:
            oox2y1 = self.aux[x2][y1 - 1]

        if x1 > 0 and y1 > 0:
            oox1y1 = self.aux[x1 - 1][y1 - 1]

        result = oox2y2 - oox1y2 - oox2y1 + oox1y1
        return result


if __name__ == '__main__':
    m = [
        [1, 2, 3, 4, 6],
        [5, 3, 8, 1, 2],
        [4, 6, 7, 5, 5],
        [2, 4, 8, 9, 4]
    ]

    q = MatrixQueries(m)
    print q.get_sum(2, 2, 3, 4)
    print q.get_sum(0, 0, 1, 1)
    print q.get_sum(1, 2, 3, 3)
