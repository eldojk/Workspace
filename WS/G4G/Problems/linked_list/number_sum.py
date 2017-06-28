"""
LL represent number in reverse order. add two numbers represented by two lls and give new ll
"""
from linked_list import Node
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def get_number(node):
    digit = 1
    val = 0

    while node is not None:
        val += node.data * digit
        digit *= 10
        node = node.nxt

    return val


def create_ll_from_num(num):
    prev = None
    start = None
    while num > 0:
        digit = num % 10
        node = Node(digit)

        if start is None:
            start = node

        if prev:
            prev.nxt = node

        prev = node
        num = (num - digit) / 10

    return start


def sum_ll(node1, node2):
    n1 = get_number(node1)
    n2 = get_number(node2)

    num = n1 + n2

    return create_ll_from_num(num)

# l1 = create_linked_list([1, 2, 3, 4])
# l2 = create_linked_list([1, 2, 3, 4])
# print_ll(sum_ll(l1, l2))


"""
amzn msft

http://www.geeksforgeeks.org/sum-of-two-linked-lists/
http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
"""


def count_nodes(head):
    cnt = 0

    while head:
        cnt += 1
        head = head.nxt

    return cnt


def add_eq_len_lls(h1, h2):
    if h1 is None:
        return 0

    carry = add_eq_len_lls(h1.nxt, h2.nxt)
    sm = carry + h1.data + h2.data

    if sm >= 10:
        sm %= 10
        carry = 1
    else:
        carry = 0

    h1.data = sm
    return carry


def append_zeros(head, n):
    h = None
    t = None

    while n > 0:
        if t is None:
            t = Node(0)
            h = t
            n -= 1
            continue

        t.nxt = Node(0)
        n -= 1
        t = t.nxt

    if t is None:
        return head

    t.nxt = head
    return h


def add_lls(h1, h2):
    c1 = count_nodes(h1)
    c2 = count_nodes(h2)

    ll = h1 if c1 >= c2 else h2
    sl = h1 if ll == h2 else h2

    sl = append_zeros(sl, abs(c1 - c2))

    carry = add_eq_len_lls(ll, sl)

    if carry > 0:
        head = Node(carry)
        head.nxt = h1
        return head

    return h1


if __name__ == '__main__':
    l1 = create_linked_list([5, 6, 3])
    l2 = create_linked_list([8, 4, 2])

    _sum_list = add_lls(l1, l2)

    print_ll(_sum_list)