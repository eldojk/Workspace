"""
amzn, msft

http://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
"""
from G4G.Problems.stack.stack import Stack


def is_operator(ch):
    return ch in ['+', '-', '/', '*', '%']


def evaluate(exp):
    s = Stack()

    i = 0
    while i < len(exp):
        if not is_operator(exp[i]):
            s.push(int(exp[i]))

        else:
            val1 = s.pop()
            val2 = s.pop()

            if exp[i] == '+':
                s.push(val1 + val2)

            elif exp[i] == '-':
                s.push(val2 - val1)

            elif exp[i] == '*':
                s.push(val1 * val2)

            elif exp[i] == '/':
                s.push(val2 / val1)

            else:
                s.push(val2 % val1)

    return s.pop()