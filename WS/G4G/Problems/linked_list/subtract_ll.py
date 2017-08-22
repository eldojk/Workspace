"""
amzn

http://www.geeksforgeeks.org/subtract-two-numbers-represented-as-linked-lists/

Input  : l1 = 1 -> 0 -> 0 -> NULL,  l2 = 1 -> NULL
Output : 0->9->9->NULL

Input  : l1 = 1 -> 0 -> 0 -> NULL,  l2 = 1 -> NULL
Output : 0->9->9->NULL

Input  : l1 = 7-> 8 -> 6 -> NULL,  l2 = 7 -> 8 -> 9 NULL
Output : 3->NULL
"""
from G4G.Problems.linked_list.linked_list import Node, create_linked_list, print_ll


def find_ll_length(head):
    n = 0

    while head is not None:
        n += 1
        head = head.nxt

    return n


def compare_ll(h1, h2):
    result = 0
    while h1 is not None:
        if h1.data > h2.data:
            result = 1
            break

        elif h1.data < h2.data:
            result = -1
            break

        h1 = h1.nxt
        h2 = h2.nxt

    return result


def append_zeroes(head, n):
    h = t = None

    while n > 0:

        if t is None:
            h = t = Node(0)

        else:
            t.nxt = Node(0)
            t = t.nxt

        n -= 1

    t.nxt = head
    return h


def get_subtract_able_lists(h1, h2):
    n1 = find_ll_length(h1)
    n2 = find_ll_length(h2)

    if n1 > n2:
        a = h1
        b = append_zeroes(h2, n1 - n2)

    elif n2 > n1:
        a = h2
        b = append_zeroes(h1, n2 - n1)

    else:
        cmp_result = compare_ll(h1, h2)

        if cmp_result == 0:
            return h1, h2

        elif cmp_result == -1:
            a = h2
            b = h1

        else:
            a = h1
            b = h2

    return a, b


def subtract_recur(h1, h2):
    if h1 is None:
        return 0

    else:
        carry = subtract_recur(h1.nxt, h2.nxt)
        a = h1.data
        b = h2.data
        b += carry

        if a >= b:
            h1.data = a - b
            carry = 0

        else:
            a += 10
            h1.data = a - b
            carry = 1

        return carry


def subtract_ll(h1, h2):
    a, b = get_subtract_able_lists(h1, h2)
    subtract_recur(a, b)
    return a


if __name__ == '__main__':
    head1 = create_linked_list([1, 0, 0])
    head2 = create_linked_list([1])
    res = subtract_ll(head1, head2)
    print_ll(res)

    head1 = create_linked_list([7, 8, 6])
    head2 = create_linked_list([7, 8, 9])
    res = subtract_ll(head1, head2)
    print_ll(res)
