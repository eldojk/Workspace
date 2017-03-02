"""
http://www.geeksforgeeks.org/find-expression-duplicate-parenthesis-not/
"""
from G4G.Problems.stacks.stack import Stack


def is_exp(s):
    return '+' in s


def dupe_found(string):
    s = Stack()
    for c in string:
        exp = ""
        if c != ')':
            s.push(c)
        else:
            while not s.is_empty() and s.peek() != '(':
                char = s.pop()
                exp += char

            if not is_exp(exp):
                return True
            s.pop()

    return False


print dupe_found('((a+b)+((c+d)))')
print dupe_found('(((a+(b)))+(c+d))')
print dupe_found('(((a+(b))+c+d))')
print dupe_found('((a+b)+(c+d))')
