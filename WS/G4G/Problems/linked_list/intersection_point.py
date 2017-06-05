"""
http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def count_nodes(head):
    counter = 0

    while head:
        counter += 1
        head = head.nxt

    return counter


def get_intersection_point(h1, h2):
    c1 = count_nodes(h1)
    c2 = count_nodes(h2)

    bl = h1 if c1 >= c2 else h2
    sl = h1 if bl == h2 else h2

    diff = abs(c1 - c2)

    while diff > 0:
        bl = bl.nxt
        diff -= 1

    while bl is not None and sl is not None and bl != sl:
        bl = bl.nxt
        sl = sl.nxt

    return bl


if __name__ == '__main__':
    l1 = create_linked_list([1, 2, 3, 4, 5, 6])
    l2 = create_linked_list([8, 9])
    l2.nxt.nxt = l1.nxt.nxt.nxt

    print get_intersection_point(l1, l2)