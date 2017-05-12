"""
amzn

http://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
Stack with min
"""
from sys import maxint


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        current_min = self.minimum()
        tup = (data, current_min if data > current_min else data)
        self.stack.append(tup)
        print self.stack

    def pop(self):
        return self.stack.pop()[0] if len(self.stack) > 0 else None

    def peek(self):
        return self.stack[-1][1]

    def minimum(self):
        if len(self.stack) == 0:
            return maxint

        return self.peek()

s = Stack()
s.push(5)
s.push(6)
s.push(3)
s.push(7)

print s.minimum()
s.pop()
print s.minimum()
s.pop()
print s.minimum()
s.pop()
print s.minimum()
s.pop()
print s.minimum()
