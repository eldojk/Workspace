"""
amzn msft

http://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/

Input:  digits[] = "121"
Output: 3
The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
The possible decodings are "ABCD", "LCD", "AWD"

	0	1	2	3	4
	1	1	2	3	3

	F(n) = f(n-1) # if int s[i] >0 and  <=9
			+
			f(n-2) # if int s[i-1]s[i] is > 0 and <= 26
"""


def get_max_decodings(number):
    decodings = [0 for i in range(len(number) + 1)]
    number = "".join(['0', number])

    decodings[0] = 1
    decodings[1] = 1

    for i in range(2, len(number)):
        decodings[i] = 0

        num = int(number[i])
        if 0 < num <= 9:
            decodings[i] += decodings[i - 1]

        num = int("".join([number[i - 1], number[i]]))
        if 0 < num <= 26:
            decodings[i] += decodings[i - 2]

    return decodings[len(number) - 1]


if __name__ == '__main__':
    print get_max_decodings('1234')


def print_all_decodings(string, i, suffix):
    if i < 0:
        print suffix
        return

    num = int(string[i])
    ascii = num + ord('a') - 1
    if 0 < num <= 9:
        c = chr(ascii)
        print_all_decodings(string, i - 1, c + suffix)

    if i - 1 >= 0:
        n2 = int(string[i - 1])
        num2 = n2 * 10 + num

        if 10 <= num2 < 26:
            ascii = num2 + ord('a') - 1
            c = chr(ascii)
            print_all_decodings(string, i - 2, c + suffix)


if __name__ == '__main__':
    print ''
    print_all_decodings('1234', 3, '')
