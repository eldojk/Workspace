"""
amzn

http://quiz.geeksforgeeks.org/lexicographically-minimum-string-rotation/
"""


def get_rotation(string):
    s = string + string
    n = len(string)

    # all rotations
    rotations = [s[i: i + n] for i in range(n)]

    rotations.sort()
    return rotations[0]


if __name__ == '__main__':
    print get_rotation('GEEKSQUIZ')
    print get_rotation('GEEKSFORGEEKS')
