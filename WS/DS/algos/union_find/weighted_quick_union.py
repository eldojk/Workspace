"""
Weighted Quick Union approach

Idea: The value of array[p] would contain the parent of p
p and q are connected if both of them have the same root,
i.e. both are on the same tree.

Unfortunately these trees can bee really tall, so we can do
one more optimization. While doing union(p, q), if we always
make sure to set the smaller as the child of the larger tree,
the tree size is at max the size of the larger tree :)
"""


class WeightedQuickUnion(object):
    def __init__(self, num):
        self.array = range(num)
        self.size_array = [1 for x in range(num)]

    def _find_root(self, x):
        while self.array[x] != x:
            # self.array[x] = self.array[array[x]] - This is path compression
            x = self.array[x]

        return x

    def size(self, x):
        """
        Find size of tree containing x

        :param x:
        :return:
        """
        x_root = self._find_root(x)
        return self.size_array[x_root]

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

        q_size = self.size(q)
        p_size = self.size(p)

        if q_size >= p_size:
            self.array[p_root] = q_root
            self.size_array[q_root] = p_size + q_size
        else:
            self.array[q_root] = p_root
            self.size_array[p_root] = p_size + q_size
