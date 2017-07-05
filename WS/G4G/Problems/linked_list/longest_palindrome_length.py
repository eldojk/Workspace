"""
msft

http://www.geeksforgeeks.org/length-longest-palindrome-list-linked-list-using-o1-extra-space/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def count_common_nodes(h1, h2):
    count = 0

    while h1 is not None and h2 is not None:
        if h1.data == h2.data:
            count += 1
            h1 = h1.nxt
            h2 = h2.nxt

        else:
            break

    return count


def longest_palindrome_length(head):
    result = 0
    prev = None
    curr = head

    while curr:
        nxt = curr.nxt
        curr.nxt = prev

        # check for odd length palindrome with
        # curr as middle
        result = max(
            result,
            2 * count_common_nodes(prev, nxt) + 1
        )

        # check for even length palindrome
        result = max(
            result,
            2 * count_common_nodes(curr, nxt)
        )

        prev = curr
        curr = nxt

    return result


if __name__ == '__main__':
    h = create_linked_list([2, 3, 7, 3, 2, 12, 24])
    print longest_palindrome_length(h)

    h = create_linked_list([12, 4, 4, 3, 14])
    print longest_palindrome_length(h)
