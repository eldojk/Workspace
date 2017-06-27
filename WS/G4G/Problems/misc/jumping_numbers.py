"""
msft

http://www.geeksforgeeks.org/print-all-jumping-numbers-smaller-than-or-equal-to-a-given-value/
"""
from Queue import Queue


def bfs(num, x):
    q = Queue()
    q.put(num)

    while not q.empty():
        num = q.get()

        if num <= x:
            print num,

            last_digit = num % 10

            if last_digit == 0:
                q.put(num * 10 + 1)

            elif last_digit == 9:
                q.put(num * 10 + 8)

            else:
                q.put(num * 10 + (last_digit - 1))
                q.put(num * 10 + (last_digit + 1))


def jumping_numbers(x):
    print 0,
    for i in range(1, 10):
        bfs(i, x)


if __name__ == '__main__':
    jumping_numbers(40)