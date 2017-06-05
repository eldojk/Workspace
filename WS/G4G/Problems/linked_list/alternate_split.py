"""
http://www.geeksforgeeks.org/alternating-split-of-a-given-singly-linked-list/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def alternate_split(head):
    a = head
    b = head.nxt

    h1 = a
    h2 = b

    while b is not None and b.nxt is not None:
        a.nxt = a.nxt.nxt
        b.nxt = b.nxt.nxt

        a = a.nxt
        b = b.nxt

    a.nxt = None

    return h1, h2


if __name__ == '__main__':
    h = create_linked_list([0, 1, 0, 1, 0, 1])
    _h1, _h2 = alternate_split(h)
    print_ll(_h1)
    print_ll(_h2)

    print ''

    h = create_linked_list([0, 1, 0, 1, 0])
    _h1, _h2 = alternate_split(h)
    print_ll(_h1)
    print_ll(_h2)

    print ''

    h = create_linked_list([0, 1])
    _h1, _h2 = alternate_split(h)
    print_ll(_h1)
    print_ll(_h2)