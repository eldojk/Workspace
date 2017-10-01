"""
amzn

http://www.geeksforgeeks.org/implement-a-stack-using-single-queue/
"""

from Queue import Queue


class Stack(object):

    def __init__(self):
        self.q = Queue()

    def push(self, element):
        if self.q.empty():
            self.q.put(element)
        else:
            s = self.q.qsize()
            self.q.put(element)

            # pop from front and put it at the back
            for i in range(s):
                self.q.put(self.q.get())

    def pop(self):
        return self.q.get()


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print s.pop(), s.pop(), s.pop()
