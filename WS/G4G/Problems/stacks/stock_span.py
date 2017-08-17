"""
amzn

http://www.geeksforgeeks.org/the-stock-span-problem/
"""
from G4G.Problems.stacks.stack import Stack


def calculate_span(stocks):
    spans = [-1 for i in stocks]
    s = Stack()
    s.push(-1)
    spans[0] = 1

    for i in range(len(stocks)):
        # pop until we find a taller element in stack
        while s.peek() != -1 and stocks[s.peek()] <= stocks[i]:
            s.pop()

        # calculate span
        spans[i] = i - s.peek()

        s.push(i)

    return spans


if __name__ == '__main__':
    print calculate_span([10, 4, 5, 90, 120, 80])
