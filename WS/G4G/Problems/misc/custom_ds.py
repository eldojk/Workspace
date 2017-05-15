"""
amzn

http://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/
"""
from random import randint


class DS(object):

    def __init__(self):
        self.hash = {}
        self.list = []

    def lookup(self, val):
        idx = self.hash.get(val)

        return self.list[idx] if idx is not None else None

    def insert(self, val):
        if self.lookup(val) is None:
            self.hash[val] = len(self.list)
            self.list.append(val)

    def remove(self, val):
        idx = self.lookup(val)

        if idx is not None:
            n = len(self.list) - 1
            n_val = self.list[n]

            self.hash[n_val] = idx
            self.list[idx] = n_val

            self.hash.pop(val)
            self.list.pop()

    def random(self):
        return self.list[randint(0, len(self.list) - 1)]
