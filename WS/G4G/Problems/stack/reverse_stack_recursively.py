"""
amzn

http://www.geeksforgeeks.org/reverse-a-stack-using-recursion/
"""
from G4G.Problems.stack.stack import Stack


def insert_at_bottom(stack, element):
    if stack.is_empty():
        stack.push(element)

    else:
        el = stack.pop()
        insert_at_bottom(stack, element)
        stack.push(el)


def reverse_stack(stack):
    if not stack.is_empty():
        el = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, el)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    reverse_stack(s)

    while not s.is_empty():
        print s.pop(),