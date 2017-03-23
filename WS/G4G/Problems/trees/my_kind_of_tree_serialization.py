"""
Found here: refer http://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
"""
from DS.algos.graphs.binary_tree import Node


def serialize(root):
    if root is None:
        return '$'

    left_val = serialize(root.left)
    right_val = serialize(root.right)

    return root.data + left_val + right_val


IDX = 0


def deserialize(string, m):
    global IDX
    if IDX > m:
        return None

    if string[IDX] == '$':
        IDX += 1
        return None

    root = Node(string[IDX])
    IDX += 1

    root.left = deserialize(string, m)
    root.right = deserialize(string, m)

    return root


if __name__ == '__main__':
    r = Node('A')
    r.left = Node('B')
    r.right = Node('C')
    r.left.left = Node('D')
    r.left.right = Node('E')
    r.right.left = Node('F')
    r.right.right = Node('G')

    print serialize(r)

    root = deserialize('ABD$$E$$CF$$G$$', 14)
    print root
    print root.left, root.right
    print root.left.left, root.left.right, root.right.left, root.right.right

    r = Node('A')
    r.left = Node('B')
    r.right = Node('C')
    r.left.left = Node('D')
    r.right.left = Node('F')

    IDX = 0

    print ''
    s = serialize(r)
    print s

    root = deserialize(s, 10)
    print root
    print root.left, root.right
    print root.left.left, root.left.right, root.right.left, root.right.right