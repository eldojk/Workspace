"""
Check if ll is palindrome using:
Stack, push elements to stack till mid, after that pop each element and compare (mid finding by first getting n or
using first and slow runners : ref CITC 197)
todo
"""


def is_palindrome(node):
    if node.nxt is None or node.nxt.nxt is None:
        return node.data == node.nxt.data if node.nxt else True

    stack = []
    fast_pt = node
    slow_pt = node
    while fast_pt is not None and fast_pt.nxt is not None:
        stack.append(slow_pt.data)
        slow_pt = slow_pt.nxt
        fast_pt = fast_pt.nxt.nxt

    print stack
    while slow_pt is not None:
        if fast_pt:
            # Odd number of nodes
            slow_pt = slow_pt.nxt
            fast_pt = None

        pop = stack.pop()
        print pop, slow_pt
        if slow_pt.data == pop:
            slow_pt = slow_pt.nxt
        else:
            return False

    return True


# l = create_linked_list([1, 2, 2, 2])
# print is_palindrome(l)