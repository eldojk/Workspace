"""
amzn, msft

http://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
"""
from Queue import Queue

from G4G.Problems.linked_list.flatten_ll import Node
from G4G.Problems.linked_list.linked_list import create_linked_list


def flatten(head):
    q = Queue()
    t = None
    q.put(head)

    while not q.empty():
        if t:
            t.nxt = q.get()
            t = t.nxt

        else:
            t = q.get()

        # for each head in q,
        # scan horizontally
        while True:
            if t.down:
                q.put(t.down)

            if t.nxt:
                t = t.nxt

            else:
                break

    return head


if __name__ == '__main__':
    l1 = create_linked_list([10, 5, 12, 7, 11], Node)
    l2 = create_linked_list([4, 20, 13], Node)
    l3 = create_linked_list([17, 6], Node)

    l1.down = l2
    l1.nxt.nxt.nxt.down = l3

    l2.nxt.down = Node(2)
    l2.nxt.nxt.down = Node(16)
    l2.nxt.nxt.down.down = Node(3)

    l3.down = create_linked_list([9, 8], Node)
    l3.down.down = create_linked_list([19, 15], Node)

    h = flatten(l1)

    while h is not None:
        print h,
        h = h.nxt
