"""
Priority Queue

TODO:
1. Handle underflow error
2. Write tests
3. NEED A MUCH BETTER IMPLEMENTATION. Separate Priority queue implementation from binary heap implementation
"""


class Node(object):
    def __init__(self, priority):
        self.priority = priority


class PriorityQueue(object):
    def __init__(self):
        self.array = [None]

    def insert(self, node):
        """
        Insert at the end and swim upward till binary heap property is satisfied

        :param node:
        :return:
        """
        self.array.append(node)
        max_index = len(self.array) - 1
        self.swim(max_index)

    def pop_max(self):
        """
        Swap top with last,
        Remove the last,
        Sink the top until binary heap property is satisfied

        :return:
        """
        max_index = len(self.array) - 1
        self.exchange(1, max_index)
        max_element = self.array.pop()
        self.sink(1)
        return max_element

    def swim(self, n):
        """
        Exchange with parent until parent priority is not less

        :param n:
        :return:
        """
        while n // 2 >= 1:
            parent_key = n // 2
            if self.array[parent_key].priority < self.array[n].priority:
                self.exchange(parent_key, n)
                n = parent_key

    def sink(self, n):
        """
        Exchange with the bigger of children until both of children's priorities are not higher

        :param n:
        :return:
        """
        while self.get_child_bigger_than_self(n) is not None:
            big_child = self.get_child_bigger_than_self(n)
            self.exchange(n, big_child)
            n = big_child

    def exchange(self, m, n):
        self.array[m], self.array[n] = self.array[n], self.array[m]

    def get_child_bigger_than_self(self, n):
        # TODO : Refactor this
        l_index = None
        if 2 * n <= len(self.array):
            largest_child = self.array[2 * n]
            l_index = 2 * n

            if largest_child and l_index + 1 <= len(self.array):
                right_child = self.array[l_index + 1]
                l_index = l_index if largest_child.priority > right_child.priority else l_index + 1

        if l_index and (self.array[n].priority < self.array[l_index].priority):
            return l_index

        return None
