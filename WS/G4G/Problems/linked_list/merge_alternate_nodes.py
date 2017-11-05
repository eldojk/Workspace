"""
http://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def merge_alternate(l1, l2):
    list1 = False
    head = l1
    tail = l1
    l1 = l1.nxt

    while l1 is not None or l2 is not None:
        if l1 is None:
            tail.nxt = l2
            tail = l2
            l2 = l2.nxt

        elif l2 is None:
            tail.nxt = l1
            tail = l1
            l1 = l1.nxt

        elif list1:
            tail.nxt = l1
            tail = l1
            l1 = l1.nxt
        else:
            tail.nxt = l2
            tail = l2
            l2 = l2.nxt

        list1 = not list1

    return head


if __name__ == '__main__':
    h1 = create_linked_list([5, 7, 17, 13, 11])
    h2 = create_linked_list([12, 10, 2, 4, 6])
    res = merge_alternate(h1, h2)

    print_ll(res)

    print ''

    h1 = create_linked_list([1, 2, 3])
    h2 = create_linked_list([4, 5, 6, 7, 8])
    res = merge_alternate(h1, h2)

    print_ll(res)
