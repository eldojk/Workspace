"""
Delete a node from an ll given access to only that node
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll, get_node


def delete_node(node):
    if node.nxt:
        next_node = node.nxt
        node.data = next_node.data
        node.nxt = next_node.nxt
        next_node.nxt = None
        del next_node


start = create_linked_list([1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 4, 7])
print_ll(start)
node = get_node(start, 3)
print node.data

delete_node(node)
print_ll(start)
