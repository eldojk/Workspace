# coding=utf-8
"""
amzn

(more done down)

Check for balanced parentheses in an expression
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]”
are correct in exp. For example, the program should print true for exp = “[()]{}{[()()]()}” and false for exp = “[(])”

Use stack, the one opened last should be closed first (brackets)
"""


def is_balanced(string):
    complements = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    opening_brackets = complements.keys()

    stack = []
    for st in string:
        if st in opening_brackets:
            stack.append(st)
        else:
            if len(stack) > 0:
                # closing bracket found
                open_st = stack.pop()
                if complements[open_st] != st:
                    return False
            else:
                return False

    # Stack should be empty by now
    return len(stack) == 0


if __name__ == '__main__':
    print is_balanced('[()]{}{[()()]()}')


"""
Without using stack
https://stackoverflow.com/questions/18482654/to-check-if-parenthesis-are-balanced-without-stack

only one bracket being checked '('
"""


def is_balanced_wo_stack(expression):
    balance = 0

    for s in expression:
        if s == '(':
            balance += 1

        elif s == ')':
            balance -= 1

            if balance < 0:
                # found a closing bracket before an opening one
                return False

    # balance has to be zero after all is done
    return balance == 0


if __name__ == '__main__':
    print ''
    print 'without stack'
    print is_balanced_wo_stack('((())())')
    print is_balanced_wo_stack('(())))()')
