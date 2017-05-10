"""
amzn

CHECK THESE TWO PROBLEMS. ALL 3 SOLUTIONS ARE AWESOME
http://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/
http://www.geeksforgeeks.org/clone-linked-list-next-arbit-pointer-set-2/

You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link
list. The second pointer however CAN point to any node in the list and not just the previous node

"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


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


"""
Without extra space

amzn

1) Create the copy of node 1 and insert it between node 1 & node 2 in original Linked List, create the copy of 2 and
insert it between 2 & 3.. Continue in this fashion, add the copy of N afte the Nth node
2) Now copy the arbitrary link in this fashion

     original->next->arbitrary = original->arbitrary->next;  /*TRAVERSE TWO NODES*/
This works because original->next is nothing but copy of original and Original->arbitrary->next is nothing but copy of
arbitrary.
3) Now restore the original and copy linked lists in this fashion in a single loop.

     original->next = original->next->next;
     copy->next = copy->next->next;
4) Make sure that last element of original->next is NULL.
"""


def clone_without_extra_space(start):
    node = start
    cl_start = None

    while node is not None:
        clone_node = Node(node.data)

        if cl_start is None:
            cl_start = clone_node

        next_node = node.nxt
        clone_node.nxt = next_node
        node.nxt = clone_node

        node = next_node

    flag = True
    node = start

    # traverse 2 nodes at a time
    while node is not None:
        if flag:
            node.nxt.other = node.other.nxt

        flag = not flag
        node = node.nxt

    node = start

    while node is not None:
        clone_node = node.nxt
        node.nxt = node.nxt.nxt

        if clone_node.nxt:
            clone_node.nxt = clone_node.nxt.nxt

        node = node.nxt

    return cl_start


if __name__ == '__main__':
    # with extra space
    ll1 = create_linked_list([1, 2, 3, 4], node=Node)
    ll1.other = ll1.nxt.nxt
    ll1.nxt.other = ll1.nxt.nxt.nxt
    ll1.nxt.nxt.other = ll1
    ll1.nxt.nxt.nxt.other = ll1.nxt
    print_ll(ll1)
    ll2 = clone_without_extra_space(ll1)
    print_ll(ll2)
    print ll2.other
    print ll2.nxt.other
    print ll2.nxt.nxt.other
    print ll2.nxt.nxt.nxt.other

    print ''

    # without extra space
    ll1 = create_linked_list([1, 2, 3, 4], node=Node)
    ll1.other = ll1.nxt.nxt
    ll1.nxt.other = ll1.nxt.nxt.nxt
    ll1.nxt.nxt.other = ll1
    ll1.nxt.nxt.nxt.other = ll1.nxt
    print_ll(ll1)
    ll2 = clone_without_extra_space(ll1)
    print_ll(ll2)
    print ll2.other
    print ll2.nxt.other
    print ll2.nxt.nxt.other
    print ll2.nxt.nxt.nxt.other
