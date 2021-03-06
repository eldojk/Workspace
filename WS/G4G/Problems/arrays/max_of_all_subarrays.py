"""
amzn

#tricky
sliding window
http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
http://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/

check to find explanation: https://www.youtube.com/watch?v=39grPZtywyQ

We create a Dequeue, Qi of capacity k, that stores only useful elements of current window
of k elements. An element is useful if it is in current window and is greater than all
other elements on left side of it in current window. We process all array elements one
by one and maintain Qi to contain useful elements of current window and these useful
elements are maintained in sorted order. The element at front of the Qi is the largest
and element at rear of Qi is the smallest of current window.
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

    # store useful elements in queue for the first k elements
    for i in range(k):
        while not q.is_empty() and array[q.rear()] <= array[i]:
            q.pop_rear()

        q.push(i)

    for i in range(k, len(array)):
        print array[q.front()],

        # remove elements from front if sliding window grows to size
        # greater than k
        while not q.is_empty() and i - q.front() >= k:
            q.pop_front()

        # pop from back as an when we find greater elements since smaller
        # elements in the window are useless
        while not q.is_empty() and array[q.rear()] <= array[i]:
            q.pop_rear()

        q.push(i)

    print array[q.front()]


if __name__ == '__main__':
    print_maximums([12, 1, 78, 90, 57, 89, 56], 3)


"""
print minimums? keep minimum elements in DeQueue

to find max of all minimums, instead of printing keep track of it
http://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/
"""


def print_minimums(array, k):
    q = DeQueue()

    # store useful elements in queue for the first k elements
    for i in range(k):
        while not q.is_empty() and array[q.rear()] >= array[i]:
            q.pop_rear()

        q.push(i)

    for i in range(k, len(array)):
        print array[q.front()],

        # remove elements from front if sliding window grows to size
        # greater than k
        while not q.is_empty() and i - q.front() >= k:
            q.pop_front()

        # pop from back as an when we find smaller elements since greater
        # elements in the window are useless
        while not q.is_empty() and array[q.rear()] >= array[i]:
            q.pop_rear()

        q.push(i)

    print array[q.front()]


if __name__ == '__main__':
    print_minimums([12, 1, 78, 90, 57, 89, 56], 3)
