"""
print paths summing up to a given value
"""


def print_path(path, i, j):
    print " -> ".join(path[i:j + 1])


def get_depth(root):
    if root is None:
        return 0

    return 1 + max(get_depth(root.left), get_depth(root.right))


def find_sum(node, s, path, level):
    if node is None:
        return

    path[level] = node.data
    i = level

    curr_sum = 0
    while i >= 0:
        curr_sum += path[i]
        if curr_sum == s:
            print_path(path, i, level)

    find_sum(node.left, s, path, level + 1)
    find_sum(node.right, s, path, level + 1)


def find_sum_paths(root, sum_to_find):
    depth = get_depth(root)
    path = [None for i in range(depth)]
    find_sum(root, sum_to_find, path, 0)
