"""
kth node from end using recursion and stack unwinding
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def kth_node_from_end(node, n, k):
    data = None
    if node.nxt:
        n, data = kth_node_from_end(node.nxt, n, k)

    n += 1
    if n == k:
        return n, node.data

    return n, data


def kth_node(start, n):
    n, data = kth_node_from_end(start, 0, n)
    return data


if __name__ == '__main__':
    start = create_linked_list([1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 4, 7])
    print_ll(start)
    print kth_node(start, 4)
