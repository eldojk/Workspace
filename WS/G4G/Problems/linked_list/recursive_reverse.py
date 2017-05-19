"""
amzn

Recursively reverse LL

#todo
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll

HEAD = None


def reverse(node, prev):
    global HEAD
    if node.nxt:
        node = reverse(node.nxt, node)

    if HEAD is None:
        HEAD = node

    node.nxt = prev
    return prev


def reverse2(node, prev):
    if node is None:
        return prev
    else:
        temp = reverse2(node.nxt, node)
        node.nxt = prev
        return temp


if __name__ == '__main__':
    start = create_linked_list([1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 4, 7])
    print_ll(start)

    new_head = reverse2(start, None)

    print_ll(new_head)
