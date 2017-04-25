"""
amzn

http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

check to find explanation: https://www.youtube.com/watch?v=39grPZtywyQ
"""


class DeQueue(object):
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def front(self):
        return self.array[0]

    def rear(self):
        return self.array[-1]

    def pop_front(self):
        return self.array.pop(0)

    def pop_rear(self):
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0


def print_maximums(array, k):
    q = DeQueue()

    for i in range(k):
        while not q.is_empty() and array[q.rear()] <= array[i]:
            q.pop_rear()

        q.push(i)

    for i in range(k, len(array)):
        print array[q.front()],

        while not q.is_empty() and i - q.front() >= k:
            q.pop_front()

        while not q.is_empty() and array[q.rear()] <= array[i]:
            q.pop_rear()

        q.push(i)

    print array[q.front()]


if __name__ == '__main__':
    print_maximums([12, 1, 78, 90, 57, 89, 56], 3)

