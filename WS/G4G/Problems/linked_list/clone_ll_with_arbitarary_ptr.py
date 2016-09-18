"""
http://www.geeksforgeeks.org/clone-linked-list-next-arbit-pointer-set-2/
You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link
list. The second pointer however CAN point to any node in the list and not just the previous node

"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.other = None

    def __repr__(self):
        return str(self.data)


def clone_ll(start):
    dict = {}
    node = start
    dict[node] = Node(node.data)

    while node.nxt:
        node = node.nxt
        dict[node] = Node(node.data)

    for nd in dict.keys():
        if nd.nxt:
            dict[nd].nxt = dict[nd.nxt]

        if nd.other:
            dict[nd].other = dict[nd.other]

    return dict[start]


# ll1 = create_linked_list([1, 2, 3, 4], node=Node)
# ll1.other = ll1.nxt.nxt
# print_ll(ll1)
# ll2 = clone_ll(ll1)
# print_ll(ll2)
# print ll2.other