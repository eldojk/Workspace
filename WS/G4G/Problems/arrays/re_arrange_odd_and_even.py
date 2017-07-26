"""
amzn

(single scan)

http://www.crazyforcode.com/rearrange-array-even-numbers-odd-numbers/
"""


def re_arrange(array):
    n = len(array)

    even_idx = 0
    odd_idx = 1

    while True:
        while even_idx < n and array[even_idx] % 2 == 0:
            even_idx += 2

        while odd_idx < n and array[odd_idx] % 2 != 0:
            odd_idx += 2

        if even_idx < n and odd_idx < n:
            tmp = array[even_idx]
            array[even_idx] = array[odd_idx]
            array[odd_idx] = tmp

        else:
            break

    return array


if __name__ == '__main__':
    print re_arrange([2, 3, 1, 9, 5, 2, 5, 5, 6, 7])