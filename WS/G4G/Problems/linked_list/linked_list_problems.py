from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll, Node


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
