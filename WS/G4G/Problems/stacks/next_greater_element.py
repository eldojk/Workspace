"""
amzn

http://www.geeksforgeeks.org/next-greater-element/
"""

from G4G.Problems.stacks.stack import Stack

def get_nge(array):
    s = Stack()

    for element in array:
        if s.is_empty():
            s.push(element)
        else:
            while not s.is_empty() and s.peek() < element:
                top = s.pop()
                print top, element
            else:
                s.push(element)

    if not s.is_empty():
        while not s.is_empty():
            print s.pop(), -1

get_nge([4, 5, 2, 25])