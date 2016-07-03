"""
Quick Union approach

Idea: The value of array[p] would contain the parent of p
p and q are connected if both of them have the same root,
i.e. both are on the same tree.
"""


class QuickUnion(object):
    def __init__(self, num):
        self.array = range(num)

    def _find_root(self, x):
        while self.array[x] != x:
            x = self.array[x]

        return x

    def find(self, p, q):
        return self._find_root(p) == self._find_root(q)

    def union(self, p, q):
        """
        We set the value of p's root to the value of q's root

        :param p:
        :param q:
        :return:
        """
        q_root = self._find_root(q)
        p_root = self._find_root(p)

        self.array[p_root] = q_root