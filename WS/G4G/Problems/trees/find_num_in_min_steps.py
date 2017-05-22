# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/find-a-number-in-minimum-steps/
http://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/

Given an infinite number line from -INFINITY to +INFINITY and we are on zero. We can move n steps either side at each
n’th time.

1st time; we can move only 1 step to both ways, means -1 1;

2nd time we can move 2 steps  from -1 and 1;
-1 :  -3 (-1-2)  1(-1+2)
 1 :  -1 ( 1-2)  3(1+2)

3rd time we can move 3 steps either way from -3, 1, -1, 3
-3:  -6(-3-3) 0(-3+3)
1:   -2(1-3)   4(1+3)
-1:  -4(-1-3)  2(-1+3)
3:     0(0-3)   6(3+3)

Find the minimum number of steps to reach a given number n.

This problem can be modeled as tree. We put initial point 0 at root, 1 and -1 as children of root. Next level contains
values at distance 2 and so on.

              0
            /   \
         -1       1
        /  \     /  \
       1   -3   -1   3
     /  \  / \  / \  / \
The problem is now to find the closes node to root with value n. The idea is to do Level Order Traversal of tree to find
the closest node.
"""
from Queue import Queue


def find_num(n):
    q = Queue()
    q.put((0, 1))

    while not q.empty():
        num = q.get()

        if num[0] == n:
            print num[1] - 1
            break

        q.put((num[0] + num[1], num[1] + 1))
        q.put((num[0] - num[1], num[1] + 1))


if __name__ == '__main__':
    find_num(13)