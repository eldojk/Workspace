"""
Given Inorder Traversal of a Special Binary Tree in which key of every node is greater than keys in left and right
children, construct the Binary Tree and return root.

Examples:

Input: inorder[] = {5, 10, 40, 30, 28}
Output: root of following tree
         40
       /   \
      10     30
     /         \
    5          28

Input: inorder[] = {1, 5, 10, 40, 30,
                    15, 28, 20}
Output: root of following tree
          40
        /   \
       10     30
      /         \
     5          28
    /          /  \
   1         15    20
"""
from G4G.Problems.bst.vertical_sum import Node


def find_max_index(arr, start, end):
    max_index = start
    for i in range(start, end + 1):
        if arr[i] > arr[max_index]:
            max_index = i

    return max_index


def build_tree(arr, start, end):
    if start > end:
        return

    root_index = find_max_index(arr, start, end)
    root = Node(arr[root_index])

    root.left = build_tree(arr, start, root_index - 1)
    root.right = build_tree(arr, root_index + 1, end)

    return root


# r = build_tree([1, 5, 10, 40, 30, 15, 28, 20], 0, 7)
# print r
# print r.left
# print r.right
# print r.left.left
# print r.right.right
# print r.left.left.left
# print r.right.right.left
# print r.right.right.right