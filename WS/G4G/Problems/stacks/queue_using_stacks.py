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
