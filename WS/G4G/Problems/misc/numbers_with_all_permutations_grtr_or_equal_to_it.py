"""
http://www.geeksforgeeks.org/count-natural-numbers-whose-permutation-greater-number/

A simple solution is to run a loop from 1 to n and for every number check if
its digits are in non-decreasing order or not.

An efficient solution is based on below observations.

Observation 1: From 1 to 9, all number have this property. So, for n <= 9, output n.
Observation 2: The number whose all permutation is greater than or equal
to that number have all their digits in increasing order.

The idea is to push all the number from 1 to 9. Now, pop the top element, say topel
and try to make number whose digits are in increasing order and the first digit is topel.
To make such numbers, the second digit can be from topel%10 to 9. If this number is less than n,
increment the count and push the number in the stack, else ignore.
"""
from G4G.Problems.stacks.stack import Stack


def print_num(n):
    s = Stack()
    num = 0

    for i in range(1, 10):

        if i <= n:
            s.push(i)
            num += 1

        while not s.is_empty():
            tp = s.pop()
            j = tp % 10

            while j <= 9:
                x = tp * 10 + j

                if x <= n:
                    s.push(x)
                    num += 1

                j += 1
    return num


if __name__ == '__main__':
    print print_num(15)
