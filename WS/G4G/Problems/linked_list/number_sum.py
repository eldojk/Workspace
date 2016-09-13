"""
LL represent number in reverse order. add two numbers represented by two lls and give new ll
"""
from linked_list import Node


def get_number(node):
    digit = 1
    val = 0

    while node is not None:
        val += node.data * digit
        digit *= 10
        node = node.nxt

    return val


def create_ll_from_num(num):
    prev = None
    start = None
    while num > 0:
        digit = num % 10
        node = Node(digit)

        if start is None:
            start = node

        if prev:
            prev.nxt = node

        prev = node
        num = (num - digit) / 10

    return start


def sum_ll(node1, node2):
    n1 = get_number(node1)
    n2 = get_number(node2)

    num = n1 + n2

    return create_ll_from_num(num)

# l1 = create_linked_list([1, 2, 3, 4])
# l2 = create_linked_list([1, 2, 3, 4])
# print_ll(sum_ll(l1, l2))
