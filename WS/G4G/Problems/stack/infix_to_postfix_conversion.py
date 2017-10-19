"""
amzn

#tricky
http://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
"""
from G4G.Problems.stack.stack import Stack

CAPS_RANGE = range(ord('A'), ord('Z') + 1)
SMALL_RANGE = range(ord('a'), ord('z') + 1)


def is_operand(op):
    global CAPS_RANGE, SMALL_RANGE
    return ord(op) in CAPS_RANGE or ord(op) in SMALL_RANGE


def precedence(ch):
    if ch == '+' or ch == '-':
        return 1

    elif ch == '*' or ch == '/':
        return 2

    elif ch == '^':
        return 3

    else:
        return -1


def convert(exp):
    k = -1
    exp = list(exp)

    s = Stack()

    for i in range(len(exp)):

        if is_operand(exp[i]):
            k += 1
            exp[k] = exp[i]

        elif exp[i] == '(':
            s.push(exp[i])

        elif exp[i] == ')':
            while not s.is_empty() and s.peek() != '(':
                k += 1
                exp[k] = s.pop()

            if not s.is_empty() and s.peek() != '(':
                return -1

            else:
                s.pop()  # pop off the '('

        else:
            while not s.is_empty() and precedence(exp[i]) <= precedence(s.peek()):
                k += 1
                exp[k] = s.pop()

            s.push(exp[i])

    while not s.is_empty():
        k += 1
        exp[k] = s.pop()

    return ''.join(exp)[0: k + 1]


if __name__ == '__main__':
    print convert('a+b*(c^d-e)^(f+g*h)-i')
