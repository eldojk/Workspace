"""
amzn, msft

http://www.geeksforgeeks.org/flattening-a-linked-list/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.down = None

    def  __repr__(self):
        return str(self.data)


def merge_list(head1, head2):
    if head1.data < head2.data:
        h = head1
        head1 = head1.down
    else:
        h = head2
        head2 = head2.down

    tail = h

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            tail.down = head1
            head1 = head1.down
            tail = tail.down
        else:
            tail.down = head2
            head2 = head2.down
            tail = tail.down

    while head1 is not None:
        tail.down = head1
        head1 = head1.down
        tail = tail.down

    while head2 is not None:
        tail.down = head2
        head2 = head2.down
        tail = tail.down

    return h


def flatten_list(head):
    l1 = head
    l2 = head.nxt

    while l2 is not None:
        l1 = merge_list(l1, l2)
        l2 = l2.nxt

    return l1


if __name__ == '__main__':
    l1 = Node(5)
    l1.down = Node(7)
    l1.down.down = Node(8)
    l1.down.down.down = Node(30)

    l2 = Node(10)
    l2.down = Node(20)

    l1.nxt = l2

    l3 = Node(19)
    l3.down = Node(22)
    l3.down.down = Node(50)

    l2.nxt = l3

    l4 = Node(28)
    l4.down = Node(35)
    l4.down.down = Node(40)
    l4.down.down.down = Node(45)

    l3.nxt = l4

    h = flatten_list(l1)

    while h.down is not None:
        print h,
        h = h.down



