"""
amzn

http://www.geeksforgeeks.org/the-stock-span-problem/
"""
from G4G.Problems.stacks.stack import Stack


def calculate_span(stocks):
    spans = [-1 for i in stocks]
    s = Stack()
    s.push(0)
    spans[0] = 1

    for i in range(1, len(stocks)):
        # pop until we find a taller element in stack
        while not s.is_empty() and stocks[s.peek()] <= stocks[i]:
            s.pop()

        # now that stack has a taller element
        if s.is_empty():
            # we popped everything, that means i is highest and its span is i + 1
            spans[i] = i + 1
        else:
            # or difference between the higher one and i
            spans[i] = i - s.peek()

        s.push(i)

    return spans


if __name__ == '__main__':
    print calculate_span([10, 4, 5, 90, 120, 80])
