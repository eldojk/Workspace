"""
amzn

#tricky
(more down)
print paths summing up to a given value

http://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
"""
from DS.algos.graphs.binary_tree import Node


def print_path(path, i, j):
    while i <= j:
        print path[i],
        i += 1

    print ''


def paths_sum_to_k(root, path, k):
    if root is None:
        return

    path.append(root.data)

    paths_sum_to_k(root.left, path, k)
    paths_sum_to_k(root.right, path, k)

    current_sum = 0
    m = len(path) - 1
    n = m

    while m >= 0:
        current_sum += path[m]

        if current_sum == k:
            print_path(path, m, n)

        m -= 1

    path.pop()


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(3)
    r.right = Node(-1)
    r.left.left = Node(2)
    r.left.right = Node(1)
    r.right.left = Node(4)
    r.right.right = Node(5)
    r.left.right.left = Node(1)
    r.right.left.left = Node(1)
    r.right.left.right = Node(2)
    r.right.right.right = Node(6)

    paths_sum_to_k(r, [], 5)


"""
consider every node as a potential root
"""


def path_with_sum_k(root, curr_sum, k):
    if root is None:
        return False

    curr_sum += root.data

    if curr_sum == k:
        return True

    result = path_with_sum_k(root.left, curr_sum, k)

    if result:
        return result

    result = path_with_sum_k(root.right, curr_sum, k)

    if result:
        return result

    result = path_with_sum_k(root.left, 0, k)

    if result:
        return result

    return path_with_sum_k(root.right, 0, k)


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(3)
    r.right = Node(-1)
    r.left.left = Node(2)
    r.left.right = Node(1)
    r.right.left = Node(4)
    r.right.right = Node(5)
    r.left.right.left = Node(1)
    r.right.left.left = Node(1)
    r.right.left.right = Node(2)
    r.right.right.right = Node(6)

    print path_with_sum_k(r, 0, 5)
