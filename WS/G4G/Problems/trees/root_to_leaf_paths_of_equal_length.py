"""
http://www.geeksforgeeks.org/root-leaf-paths-equal-lengths-binary-tree/
"""
from copy import copy

from G4G.Problems.bst.vertical_sum import Node


def is_leaf(root):
    return root.left is None and root.right is None


def print_paths_of_equal_length(root, stack, curr_len, mp):
    if root:
        stack.append(root.data)
        if is_leaf(root):
            if mp.get(curr_len) is None:
                mp[curr_len] = [copy(stack)]
            else:
                mp[curr_len].append(copy(stack))

        print_paths_of_equal_length(root.left, stack, curr_len + 1, mp)
        print_paths_of_equal_length(root.right, stack, curr_len + 1, mp)
        stack.pop()


def paths(root):
    stack = []
    mp = {}
    print_paths_of_equal_length(root, stack, 1, mp)
    for val in mp.values():
        print val


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    root.right.right = Node(4)

    paths(root)
