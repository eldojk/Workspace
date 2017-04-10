"""
amzn

http://www.geeksforgeeks.org/diagonal-sum-binary-tree/
http://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


SUMS = {}


def diagonal_sum(root, level):
    global SUMS
    if root:
        SUMS[level] = root.data if SUMS.get(level) is None else SUMS[level] + root.data

        diagonal_sum(root.right, level)
        diagonal_sum(root.left, level + 1)


def diagonal_traversal(root, level, di):
    if root:
        if di.get(level):
            di[level].append(root.data)

        else:
            di[level] = [root.data]

        diagonal_traversal(root.right, level, di)
        diagonal_traversal(root.left, level + 1, di)


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    diagonal_sum(r, 0)
    print SUMS


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    d = {}
    diagonal_traversal(r, 0, d)

    print ''
    for k in sorted(d.keys()):
        print d[k]



