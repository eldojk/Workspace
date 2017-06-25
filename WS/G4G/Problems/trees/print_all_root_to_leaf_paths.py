"""
http://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
"""
from G4G.Problems.bst.vertical_sum import Node


def is_leaf(node):
    return node.left is None and node.right is None


def print_all_paths(root, arr):
    if root:
        arr.append(root)

        print_all_paths(root.left, arr)
        print_all_paths(root.right, arr)

        if is_leaf(root):
            print " ".join(map(str, arr))

        arr.pop()


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print_all_paths(root, [])


"""
amzn, goog

http://www.geeksforgeeks.org/print-all-root-to-leaf-paths-with-there-relative-positions/
"""


def print_underscores(num):
    while num > 0:
        print '_',
        num -= 1


def print_with_underscore(path):
    offset_required = min([entry[1] for entry in path])

    # if there are elements going left, adjust everything rightward
    if offset_required < 0:
        path = [[entry[0], entry[1] + abs(offset_required)] for entry in path]

    for entry in path:
        num_scores = entry[1]
        element = entry[0]
        print_underscores(num_scores)
        print element

    print ''


def print_root_to_leaf_paths_with_rel_pos(root, path, hd):
    if root is None:
        return

    path.append([root.data, hd])
    print_root_to_leaf_paths_with_rel_pos(root.left, path, hd - 1)
    print_root_to_leaf_paths_with_rel_pos(root.right, path, hd + 1)

    if is_leaf(root):
        print_with_underscore(path)

    path.pop()


if __name__ == '__main__':
    print ''
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    root.right.right = Node('G')

    print_root_to_leaf_paths_with_rel_pos(root, [], 0)