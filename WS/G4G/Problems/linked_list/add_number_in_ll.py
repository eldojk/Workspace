"""
http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list


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
        num = num + multiplier * head.data
        multiplier = multiplier * 10
        head = head.nxt

    return num


print get_number_from_rev_list(create_linked_list([1, 2, 3]))
print get_number_from_list(create_linked_list([1, 2, 3]))[0]