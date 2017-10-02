# coding=utf-8
"""
amzn

http://qa.geeksforgeeks.org/861/given-number-integer-return-true-its-rotationally-symmetric

Rotational Symmetry means, if we write that number on a page and rotate that page by 180º,
the number remains same.
For Example: 88 is rotationally symmetric. 108801 is rotationally symmetric.
69 is rotationally symmetric.
6996 is NOT rotationally symmetric. 169 is NOT rotationally symmetric.
"""


SYMMETRY = {
    '0': '0',
    '6': '9',
    '9': '6',
    '8': '8',
    '1': '1'
}


def is_symmetric(number):
    global SYMMETRY
    num = str(number)

    if len(num) == 1:
        return num in SYMMETRY.keys()

    i = 0
    j = len(num) - 1

    while i < j:
        if SYMMETRY[num[i]] == num[j]:
            i += 1
            j -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    print is_symmetric(108801)
    print is_symmetric(6996)
    print is_symmetric(69)