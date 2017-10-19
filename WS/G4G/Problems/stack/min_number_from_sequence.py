"""
amzn

#tricky
http://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/
"""
from G4G.Problems.stack.stack import Stack


def print_min_number(sequence):
    result = []
    s = Stack()

    for i in range(len(sequence) + 1):
        s.push(i + 1)

        if i == len(sequence) or sequence[i] == 'I':

            while not s.is_empty():
                result.append(s.pop())

    print ''.join(map(str, result))


if __name__ == '__main__':
    print_min_number('IDID')
    print_min_number('IIDDD')
