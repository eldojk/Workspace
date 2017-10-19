# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/amazon-interview-experience-set-333-internship/

You have been given a generator string ab from which any number of strings can be generated
recursively by inserting ‘ab’ at any location. You have been given an input string to check
if that given string is valid or not.
(i.e. generated by given with given string.)

eg.
Input: aabbab
Output: valid
Input: abbaab
output: Invalid
"""
from G4G.Problems.stack.stack import Stack


def is_valid(string):
    s = Stack()
    for c in string:
        if c == 'a':
            s.push(c)
        elif c == 'b' and not s.is_empty():
            s.pop()
        else:
            return False

    return s.is_empty()


if __name__ == '__main__':
    print is_valid('aabbab')
    print is_valid('abbaab')
