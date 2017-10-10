"""
amzn

http://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def get_kth_from_start(head, k):
    prev = None
    n = 0
    nxt = head.nxt

    while head:
        n += 1

        if n == k:
            break

        prev = head
        head = head.nxt
        nxt = head.nxt if head is not None else None

    return prev, head, nxt


def get_kth_from_end(head, k):
    p1 = head
    p2 = head
    k -= 1
    prev = None
    nxt = head.nxt

    while k > 0:
        k -= 1
        p1 = p1.nxt

    while p1.nxt is not None:
        p1 = p1.nxt

        prev = p2
        p2 = p2.nxt
        nxt = p2.nxt if p2 else None

    return prev, p2, nxt


def swap_kth_beg_and_end(head, k):
    pre1, n1, nxt1 = get_kth_from_start(head, k)
    pre2, n2, nxt2 = get_kth_from_end(head, k)

    if n1 == n2:
        # they are same
        return

    elif nxt1 == n2:
        # n2 is next to n1
        pre1.nxt = n2
        n2.nxt = n1
        n1.nxt = nxt2

    elif nxt2 == n1:
        # n1 is next 2 n2
        pre2.nxt = n1
        n1.nxt = n2
        n2.nxt = nxt1

    else:
        if pre1 is None:
            # n1 is first
            head = n2
            n2.nxt = nxt1
            pre2.nxt = n1
            n1.nxt = nxt2

        elif pre2 is None:
            # n2 is first
            head = n1
            n1.nxt = nxt2
            pre1.nxt = n2
            n2.nxt = nxt1

        else:
            # somewhere in between
            pre1.nxt = n2
            n2.nxt = nxt1
            pre2.nxt = n1
            n1.nxt = nxt2

    return head


if __name__ == '__main__':
    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 1)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 2)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 3)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 4)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 5)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 6)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 7)
    print_ll(h1)

    print ''

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    h1 = swap_kth_beg_and_end(h, 8)
    print_ll(h1)
