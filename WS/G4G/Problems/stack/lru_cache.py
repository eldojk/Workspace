"""
amzn, msft

http://www.geeksforgeeks.org/implement-lru-cache/
http://www.geeksforgeeks.org/lru-cache-implementation/
"""
from G4G.Problems.linked_list.linked_list import DNode, print_ll


class Cache(object):
    def __init__(self, max_count):
        self.first_page = None
        self.last_page = None
        self.node_count = 0
        self.max_count = max_count
        self.hash = {}

    def _remove_last_node(self):
        data = self.last_page.data
        del self.hash[data]
        self.last_page = self.last_page.prev
        self.last_page.nxt = None

    def _add_to_front(self, node):
        if self.first_page is None:
            self.first_page = node
            self.last_page = node
            return

        node.nxt = self.first_page
        self.first_page.prev = node
        self.first_page = node

    def _move_to_front(self, node):
        if node == self.first_page:
            return

        elif node == self.last_page:
            self.last_page = self.last_page.prev
            self.last_page.nxt = None
            node.prev = None

        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            node.prev = None
            node.nxt = None

        self._add_to_front(node)

    def put(self, key):
        if key in self.hash:
            node = self.hash[key]
            self._move_to_front(node)

        else:
            if self.node_count == self.max_count:
                self._remove_last_node()

            node = DNode(key)
            self.hash[key] = node
            self._add_to_front(node)
            self.node_count += 1

        print_ll(self.first_page)

    def get(self, key):
        node = self.hash.get(key)

        if node:
            self._move_to_front(node)
            print_ll(self.first_page)
            return node.data

        if self.first_page:
            print_ll(self.first_page)
        return None


if __name__ == '__main__':
    c = Cache(5)
    print c.get(1)
    c.put(1)
    c.put(2)
    c.put(3)
    c.put(4)
    c.put(5)
    print c.get(2)
    print c.get(4)
    c.put(6)