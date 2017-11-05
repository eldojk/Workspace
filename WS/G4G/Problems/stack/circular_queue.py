"""
amzn

http://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
"""


class CircularQueue(object):
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.array = [None for i in range(size)]

    def enqueue(self, num):
        if (self.front == 0 and self.rear == self.size - 1) or self.rear == self.front - 1:
            print 'Q full'
            return False

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.array[self.rear] = num
            return True

        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
            self.array[self.rear] = num
            return True

        else:
            self.rear += 1
            self.array[self.rear] = num
            return True

    def dequeue(self):
        if self.front == -1:
            print 'Q empty'
            return False

        data = self.array[self.front]
        self.array[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        elif self.front == self.size - 1:
            self.front = 0

        else:
            self.front += 1

        return data
