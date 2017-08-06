"""
amzn

http://www.geeksforgeeks.org/next-greater-element/

Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in array.
Elements for which no greater element exist, consider next greater element as -1.
"""

from G4G.Problems.stacks.stack import Stack


def nge(array):
    s = Stack()

    for num in array:
        while not s.is_empty() and s.peek() < num:
            print s.pop(), '-', num

        s.push(num)

    while not s.is_empty():
        print s.pop(), '-', -1


if __name__ == '__main__':
    nge([11, 13, 21, 3])
    nge([4, 5, 2, 25])

