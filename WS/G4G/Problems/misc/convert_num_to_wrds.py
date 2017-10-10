"""
amzn, msft

#tricky
http://www.geeksforgeeks.org/program-to-convert-a-given-number-to-words-set-2/
http://www.geeksforgeeks.org/convert-number-to-words/
"""

ONE = ["", "one ", "two ", "three ", "four ",
       "five ", "six ", "seven ", "eight ",
       "nine ", "ten ", "eleven ", "twelve ",
       "thirteen ", "fourteen ", "fifteen ",
       "sixteen ", "seventeen ", "eighteen ",
       "nineteen "]
TEN = ["", "", "twenty ", "thirty ", "forty ",
       "fifty ", "sixty ", "seventy ", "eighty ",
       "ninety "]


def num_to_words(num, suffix):
    res = ''

    if num > 19:
        res += TEN[num // 10] + ONE[num % 10]
    else:
        res += TEN[num]

    if num != 0:
        res += suffix

    return res


def convert_number_to_words(num):
    output = ''

    output += num_to_words((num // 10000000), 'crore ')

    output += num_to_words((num // 100000) % 100, 'lakh ')

    output += num_to_words((num // 1000) % 100, 'thousand ')

    output += num_to_words((num // 100) % 10, 'hundred ')

    if num > 100 and num % 100 != 0:
        output += 'and '

    output += num_to_words(num % 100, '')

    return output


if __name__ == '__main__':
    print ''
    print convert_number_to_words(438237764)
    print ''
