"""
Check if ll is palindrome using:
Stack, push elements to stack till mid, after that pop each element and compare (mid finding by first getting n or
using first and slow runners : ref CITC 197)
todo
"""
from  G4G.Problems.linked_list.linked_list import create_linked_list


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


"""
amzn
"""


def is_palindrome_2(node, complementary_node):
    isPal = True
    if node.nxt:
        isPal, complementary_node = is_palindrome_2(node.nxt, complementary_node)

    if isPal and node.data == complementary_node.data:
        return True, complementary_node.nxt

    return False, complementary_node.nxt


if __name__ == '__main__':
    l = create_linked_list([1, 2, 2, 3, 4, 4, 2, 2, 1])
    print is_palindrome_2(l, l)