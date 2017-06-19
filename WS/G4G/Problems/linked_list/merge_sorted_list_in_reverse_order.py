"""
msft

http://www.geeksforgeeks.org/merge-two-sorted-linked-lists-such-that-merged-list-is-in-reverse-order/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def add_to_list(node, head):
    node.nxt = head
    return node


def merge_sorted_lls(head1, head2):
    head = None

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            node = head1
            head1 = head1.nxt
            head = add_to_list(node, head)

        else:
            node = head2
            head2 = head2.nxt
            head = add_to_list(node, head)

    while head1 is not None:
        node = head1
        head1 = head1.nxt
        head = add_to_list(node, head)

    while head2 is not None:
        node = head2
        head2 = head2.nxt
        head = add_to_list(node, head)

    return head


if __name__ == '__main__':
    h1 = create_linked_list([5, 10, 15, 40])
    h2 = create_linked_list([2, 3, 20])

    h = merge_sorted_lls(h1, h2)
    print_ll(h)