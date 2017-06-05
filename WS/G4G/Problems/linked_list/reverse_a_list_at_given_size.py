"""
amzn

http://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/

a generic solution for this is implemented:
http://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/

different implementation :)
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def get_next_head_and_tail_with_k_distance(ptr, k):
    h = ptr
    t = None

    while ptr is not None and k > 0:
        t = ptr
        ptr = ptr.nxt
        k -= 1

    return h, t


def reverse_from_head_to_tail(head, tail):
    if head == tail:
        return head, tail

    else:
        new_head, new_tail = reverse_from_head_to_tail(head.nxt, tail)
        head.nxt = new_tail.nxt
        new_tail.nxt = head
        return new_head, head


def reverse_at_k_groups(head, k):
    prev = None
    head_to_return = None
    ptr = head

    while True:
        if ptr is None:
            break

        h, t = get_next_head_and_tail_with_k_distance(ptr, k)
        nh, nt = reverse_from_head_to_tail(h, t)

        if prev is None:
            head_to_return = nh

        else:
            prev.nxt = nh

        prev = nt
        ptr = nt.nxt

    return head_to_return


if __name__ == '__main__':
    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
    rl = reverse_at_k_groups(h, 3)
    print_ll(rl)