"""
amzn, msft

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


def get_result_combinations(res, vals):
    if len(res) == 0:
        return vals

    result = []
    for r in res:
        for v in vals:
            result.append(r + v)

    return result


def find_values_iterative(number):
    res = []
    for i in range(len(number)):
        tmp = KEYPAD[int(number[i])]
        res = get_result_combinations(res, tmp)

    return res


if __name__ == '__main__':
    find_possible_digits('234', 0, [])
    print ''
    print ' '.join(find_values_iterative('234'))
