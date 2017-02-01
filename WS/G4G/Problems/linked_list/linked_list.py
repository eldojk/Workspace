class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

    def set_next(self, node):
        self.nxt = node

    def __repr__(self):
        return str(self.data)


class DNode(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.prev = None

    def set_next(self, node):
        self.nxt = node

    def __repr__(self):
        return str(self.data)


def create_linked_list(array, node=Node):
    ll = [node(data) for data in array]

    for i in range(len(array) - 1):
        ll[i].nxt = ll[i + 1]

    return ll[0]


def create_doubly_linked_list(array):
    ll = [DNode(data) for data in array]

    for i in range(len(array) - 1):
        ll[i].nxt = ll[i + 1]

    for j in range(1, len(array)):
        ll[i].prev = ll[i-1]

    return ll[0]


def get_node(node, n):
    while n > 0:
        node = node.nxt
        n -= 1

    return node


def print_ll(node):
    datas = []
    while True:
        datas.append(node.data)
        node = node.nxt

        if node is None:
            break

    print " -> ".join(map(str, datas))
