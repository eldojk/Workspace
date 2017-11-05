"""
amzn
(more down)

Recursively reverse LL
http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/

#todo
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


HEAD = None


def reverse(node, prev):
    global HEAD
    if node.nxt:
        node = reverse(node.nxt, node)

    if HEAD is None:
        HEAD = node

    node.nxt = prev
    return prev


def reverse2(node, prev):
    if node is None:
        return prev
    else:
        temp = reverse2(node.nxt, node)
        node.nxt = prev
        return temp


if __name__ == '__main__':
    start = create_linked_list([1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 4, 7])
    print_ll(start)

    new_head = reverse2(start, None)

    print_ll(new_head)


"""
Iterative reverse
"""


def iterative_reverse(head):
    prev = head
    curr = head.nxt
    prev.nxt = None

    while curr:
        next_node = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = next_node

    return prev


if __name__ == '__main__':
    print ''
    print 'Iterative rev'
    print ''

    h1 = create_linked_list([1, 2, 3, 4, 5])
    rh1 = iterative_reverse(h1)
    print_ll(rh1)

    print ''

    h1 = create_linked_list([1, 2, 3])
    rh1 = iterative_reverse(h1)
    print_ll(rh1)

    print ''

    h1 = create_linked_list([1, 2])
    rh1 = iterative_reverse(h1)
    print_ll(rh1)

    print ''

    h1 = create_linked_list([1])
    rh1 = iterative_reverse(h1)
    print_ll(rh1)
