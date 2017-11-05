

def convert_to_roman(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return m[num / 1000] + c[(num % 1000) / 100] + x[(num % 100) / 10] + i[num % 10]


if __name__ == '__main__':
    print convert_to_roman(3549)  # MMMDXLIX


"""
amzn msft

#tricky
http://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/ -- seems wrong
https://stackoverflow.com/questions/9073150/converting-roman-numerals-to-decimal
"""


def process_decimal(curr_decimal, last_decimal, last_number):
    if last_decimal > curr_decimal:

        return last_number - curr_decimal

    return last_number + curr_decimal


def convert_to_decimal(string):
    last_number = 0
    last_decimal = 0

    i = len(string) - 1

    while i >= 0:
        s = string[i]

        if s == 'M':
            last_number = process_decimal(1000, last_decimal, last_number)
            last_decimal = 1000

        elif s == 'D':
            last_number = process_decimal(500, last_decimal, last_number)
            last_decimal = 500

        elif s == 'C':
            last_number = process_decimal(100, last_decimal, last_number)
            last_decimal = 100

        elif s == 'L':
            last_number = process_decimal(50, last_decimal, last_number)
            last_decimal = 50

        elif s == 'X':
            last_number = process_decimal(10, last_decimal, last_number)
            last_decimal = 10

        elif s == 'V':
            last_number = process_decimal(5, last_decimal, last_number)
            last_decimal = 5

        elif s == 'I':
            last_number = process_decimal(1, last_decimal, last_number)
            last_decimal = 1

        i -= 1

    return last_number


if __name__ == '__main__':
    print convert_to_decimal('MMMDXLIX')
