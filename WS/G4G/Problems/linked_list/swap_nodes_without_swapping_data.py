"""
amzn

#tricky
(because, notice the use of index. If we use index info we can make better
decisions about position of nodes. #tricky tagged because of this. Just
wanted to notice the use of indexes in linked lists)

http://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def find_nodes(head, data):
    _prev = None
    node = head
    _next = head.nxt

    idx = 0
    while node is not None:
        if node.data == data:
            return _prev, node, _next, idx

        idx += 1
        _prev = node
        node = node.nxt

        if node:
            _next = node.nxt

    return None, None, None


def swap(head, n1, n2):
    p_node1, node1, n_node1, idx1 = find_nodes(head, n1)
    p_node2, node2, n_node2, idx2 = find_nodes(head, n2)

    first = node1
    second = node2
    pf = p_node1
    nf = n_node1
    ps = p_node2
    ns = n_node2

    if idx1 > idx2:
        first = node2
        second = node1
        pf = p_node2
        nf = n_node2
        ps = p_node1
        ns = n_node1

    # adjacent
    if first.nxt == second:
        # if first is left most
        if pf:
            pf.nxt = second

        first.nxt = second.nxt
        second.nxt = first

    else:
        if pf:
            pf.nxt = second

        first.nxt = ns
        second.nxt = nf
        ps.nxt = first

    # return new head if head was swapped
    return second if head == first else head


if __name__ == '__main__':
    h = create_linked_list([10, 15, 12, 13, 20, 14])
    h = swap(h, 12, 20)
    print_ll(h)

    h = create_linked_list([10, 15, 12, 13, 20, 14])
    h = swap(h, 10, 20)
    print_ll(h)

    h = create_linked_list([10, 15, 12, 13, 20, 14])
    h = swap(h, 12, 13)
    print_ll(h)

    h = create_linked_list([10, 15, 12, 13, 20, 14])
    h = swap(h, 12, 14)
    print_ll(h)

    h = create_linked_list([10, 15, 12, 13, 20, 14])
    h = swap(h, 10, 14)
    print_ll(h)
