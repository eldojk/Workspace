"""
amzn

http://www.geeksforgeeks.org/maximum-path-sum-triangle/
^ refer for explanation
"""


def max_sum_val(triangle):
    m = len(triangle) - 1
    n = len(triangle[0]) - 1

    i = m - 1

    while i >= 0:

        for j in range(i + 1):

            triangle[i][j] += max(
                triangle[i + 1][j],
                triangle[i + 1][j + 1]
            )

        i -= 1

    return triangle[0][0]


if __name__ == '__main__':
    print max_sum_val(
        [
            [1, 0, 0],
            [4, 8, 0],
            [1, 5, 3]
        ]
    )
