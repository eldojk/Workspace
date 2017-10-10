"""

"""
from Queue import Queue


def reverse(queue):
    if queue.empty():
        return queue

    el = queue.get()
    queue = reverse(queue)
    queue.put(el)

    return queue


if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    q = reverse(q)

    print q.get(), q.get(), q.get()
