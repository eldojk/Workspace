from sys import maxint
# 1 2 3
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def reverse(head, prev):
    if head is None:
        return prev, head

    # 9, 8 - 8, 7
    a, b = reverse(head.nxt, head)

    if b is None:
        return head, head

    b.nxt = head
    return a, head


if __name__ == '__main__':
    h = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    rl, rt = reverse(h, None)
    rt.nxt = None
    print_ll(rl)
