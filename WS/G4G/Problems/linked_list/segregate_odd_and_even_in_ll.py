"""
amzn, msft

http://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

better way: just append odd to one list and even to another and merge them
^ coded down
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def get_tail_ll(head):
    while head.nxt is not None:
        head = head.nxt

    return head


def move_node_to_end(prev, h, nxt, is_head, tail):
    if is_head:
        prev = None
    else:
        prev.nxt = nxt

    tail.nxt = h
    tail = tail.nxt
    tail.nxt = None

    h = nxt
    nxt = nxt.nxt
    return prev, h, nxt, tail


def segregate_odd_and_even(head):
    """
    traverse and move odd nodes to the end

    :param head:
    :return:
    """
    h = head
    t = get_tail_ll(head)

    prev = None
    nxt = h.nxt
    first_node_to_move = None

    while nxt is not None:
        if h.data % 2 != 0:
            # logic to check if we encountered a node that is already moved
            if h == first_node_to_move:
                break

            if first_node_to_move is None:
                first_node_to_move = h

            # update head ptr if head was moved
            if head == h:
                prev, h, nxt, t = move_node_to_end(prev, h, nxt, True, t)
                head = h
            else:
                prev, h, nxt, t = move_node_to_end(prev, h, nxt, False, t)
        else:
            prev = h
            h = nxt
            nxt = nxt.nxt

    return head


if __name__ == '__main__':
    _h = create_linked_list([17, 15, 8, 12, 10, 5, 4, 1, 7, 6])
    print_ll(segregate_odd_and_even(_h))


"""
better approach
"""


def add_to_ll(head, tail, node):
    if head:
        tail.nxt = node
        return head, node

    return node, node


def segregate_odd_and_even_another_app(head):
    odd_h = odd_t = even_h = even_t = None

    while head is not None:
        nxt = head.nxt
        head.nxt = None

        if head.data % 2 == 0:
            even_h, even_t = add_to_ll(even_h, even_t, head)

        else:
            odd_h, odd_t = add_to_ll(odd_h, odd_t, head)

        head = nxt

    if even_t:
        even_t.nxt = odd_h
        return even_h

    return odd_h


if __name__ == '__main__':
    _h = create_linked_list([17, 15, 8, 12, 10, 5, 4, 1, 7, 6])
    print_ll(segregate_odd_and_even_another_app(_h))
