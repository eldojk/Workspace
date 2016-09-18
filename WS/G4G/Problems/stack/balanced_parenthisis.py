# coding=utf-8
"""
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

# print is_balanced('[()]{}{[()()]()}')
