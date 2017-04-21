"""
amzn
"""

from G4G.Problems.stacks.stack import Stack


class Queue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def _move_elements(self, stack1, stack2):
        while stack1.peek() is not None:
            stack2.push(stack1.pop())

    def dequeue(self):
        self._move_elements(self.stack1, self.stack2)
        element = self.stack2.pop()
        self._move_elements(self.stack2, self.stack1)
        return element


"""
Awesome!!!
"""


class Queue2(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, element):
        self.stack1.push(element)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.peek()


"""
Using single stack
"""


class Queue3(object):

    def __init__(self):
        self.stack = Stack()
        self.element_to_pop = None
        self.element_to_peek = None

    def push(self, element):
        self.stack.push(element)

    def _pop(self):
        if not self.stack.is_empty():
            el = self.stack.pop()
            self._pop()

            if self.element_to_pop is None:
                self.element_to_pop = el
            else:
                self.stack.push(el)

    def _peek(self):
        if not self.stack.is_empty():
            el = self.stack.pop()
            self._pop()

            if self.element_to_pop is None:
                self.element_to_pop = el

            self.stack.push(el)

    def pop(self):
        self._pop()
        el = self.element_to_pop
        self.element_to_pop = None
        return el

    def peek(self):
        self._pop()
        el = self.element_to_pop
        self.element_to_peek = None
        return el


if __name__ == '__main__':
    q = Queue3()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.peek()
    print q.pop()
    print q.pop()













