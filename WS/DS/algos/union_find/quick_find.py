"""
Quick Find approach

Idea: If p and q are connected, then array[p] and array[q] are equal
"""


class QuickFind(object):
    def __init__(self, num):
        self.array = range(num)

    def find(self, p, q):
        return self.array[p] == self.array[q]

    def union(self, p, q):
        """
        We set all elements with value of array[p] to the
        value of array[q]

        :param p:
        :param q:
        :return:
        """
        q_value = self.array[q]

        for num in self.array:
            if num == self.array[p]:
                self.array[p] = q_value
