"""
http://www.geeksforgeeks.org/maximum-consecutive-increasing-path-length-in-binary-tree/

sending elements bottom up
"""
from G4G.Problems.bst.vertical_sum import Node


MAX_LEN_PATH = []


def longest_path(root):
    global MAX_LEN_PATH
    if root is None:
        return []

    left_path = longest_path(root.left)
    right_path = longest_path(root.right)

    max_len_path = left_path if len(left_path) > len(right_path) else right_path

    if len(max_len_path) == 0:
        max_len_path = [root.data]

    elif max_len_path[-1] > root.data:
        max_len_path += [root.data]

    else:
        max_len_path = [root.data]

    if len(max_len_path) > len(MAX_LEN_PATH):
        MAX_LEN_PATH = max_len_path

    return max_len_path


def print_longest_path(root):
    longest_path(root)
    for el in reversed(MAX_LEN_PATH):
        print el,


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(11)
    r.left.right = Node(12)
    r.left.left = Node(13)
    r.right = Node(9)
    r.right.left = Node(13)
    r.right.right = Node(8)

    print_longest_path(r)
    print ''
    MAX_LEN_PATH = []

    r = Node(5)
    r.left = Node(8)
    r.left.left = Node(9)
    r.left.left.left = Node(6)
    r.right = Node(11)
    r.right.right = Node(10)
    r.right.right.left = Node(15)

    print_longest_path(r)