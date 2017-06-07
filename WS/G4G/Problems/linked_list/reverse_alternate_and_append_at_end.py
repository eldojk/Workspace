"""
http://www.geeksforgeeks.org/given-linked-list-reverse-alternate-nodes-append-end/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll
from G4G.Problems.linked_list.recursive_reverse import reverse2


def split_alternate_nodes(head):
    l1 = head
    l2 = head.nxt
    t1 = l1
    t2 = l2

    while t2 is not None:
        n1 = t2.nxt

        if n1 is None:
            n2 = None
        else:
            n2 = t2.nxt.nxt

        t1.nxt = n1
        t2.nxt = n2

        t1 = n1
        t2 = n2

    if t1:
        t1.nxt = None

    if t2:
        t2.nxt = None

    return l1, l2


def split_and_reverse(head):
    h1, h2 = split_alternate_nodes(head)
    h2_rev = reverse2(h2, None)

    t = h1
    while t.nxt is not None:
        t = t.nxt

    t.nxt = h2_rev
    return h1


if __name__ == '__main__':
    l = create_linked_list([1, 2, 3, 4, 5, 6])
    res = split_and_reverse(l)
    print_ll(res)

    l = create_linked_list([12, 14, 16, 18, 20])
    res = split_and_reverse(l)
    print_ll(res)