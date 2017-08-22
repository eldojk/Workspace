"""
msft, amzn

http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
"""


def largest_diff(array):
    l_min = [i for i in array]
    r_max = [j for j in array]
    n = len(array)

    for i in range(1, n):
        l_min[i] = min(array[i], l_min[i - 1])

    j = n - 2
    while j >= 0:
        r_max[j] = max(array[j], r_max[j + 1])
        j -= 1

    i = j = 0
    max_diff = -1

    while i < n and j < n:

        if l_min[i] < r_max[j]:

            max_diff = max(max_diff, j - i)
            j += 1

        else:
            i += 1

    return max_diff


if __name__ == '__main__':
    print largest_diff([34, 8, 10, 3, 2, 80, 30, 33, 1])
    print largest_diff([9, 2, 3, 4, 5, 6, 7, 8, 18, 0])
    print largest_diff([1, 2, 3, 4, 5, 6])
