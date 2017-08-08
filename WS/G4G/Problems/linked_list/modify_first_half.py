# coding=utf-8
"""
Given a singly linked list containing n nodes. Modify the value of first half nodes such that 1st node’s new value is
equal to the last node’s value minus first node’s current value, 2nd node’s new value is equal to the second last node’s
value minus 2nd node’s current value, likewise for first half nodes. If n is odd then the value of the middle node
remains unchanged.
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def count_nodes(head):
    n = 0

    while head is not None:
        n += 1
        head = head.nxt

    return n


def modify_first_half(node, complement, n):
    if node is None:
        return complement
    else:
        first = modify_first_half(node.nxt, complement, n)

        if n[0] < n[1]:
            first.data = first.data - node.data
            n[0] += 1

        return first.nxt


def modify_list(head):
    cnt = count_nodes(head)
    n = [0, cnt // 2]

    modify_first_half(head, head, n)
    return head


if __name__ == '__main__':
    h = create_linked_list([10, 4, 5, 3, 6])
    modify_list(h)
    print_ll(h)

    h = create_linked_list([2, 9, 8, 12, 7, 10])
    modify_list(h)
    print_ll(h)
