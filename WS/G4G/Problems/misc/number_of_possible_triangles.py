"""
amzn

http://www.geeksforgeeks.org/find-number-of-triangles-possible/
"""


def num_triangles(array):
    n = len(array)
    array.sort()
    count = 0

    for i in range(n - 2):

        k = i + 2

        for j in range(i + 1, n):

            while k < n and array[i] + array[j] > array[k]:
                k += 1

            count += k - j - 1

    return count


if __name__ == '__main__':
    print num_triangles([10, 21, 22, 100, 101, 200, 300])