"""
amzn

http://www.geeksforgeeks.org/find-all-possible-outcomes-of-a-given-expression/

The idea is to iterate through every operator in given expression. For every operator, evaluate all
possible values of its left and right sides.
Apply current operator on every pair of left side and right side values and add all
evaluated values to the result.
"""


def evaluate(a, op, b):
    if op == '*':
        return a * b

    elif op == '+':
        return a + b

    elif op == '/':
        return a // b

    elif op == '-':
        return a - b

    else:
        return a % b


def evaluate_expression(exp, lo, hi):
    if lo > hi:
        return []

    if lo == hi:
        return [int(exp[lo])]

    if lo == hi - 2:
        return [evaluate(int(exp[lo]), exp[lo + 1], int(exp[lo + 2]))]

    res = []
    for i in range(lo, hi + 1):

        if exp[i] in ['*', '+', '-', '%', '/']:

            left_vals = evaluate_expression(exp, lo, i - 1)
            right_vals = evaluate_expression(exp, i + 1, hi)
            op = exp[i]

            for a in left_vals:
                for b in right_vals:
                    res.append(evaluate(a, op, b))

    return res


if __name__ == '__main__':
    print evaluate_expression('1*2+3*4', 0, 6)
