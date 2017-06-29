"""
msft

http://www.geeksforgeeks.org/dfa-based-division/

1. When we are at state 0 and read 0, we remain at state 0.
2. When we are at state 0 and read 1, we move to state 1, why? The number so formed(1) in decimal gives remainder 1.
3. When we are at state 1 and read 0, we move to state 2, why? The number so formed(10) in decimal gives remainder 2.
4. When we are at state 1 and read 1, we move to state 0, why? The number so formed(11) in decimal gives remainder 0.
5. When we are at state 2 and read 0, we move to state 1, why? The number so formed(100) in decimal gives remainder 1.
6. When we are at state 2 and read 1, we remain at state 2, why? The number so formed(101) in decimal gves remainder 2.

The transition table looks like following:

state   0   1
_____________
 0      0   1
 1      2   0
 2      1   2

"""


def convert_to_binary(num):
    result = []

    while num > 1:
        rem = num % 2
        num //= 2
        result.append(rem)

    result.append(num)
    result.reverse()

    return result


def decimal(binary_num):
    i = len(binary_num) - 1

    result = 0
    pw = 0
    while i >= 0:
        result += binary_num[i] * (2 ** pw)
        pw += 1
        i -= 1

    return result


def create_dfa_table(num):
    states = range(num)
    dfa = [[0, 0] for s in states]

    for state in states:
        binary = convert_to_binary(state)

        for i in [0, 1]:
            binary.append(i)
            dec_nxt_state = decimal(binary)
            nxt_to_state = dec_nxt_state % num
            dfa[state][i] = nxt_to_state
            binary.pop()

    return dfa


def is_divisible(num, dfa):
    state = 0
    binary = convert_to_binary(num)

    for ch in binary:
        state = dfa[state][ch]

    return state == 0


if __name__ == '__main__':
    _dfa = create_dfa_table(3)

    print is_divisible(6, _dfa)
    print is_divisible(5, _dfa)
    print is_divisible(4, _dfa)
    print is_divisible(3, _dfa)
    print is_divisible(2, _dfa)
    print is_divisible(1, _dfa)
    print is_divisible(0, _dfa)

    print ''
    _dfa = create_dfa_table(5)

    print is_divisible(6, _dfa)
    print is_divisible(5, _dfa)
    print is_divisible(4, _dfa)
    print is_divisible(10, _dfa)
    print is_divisible(2, _dfa)
    print is_divisible(1, _dfa)
    print is_divisible(0, _dfa)