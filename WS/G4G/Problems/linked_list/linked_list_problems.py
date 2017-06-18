from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll, create_circular_linked_list, \
    print_circular_ll, Node


def print_middle(node):
    """
    http://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

    :param node:
    :return:
    """
    fast_ptr = node
    slow_ptr = node
    flip_bit = False

    while fast_ptr is not None:
        fast_ptr = fast_ptr.nxt

        if flip_bit:
            slow_ptr = slow_ptr.nxt

        flip_bit = not flip_bit

    print slow_ptr.data


start = create_linked_list([1, 2, 3, 4, 5])
print_middle(start)
start = create_linked_list([1, 2, 3, 4, 5, 6])
print_middle(start)

print '-----------------------'


def nth_node_from_end(node, n):
    """
    http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/

    :param node:
    :return:
    """
    count = 0
    fast_ptr = node
    slow_ptr = node

    while fast_ptr.nxt is not None:
        count += 1

        fast_ptr = fast_ptr.nxt
        if count >= n:
            slow_ptr = slow_ptr.nxt

    print slow_ptr.data


start = create_linked_list([1, 2, 3, 4, 5, 6])
nth_node_from_end(start, 3)

print '-----------------------'


def delete_ll(node):
    """
    http://www.geeksforgeeks.org/write-a-function-to-delete-a-linked-list/

    :param node:
    :return:
    """
    if node.nxt:
        delete_ll(node.nxt)

    print 'deleting {0}'.format(node.data)
    del node


start = create_linked_list([1, 2, 3, 4, 5, 6])
delete_ll(start)

print '-----------------------'


def sorted_insert(start, node):
    """
    http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/

    :param start:
    :param node:
    :return:
    """
    beginning = start
    if start is None:
        return node
    elif start.data >= node.data:
        node.nxt = start
        return node

    while start.nxt is not None:
        if start.data <= node.data and start.nxt.data >= node.data:
            break

        start = start.nxt

    successor_node = start.nxt
    start.nxt = node
    node.nxt = successor_node
    return beginning


start = create_linked_list([1, 2, 4, 9, 11])
new_ll = sorted_insert(start, Node(7))
print_ll(new_ll)
new_ll = sorted_insert(start, Node(22))
print_ll(new_ll)
new_ll = sorted_insert(start, Node(0))
print_ll(new_ll)

print '-----------------------'


def reverse_print(node):
    """
    http://www.geeksforgeeks.org/write-a-recursive-function-to-print-reverse-of-a-linked-list/

    :param node:
    :return:
    """
    if node.nxt:
        reverse_print(node.nxt)

    print node.data,


start = create_linked_list([1, 2, 4, 9, 11])
reverse_print(start)
print ' '

print '-----------------------'


def remove_duplicates(node):
    """
    http://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/

    :param node:
    :return:
    """
    current = node
    while current.nxt and current.nxt.data == current.data:
        current = current.nxt
        node = current

    if node.nxt:
        node.nxt = remove_duplicates(node.nxt)

    return node


start = create_linked_list([11, 11, 11, 21, 43, 43, 60])
new_ll = remove_duplicates(start)
print_ll(new_ll)

print '-----------------------'


def remove_duplicates_unsorted(node):
    """
    http://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

    :param node:
    :return:
    """
    occured = {}
    current = node
    occured[node.data] = True

    while current and current.nxt:
        occured[current.data] = True
        if occured.get(current.nxt.data):
            node_to_del = current.nxt
            current.nxt = node_to_del.nxt
            del node_to_del

        current = current.nxt

    return node


start = create_linked_list([11, 33, 11, 4, 33, 5, 4])
new_ll = remove_duplicates_unsorted(start)
print_ll(new_ll)
print ''


"""
http://www.geeksforgeeks.org/split-a-circular-linked-list-into-two-halves/
"""


def calc_len_of_cll(head):
    hd = head
    n = 1
    while head.nxt != hd:
        n += 1
        head = head.nxt

    return n


def split_list(dll):
    head = dll
    n = calc_len_of_cll(dll)

    head1 = head
    head2 = None
    tail1 = None
    tail2 = None
    half_len = n / 2
    i = 1

    while i < n:
        head = head.nxt
        i += 1

        if i == half_len:
            head2 = head.nxt
            tail1 = head

        if i == n:
            tail2 = head

    tail1.nxt = head1
    tail2.nxt = head2

    return head1, head2


hd = create_circular_linked_list([1, 2, 3, 4])
h1, h2 = split_list(hd)
print_circular_ll(h1)
print_circular_ll(h2)


"""
http://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/
"""


def get_tail_cll(head):
    h = head
    while head.nxt != h:
        head = head.nxt

    return head


def insert_at_beg_of_cll(head, num):
    tail = get_tail_cll(head)

    node = Node(num)
    tail.nxt = node
    node.nxt = head
    return node


def insert_at_end_of_cll(num, head):
    tail = get_tail_cll(head)

    node = Node(num)
    tail.nxt = node
    node.nxt = head
    return head


def sorted_insert_to_cll(head, num):
    curr = head.nxt
    start = curr
    prev = head

    if num <= head.data:
        return insert_at_beg_of_cll(head, num)

    while True:
        if num <= curr.data:
            print curr, prev
            node = Node(num)
            prev.nxt = node
            node.nxt = curr
            break

        prev = curr
        curr = curr.nxt

        if start == curr:
            head = insert_at_end_of_cll(num, head)
            break

    return head


h1 = sorted_insert_to_cll(create_circular_linked_list([1, 2, 4, 5]), 3)
h2 = sorted_insert_to_cll(create_circular_linked_list([1, 2, 4, 5]), 0)
h3 = sorted_insert_to_cll(create_circular_linked_list([1, 2, 4, 5]), 7)
print_circular_ll(h1)
print_circular_ll(h2)
print_circular_ll(h3)
print ''


"""
amzn, msft

http://www.geeksforgeeks.org/reverse-alternate-k-nodes-in-a-singly-linked-list/
"""


def alternate_reverse(head):
    h = head
    curr = head.nxt

    flag = True
    while curr is not None:
        if flag:
            data = curr.data
            curr.data = h.data
            h.data = data

        h = curr
        curr = curr.nxt
        flag = not flag

    return head


h1 = create_linked_list([1, 2, 3, 4, 5, 6])
print_ll(alternate_reverse(h1))

h2 = create_linked_list([1, 2, 3, 4, 5])
print_ll(alternate_reverse(h2))

h3 = create_linked_list([1, 2])
print_ll(alternate_reverse(h3))

h4 = create_linked_list([1])
print_ll(alternate_reverse(h4))
print ''


"""
http://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/
"""


def delete_nodes_with_grtr_val_on_right(head):
    h = head
    prev = None
    nxt = h.nxt

    while nxt is not None:
        if nxt.data > h.data:
            # remove from beginning
            if h == head:
                h = nxt
                head = h
                prev = None
                nxt = nxt.nxt
                continue

            if prev:
                prev.nxt = nxt

        prev = h
        h = nxt
        nxt = nxt.nxt

    return head


h = create_linked_list([12, 15, 10, 11, 5, 6, 2, 3])
print_ll(delete_nodes_with_grtr_val_on_right(h))
print ''


"""
sorted insert to ll
"""


def insert_to_sorted_ll(head, data):
    if head is None:
        return Node(data)

    if head.data > data:
        h = Node(data)
        h.nxt = head
        return h

    head.nxt = insert_to_sorted_ll(head.nxt, data)
    return head


if __name__ == '__main__':
    h = create_linked_list([1, 4, 7, 8, 12])

    h = insert_to_sorted_ll(h, 5)
    print_ll(h)

    h = insert_to_sorted_ll(h, 0)
    print_ll(h)

    h = insert_to_sorted_ll(h, 13)
    print_ll(h)


"""
amzn

http://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/
"""


def zig_zag_ll(head):
    # similar to zig zag array
    flag = True

    curr = head

    while curr.nxt is not None:

        if flag:
            if curr.data > curr.nxt.data:
                curr.data, curr.nxt.data = curr.nxt.data, curr.data

        else:
            if curr.data < curr.nxt.data:
                curr.data, curr.nxt.data = curr.nxt.data, curr.data

        flag = not flag
        curr = curr.nxt

    return head


if __name__ == '__main__':
    print ''
    h = create_linked_list([4, 3, 7, 8, 6, 2, 1])
    res = zig_zag_ll(h)
    print_ll(res)


"""
amzn

http://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/
"""


def delete_n_after_m(head, m, n):
    h = head

    while h is not None:
        _m = m

        while h is not None and _m > 1:
            h = h.nxt
            _m -= 1

        _n = n

        while h is not None and h.nxt is not None and _n > 0:
            h.nxt = h.nxt.nxt
            _n -= 1

        h = h.nxt

    return h


if __name__ == '__main__':
    print ''
    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    delete_n_after_m(h, 2, 2)
    print_ll(h)

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    delete_n_after_m(h, 2, 2)
    print_ll(h)

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    delete_n_after_m(h, 3, 2)
    print_ll(h)

    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    delete_n_after_m(h, 1, 1)
    print_ll(h)
