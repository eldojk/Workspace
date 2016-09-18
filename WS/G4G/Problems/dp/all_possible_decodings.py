"""
http://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/

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
        if num > 0 and num <= 9:
            decodings[i] += decodings[i - 1]

        num = int("".join([number[i - 1], number[i]]))
        if num > 0 and num <= 26:
            decodings[i] += decodings[i - 2]

    return decodings[len(number) - 1]


print get_max_decodings('1234')
