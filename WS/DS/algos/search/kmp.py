"""
amzn, msft

KMP Sedgewick

Match transition

    0	1	2	3	4	5
    A	B	A	B	A	C
A	1		3		5
B		2		4
C						6

In case of mismatch at dfa[c][j], we will simulate the normal brute force approach.

in brute force if we have string ababaaa and pattern ababac, we scan from string[0]
when the c mismatches, we set the cursor back at position 1. i.e string[1] and start
over the same process again. But at this position we know we are looking at string
babaaa, so we can skip forward by simulating this new string babaa (as if we are
looking for babac). When c and a mismatches, we have covered only one less state,
than when we started and reached ababaa earlier. And we have this information already
in the table. use it
Instead of re-running at every mismatch, if we keep track of the state we will be at,
if we start at string[1] we can reuse this info (memoize!!!). Lets call this state X

	0	1	2	3	4	5
	A	B	A	B	A	C
A	1	1	3	1	5	1
B	0	2	0	4	0	4
C	0	0	0	0	0	6

1 - x = 0 and | 1,a = x,a; 1,c = x,c which is 0 and 0;
x - x,b = 0  # update x as we need x in next move

2 - x = 0 and | 2,b = x,b; 2,c = x,c which is 0 and 0;
x - x, a = 1

3 - x = 1 and | 3,a = x,a; 3,c - x,x which is 1 and 0
x - x,b = 2

4 - x = 2 and | 4,b = x,b; 4,c = x,c which is 0 and 0
x - x,a = 3

5 - x = 3 and | 5,a = x,a; 5,b = x,b which is 1 and 4
x - x,c = 0

^ the last state is as if we ran babac which is 0 :)
"""


def pos(character):
    return ord(character) - ord('a')


def construct_dfa(pattern):
    dfa = [[0 for i in pattern] for i in range(26)]

    # initialize first match state
    dfa[pos(pattern[0])][0] = 1

    # From state 1
    j = 1
    X = 0
    M = len(pattern)

    while j < M:
        # MisMatch transition
        for c in range(26):
            dfa[c][j] = dfa[c][X]

        # Match transition
        character = pattern[j]
        pos_of_char = pos(character)
        dfa[pos_of_char][j] = j + 1  # on match, move to next state

        # Update X
        X = dfa[pos_of_char][X]

        j += 1

    return dfa


def search(string, pattern):
    """
    Pass in lower case alphabets only (radix is set to 26)

    :param string:
    :param pattern:
    :return:
    """
    dfa = construct_dfa(pattern)

    i = 0
    j = 0
    N = len(string)
    M = len(pattern)

    while i < N and j < M:
        # update to next state based on current char and current state
        j = dfa[pos(string[i])][j]
        i += 1

    # if last state reached
    if j == M:
        return i - M

    return None


if __name__ == '__main__':
    print search('ababaaaaababacc', 'ababac')