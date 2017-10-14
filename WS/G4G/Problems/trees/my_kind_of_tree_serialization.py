"""
amzn

Found here: refer http://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
(http://www.geeksforgeeks.org/serialize-deserialize-binary-tree/)
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

    _r = deserialize('ABD$$E$$CF$$G$$', 14)
    print _r
    print _r.left, _r.right
    print _r.left.left, _r.left.right, _r.right.left, _r.right.right

    r = Node('A')
    r.left = Node('B')
    r.right = Node('C')
    r.left.left = Node('D')
    r.right.left = Node('F')

    IDX = 0

    print ''
    s = serialize(r)
    print s

    _r = deserialize(s, 10)
    print _r
    print _r.left, _r.right
    print _r.left.left, _r.left.right, _r.right.left, _r.right.right
