"""
amzn

find and remove a loop in ll
http://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def has_loop(head):
    f_ptr = head
    s_ptr = head

    # fast ptr and slow ptr will meet if there's a loop
    while f_ptr is not None and s_ptr is not None:
        f_ptr = f_ptr.nxt

        if f_ptr == s_ptr:
            return True, f_ptr, s_ptr

        if f_ptr is None:
            return False, f_ptr, s_ptr

        f_ptr = f_ptr.nxt

        if f_ptr == s_ptr:
            return True, f_ptr, s_ptr

        s_ptr = s_ptr.nxt

    return False, f_ptr, s_ptr


def remove_loop(head):
    hl, p1, p2 = has_loop(head)

    if hl:
        # count num nodes in loop
        k = 1

        while p1.nxt != p2:
            p1 = p1.nxt
            k += 1

        p1 = head
        p2 = head

        # move p2 k nodes from head
        for i in range(k):
            p2 = p2.nxt

        # Move both pointers at the same place
        # they will meet at loop starting node

        while p1 != p2:
            p1 = p1.nxt
            p2 = p2.nxt

        # Get pointer to the last node
        while p2.nxt != p1:
            p2 = p2.nxt

        p2.nxt = None


if __name__ == '__main__':
    start = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])

    p3 = start.nxt.nxt

    t = start
    while t.nxt is not None:
        t = t.nxt

    t.nxt = p3

    print has_loop(start)

    remove_loop(start)

    print_ll(start)