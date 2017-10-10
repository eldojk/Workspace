"""
amzn, msft

more down

Check if ll is palindrome using:
Stack, push elements to stack till mid, after that pop each element and compare (mid finding by first getting n or
using first and slow runners : ref CITC 197)
todo

http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll
from G4G.Problems.stack.stack import Stack


def is_palindrome(node):
    if node is None or node.nxt is None:
        return True

    s = Stack()
    a = b = node
    s.push(b)
    l = 1

    while a is not None and a.nxt is not None:
        a = a.nxt
        l += 1

        b = b.nxt
        s.push(b)

        a = a.nxt

        if a:
            l += 1

    s.pop()

    if l % 2 != 0:
        b = b.nxt

    while b is not None:
        if b.data != s.pop().data:
            return False

        b = b.nxt

    return True


if __name__ == '__main__':
    l = create_linked_list([1, 2, 2, 4, 4, 2, 2, 1])
    print is_palindrome(l)

    l = create_linked_list([1, 2, 2, 3, 4, 4, 2, 2, 1])
    print is_palindrome(l)

    l = create_linked_list([1, 2, 2, 4, 2, 2, 1])
    print is_palindrome(l)

    l = create_linked_list([1, 2, 1])
    print is_palindrome(l)

    l = create_linked_list([1, 1])
    print is_palindrome(l)


"""
amzn, msft

http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
"""


def is_palindrome_2(node, complementary_node):
    isPal = True
    if node.nxt:
        isPal, complementary_node = is_palindrome_2(node.nxt, complementary_node)

    if isPal and node.data == complementary_node.data:
        return True, complementary_node.nxt

    return False, complementary_node.nxt


if __name__ == '__main__':
    print ''
    print 'is pal recursive'
    l = create_linked_list([1, 2, 2, 3, 4, 4, 2, 2, 1])
    print is_palindrome_2(l, l)


"""
Without extra space. using reversal
"""


def reverse_at_mid(head):
    node = head
    next_node = head.nxt
    node.nxt = None

    while next_node is not None:
        next_next = next_node.nxt
        next_node.nxt = node
        node = next_node
        next_node = next_next

    return node


def get_mid(head):
    fp = sp = head

    while fp is not None:

        if fp.nxt:
            fp = fp.nxt

        else:
            break

        if fp.nxt:
            fp = fp.nxt

        else:
            break

        sp = sp.nxt

    sp = sp.nxt
    return sp


def is_pal_sans_extra_space(head):
    if head.nxt is None:
        return True

    curr = head
    mid = get_mid(head)
    mid = reverse_at_mid(mid)

    while mid is not None:
        if mid.data != curr.data:
            return False

        mid = mid.nxt
        curr = curr.nxt

    return True


if __name__ == '__main__':
    print ''
    print 'wo extra space'
    h = create_linked_list([1, 2, 3, 3, 2, 1])
    print is_pal_sans_extra_space(h)

    h = create_linked_list([1, 2, 3, 2, 1])
    print is_pal_sans_extra_space(h)

    h = create_linked_list([1, 2, 3, 4, 2, 1])
    print is_pal_sans_extra_space(h)

    h = create_linked_list([1, 2, 3, 4, 1])
    print is_pal_sans_extra_space(h)

    h = create_linked_list([1, 1])
    print is_pal_sans_extra_space(h)
