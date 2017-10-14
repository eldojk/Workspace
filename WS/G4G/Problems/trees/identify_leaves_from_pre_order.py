"""
amzn msft

https://stackoverflow.com/questions/42407162/how-to-identify-the-leaf-nodes-of-a-binary-search-tree

[5,3,2,4,8,7,9]
"""
from sys import maxint

PRE_INDEX = 0


def id_leaves(pre_order, _min, _max):
    global PRE_INDEX

    if PRE_INDEX >= len(pre_order):
        return 0

    root = pre_order[PRE_INDEX]

    if not (_min < root < _max):
        return 0

    PRE_INDEX += 1

    l_count = id_leaves(pre_order, _min, root)
    r_count = id_leaves(pre_order, root, _max)

    if l_count == 0 and r_count == 0:
        print root,

    return 1 + l_count + r_count


"""
another approach
"""


def id_leaves2(array, i, j):
    if i > j:
        return

    if i == j:
        print array[i],
        return

    root = array[i]
    a = i + 1
    b = j
    k = a

    while array[k] < root:
        k += 1

    id_leaves2(array, a, k - 1)
    id_leaves2(array, k, b)


if __name__ == '__main__':
    id_leaves([5, 3, 2, 4, 8, 7, 9], -maxint, maxint)
    print ''
    id_leaves2([5, 3, 2, 4, 8, 7, 9], 0, 6)
