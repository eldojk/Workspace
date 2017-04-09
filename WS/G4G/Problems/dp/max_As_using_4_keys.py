# coding=utf-8
"""
http://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/

Imagine you have a special keyboard with the following keys:
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
                 after what has already been printed.

If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum numbers of A's. That is to
say, the input parameter is N (No. of keys that you can press), the
output is M (No. of As that you can produce).
Examples:

Input:  N = 3
Output: 3
We can at most get 3 A's on screen by pressing
following key sequence.
A, A, A

Input:  N = 7
Output: 9
We can at most get 9 A's on screen by pressing
following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Input:  N = 11
Output: 27
We can at most get 27 A's on screen by pressing
following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V, Ctrl A,
Ctrl C, Ctrl V, Ctrl V

a) For N < 7, the output is N itself. b) Ctrl V can be used multiple times to print current buffer (See last two
examples above). The idea is to compute the optimal string length for N keystrokes by using a simple insight. The
sequence of N keystrokes which produces an optimal string length will end with a suffix of Ctrl-A, a Ctrl-C, followed by
only Ctrl-V's (For N > 6).
The task is to find out the break=point after which we get the above suffix of keystrokes. Definition of a breakpoint is
that instance after which we need to only press Ctrl-A, Ctrl-C once and the only Ctrl-V’s afterwards to generate the
optimal length. If we loop from N-3 to 1 and choose each of these values for the break-point, and compute that optimal
string they would produce. Once the loop ends, we will have the maximum of the optimal lengths for various breakpoints,
thereby giving us the optimal length for N keystrokes.
"""


def find_optimal(N):
    if N <= 6:
        return N

    screen = [0 for i in range(N)]

    for i in range(6):
        screen[i] = i + 1

    i = 7
    while i <= N:
        screen[i - 1] = 0

        b = i - 3
        while b >= 1:

            curr = (i - b - 1) * screen[b - 1]

            if curr > screen[i - 1]:
                screen[i - 1] = curr

            b -= 1

        i += 1

    return screen[N - 1]


if __name__ == '__main__':
    print find_optimal(20)