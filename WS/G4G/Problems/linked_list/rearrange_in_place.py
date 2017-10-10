"""
amzn

http://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/

Examples:
Input:  1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3

Input:  1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def rearrange(node, head):
    if node is None:
        return head

    head = rearrange(node.nxt, head)

    # Handling some corner cases
    if head is None:
        return None

    # reaching list mid
    if node == head or head.nxt == node:
        node.nxt = None
        return None

    head_next = head.nxt
    head.nxt = node
    node.nxt = head_next
    return head_next


if __name__ == '__main__':
    h = create_linked_list([1, 2, 3, 4, 5, 6])
    print_ll(h)
    rearrange(h, h)
    print_ll(h)
