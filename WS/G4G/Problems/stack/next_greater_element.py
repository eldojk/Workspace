"""
amzn

http://www.geeksforgeeks.org/next-greater-element/

Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in array.
Elements for which no greater element exist, consider next greater element as -1.
"""

from G4G.Problems.stacks.stack import Stack

def next_greater_element(array):
    s = Stack()
    s.push(array[0])

    for i in range(1, len(array)):
        element = s.pop()
        nxt = array[i]

        while element < nxt:
            print "{0} - {1}".format(str(element), str(nxt))

            if s.is_empty():
                break

            element = s.pop()

        if element >= nxt:
            s.push(element)

        s.push(nxt)

    while not s.is_empty():
        print "{0} - {1}".format(str(s.pop()), '-1')


print next_greater_element([11, 13, 21, 3])
print next_greater_element([4, 5, 2, 25])