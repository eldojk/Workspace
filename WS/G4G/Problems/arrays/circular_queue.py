"""
amzn

http://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
"""


class CircularQueue(object):
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]
        self.front = -1
        self.rear = -1

    def enqueue(self, element):
        if (self.front == 0 and self.rear == self.size - 1) or (self.rear == self.front - 1):
            print 'Queue is full'
            return

        # first element
        elif self.front == -1:
            self.front = self.rear = 0
            self.array[self.rear] = element

        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
            self.array[self.rear] = element

        else:
            self.rear += 1
            self.array[self.rear] = element

    def dequeue(self):
        if self.front == -1:
            print 'Empty queue'
            return None

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

    def print_queue(self):
        if self.front == -1:
            print 'Empty Queue'
            return

        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print self.array[i],

        else:
            for i in range(self.front, self.size):
                print self.array[i],

            for i in range(self.rear + 1):
                print self.array[i],

        print ''
