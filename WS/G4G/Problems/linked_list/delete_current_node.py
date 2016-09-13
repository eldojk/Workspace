"""
Delete a node from an ll given access to only that node
"""


def delete_node(node):
    if node.nxt:
        node.data = node.nxt.data

        if node.nxt.nxt is None:
            node.nxt = None
        else:
            delete_node(node.nxt)

# start = create_linked_list([1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 4, 7])
# print_ll(start)
# node =  get_node(start, 3)
#
# delete_node(node)
# print_ll(start)
