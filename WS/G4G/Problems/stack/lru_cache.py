"""
amzn, msft

http://www.geeksforgeeks.org/implement-lru-cache/
"""

from G4G.Problems.linked_list.linked_list import DNode


class Cache(object):
    def __init__(self, max_count):
        self.first_page = None
        self.last_page = None
        self.node_count = 0
        self.max_count = max_count
        self.hash = {}

    def push(self, key, node):
        if self.first_page is None:
            self.first_page = node
            self.last_page = self.first_page
            self.node_count += 1
        else:
            node.nxt = self.first_page
            self.first_page = node
            self.node_count += 1

            if self.node_count > self.max_count:
                last = self.last_page
                last.prev = None
                self.last_page = self.last_page.prev
                self.last_page.nxt = None
                del self.hash[key]

    def put(self, key):
        node = DNode(key)
        self.hash[key] = node
        self.push(key, node)

    def get(self, key):
        value = self.hash.get(key)

        if value:
            return value
        else:
            self.put(key)
            return self.hash[key]

