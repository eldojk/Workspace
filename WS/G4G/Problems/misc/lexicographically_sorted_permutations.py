"""
amzn

http://www.geeksforgeeks.org/lexicographic-permutations-of-string/
"""


def sort(li, i, j):
    li[i:j] = sorted(li[i:j])


def swap(li, i, j):
    ch = li[i]
    li[i] = li[j]
    li[j] = ch


def print_permutations(li, i, n):
    if i == n:
        print ''.join(li)
        return

    sort(li, i, n)

    for j in range(i, n):

        while (j < n - 1) and li[j] == li[j + 1]:
            j += 1

        swap(li, i, j)

        print_permutations(li, i + 1, n)

        swap(li, i, j)


if __name__ == '__main__':
    print_permutations(list('abc'), 0, 3)