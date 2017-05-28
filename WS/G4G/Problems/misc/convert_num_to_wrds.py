"""
amzn
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


def num_tow_words(num, suffix):
    res = ''

    if num > 19:
        res += TEN[num // 10] + ONE[num % 10]
    else:
        res += TEN[num]

    if num != 0:
        res += suffix

    return res


def better_convert(num):
    output = ''

    output += num_tow_words((num // 10000000), 'crore ')

    output += num_tow_words((num // 100000) % 100, 'lakh ')

    output += num_tow_words((num // 1000) % 100, 'thousand ')

    output += num_tow_words((num // 100) % 10, 'hundred ')

    if num > 100 and num % 100 != 0:
        output += 'and '

    output += num_tow_words(num % 100, '')

    return output


if __name__ == '__main__':
    print ''
    print better_convert(438237764)
    print ''


def convert(num):
    if len(num) == 0:
        return 'empty'

    if len(num) > 4:
        return 'unsupported'

    single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                  "nineteen"]
    tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens_power = ["hundred", "thousand"]

    l = len(num)
    i = 0
    if l > 3:
        print single_digits[int(num[i])], tens_power[1],
        l -= 1
        i += 1

    if l > 2:
        print single_digits[int(num[i])], tens_power[0],
        l -= 1
        i += 1

    if l > 1:
        if int(num[i]) == 1:
            print two_digits[num[0]],
            return
        else:
            print tens_multiple[int(num[i])],
            l -= 1
            i += 1

            if int(num[i]) == 0:
                return

    if l > 0:
        print single_digits[int(num[i])]


if __name__ == '__main__':
    convert('1234')
    convert('1204')
    convert('1200')
