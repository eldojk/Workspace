"""
http://www.geeksforgeeks.org/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def attach_to_list(node, head, tail):
    if head is None:
        head = node
        tail = head
    else:
        tail.nxt = node
        tail = tail.nxt

    nxt = node.nxt
    tail.nxt = None

    return nxt, head, tail


def partition_ll(head, partition_value):
    h = head

    ltll_h = None
    ltll_t = None
    gtll_h = None
    gtll_t = None
    eqll_t = None
    eqll_h = None

    while h is not None:
        if h.data < partition_value:
            h, ltll_h, ltll_t = attach_to_list(h, ltll_h, ltll_t)

        elif h.data == partition_value:
            h, eqll_h, eqll_t = attach_to_list(h, eqll_h, eqll_t)

        else:
            h, gtll_h, gtll_t = attach_to_list(h, gtll_h, gtll_t)

    new_head = None
    new_tail = None

    if ltll_h:
        new_head = ltll_h
        new_tail = ltll_t

    if eqll_h:
        if new_head:
            new_tail.nxt = eqll_h
        else:
            new_head = eqll_h
            new_tail = eqll_t

    if gtll_h:
        if new_head:
            new_tail.nxt = gtll_h
        else:
            new_head = gtll_h

    return new_head


if __name__ == '__main__':
    ll = create_linked_list([1, 4, 3, 2, 5, 2, 3])
    res = partition_ll(ll, 3)
    print_ll(res)

    print ''

    ll = create_linked_list([1, 4, 2, 10])
    res = partition_ll(ll, 3)
    print_ll(res)

    print ''

    ll = create_linked_list([10, 4, 20, 10, 3])
    res = partition_ll(ll, 3)
    print_ll(res)