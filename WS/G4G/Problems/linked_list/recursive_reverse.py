"""
Recursively reverse LL

#todo
"""

head = None


def reverse(node, prev):
    global head
    if node.nxt:
        node = reverse(node.nxt, node)

    if head is None:
        head = node

    node.nxt = prev
    return prev


def reverse2(node, prev):
    if node is None:
        return prev
    else:
        temp = reverse(node.nxt, node)
        node.nxt = prev
        return temp

# start = create_linked_list([1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 4, 7])
# print_ll(start)
#
# reverse2(start, None)
#
# print_ll(head)
