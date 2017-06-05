"""
http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

    def set_next(self, node):
        self.nxt = node

    def __repr__(self):
        return str(self.data)


def get_number_from_list(head):
    if head is None:
        return 0, 1

    carry, multiplier = get_number_from_list(head.nxt)
    num = carry + (multiplier * head.data)
    return num, multiplier*10


def get_number_from_rev_list(head):
    num = 0
    multiplier = 1

    while head is not None:
        num += (multiplier * head.data)
        multiplier *= 10
        head = head.nxt

    return num


if __name__ == '__main__':
    print get_number_from_rev_list(create_linked_list([1, 2, 3]))
    print get_number_from_list(create_linked_list([1, 2, 3]))[0]


"""
amzn

add num to ll or add 1 to ll
"""

def _add_num_to_linked_list(head, num):
    if head is not None:
        carry = _add_num_to_linked_list(head.nxt, num)

        op_sum = head.data + carry
        new_data = op_sum
        new_carry = 0

        if op_sum >= 10:
            new_data %= 10
            new_carry = op_sum // 10

        head.data = new_data
        return new_carry
    else:
        return num


def add_num_to_linked_list(head, num):
    carry = _add_num_to_linked_list(head, num)

    if carry > 0:
        h = Node(carry)
        h.nxt = head
        return h

    return head


if __name__ == '__main__':
    print ''
    h = create_linked_list([3, 2, 1])
    h = add_num_to_linked_list(h, 1211)
    print_ll(h)