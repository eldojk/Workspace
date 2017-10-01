"""
amzn

http://www.geeksforgeeks.org/length-of-the-longest-valid-substring/
"""
from G4G.Problems.stack.stack import Stack


def find_max_len(string):
    n = len(string)
    result = 0

    s = Stack()
    s.push(-1)

    for i in range(n):
        if string[i] == '(':
            s.push(i)

        else:

            s.pop()

            if not s.is_empty():
                result = max(result, i - s.peek())

            else:
                s.push(i)

    return result


if __name__ == '__main__':
    print find_max_len('((()()')
    print find_max_len('()(()))))')