"""
amzn

check link for explanation
http://www.geeksforgeeks.org/find-possible-words-phone-digits/
"""


KEYPAD = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}


def find_possible_digits(number, index, current_list):
    if index == len(number):
        print ''.join(current_list),
        return

    chars = KEYPAD[int(number[index])]

    for c in chars:
        current_list.append(c)
        find_possible_digits(number, index + 1, current_list)
        current_list.pop()


if __name__ == '__main__':
    find_possible_digits('234', 0, [])