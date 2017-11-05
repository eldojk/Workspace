"""
http://www.geeksforgeeks.org/rotate-a-linked-list/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll
from G4G.Problems.linked_list.segregate_odd_and_even_in_ll import get_tail_ll


def rotate_ll(head, k):
    # converting to circular ll temporarily
    tail = get_tail_ll(head)
    tail.nxt = head

    while k > 0:
        tail = head
        head = head.nxt
        k -= 1

    tail.nxt = None
    return head


if __name__ == '__main__':
    h = create_linked_list([1, 2, 3, 4, 5, 6])
    n = rotate_ll(h, 9)
    print_ll(n)
