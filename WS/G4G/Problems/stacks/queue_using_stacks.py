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
