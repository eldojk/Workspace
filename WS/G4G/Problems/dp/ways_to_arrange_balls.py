# coding=utf-8
"""
http://www.geeksforgeeks.org/ways-to-arrange-balls-such-that-adjacent-balls-are-of-different-types/

There are ‘p’ balls of type P, ‘q’ balls of type Q and ‘r’ balls of type R. Using the balls we want to create a straight
 line such that no two balls of same type are adjacent.

Examples :

Input  : p = 1, q = 1, r = 0
Output : 2
There are only two arrangements PQ and QP

Input  : p = 1, q = 1, r = 1
Output : 6
There are only six arrangements PQR, QPR,
QRP, RQP, PRQ and RPQ

Input  : p = 2, q = 1, r = 1
Output : 6
There are only six arrangements PQRP, QPRP,
PRQP, RPQP, PRPQ and PQPR

Base case
If last ball required is of type P and the number
of balls of P type is 1 while number of balls of
other color is 0 the number of ways is 1.
^ similar for Q and R

If u use P now, only Q and R can be used next
"""

DP = None


def count_ways_balls(p, q, r, last):
    global DP

    # can't make this arrangement
    if p < 0 or q < 0 or r < 0:
        return 0

    # If last ball required is of type P and the number
    # of balls of P type is 1 while number of balls of
    # other color is 0 the number of ways is 1.
    if p == 1 and q == 0 and r == 0 and last == 0:
        return 1

    if p == 0 and q == 1 and r == 0 and last == 1:
        return 1

    if p == 0 and q == 0 and r == 1 and last == 2:
        return 1

    if DP[p][q][r][last] != -1:
        return DP[p][q][r][last]

    if last == 0:
        DP[p][q][r][last] = count_ways_balls(p - 1, q, r, 1) + count_ways_balls(p - 1, q, r, 2)

    elif last == 1:
        DP[p][q][r][last] = count_ways_balls(p, q - 1, r, 0) + count_ways_balls(p, q - 1, r, 2)

    else:
        DP[p][q][r][last] = count_ways_balls(p, q, r - 1, 0) + count_ways_balls(p, q, r - 1, 1)

    return DP[p][q][r][last]


def count_ways(p, q, r):
    global DP
    DP = [[[[-1 for last in (0, 1, 2)] for _r in range(r + 1)] for _q in range(q + 1)] for _p in range(p + 1)]

    # last being 1, 2 and 3
    return count_ways_balls(p, q, r, 0) + count_ways_balls(p, q, r, 1) + count_ways_balls(p, q, r, 2)


if __name__ == '__main__':
    print count_ways(1, 1, 1)
