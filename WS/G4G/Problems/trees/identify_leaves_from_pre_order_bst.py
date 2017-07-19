"""
msft

more done down

https://stackoverflow.com/questions/42407162/how-to-identify-the-leaf-nodes-of-a-binary-search-tree
"""
from sys import maxint


def get_lesser_range(array, i, n, val):
    a = i
    while i <= n:
        if array[i] < val:
            i += 1

        else:
            break

    return a, i - 1


def get_greater_range(array, i, n, val):
    a = i
    while i <= n:
        if array[i] > val:
            i += 1

        else:
            break

    return a, i - 1


def print_leaves(pre_order, l, r):
    root = pre_order[l]
    a, b = get_lesser_range(pre_order, l + 1, r, root)
    c, d = get_greater_range(pre_order, b + 1, r, root)

    if a == b:
        print pre_order[a],

    else:
        print_leaves(pre_order, a, b)

    if c == d:
        print pre_order[c],

    else:
        print_leaves(pre_order, c, d)


if __name__ == '__main__':
    print_leaves([5, 3, 2, 4, 8, 7, 9], 0, 6)
    print ''


"""
msft

another approach

try tree range check until it fails, when it fails we found a leaf
"""

IDX = 0


def print_all_leaves(pre_order, _min, _max, n):
    global IDX

    if IDX >= n:
        return False

    root = pre_order[IDX]

    if root < _min or root > _max:
        return False

    IDX += 1
    is_fitting_left = print_all_leaves(pre_order, _min, root, n)
    is_fitting_right = print_all_leaves(pre_order, root, _max, n)

    if not is_fitting_left and not is_fitting_right:
        print root,

    return _min < root < _max


if __name__ == '__main__':
    print ''
    print_all_leaves([5, 3, 2, 4, 8, 7, 9], -maxint, maxint, 7)
