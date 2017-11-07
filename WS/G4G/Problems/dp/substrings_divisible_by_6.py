"""
amzn

#tricky
http://www.geeksforgeeks.org/number-substrings-divisible-6-string-integers/

Let f(i, m) be the number of strings starting at index i and sum of their digits modulo 3 (so far) is m and
number it represents is even. So, our answer would be
sum f(i, 0) for i in [0, n - 1]

// We initially pass m (sum modulo 3 so far) as 0
f(i, m) = 1 if ((x + m)%3 == 0 and x%2 == 0) else 0+
          f(i + 1, (m + x)%3)  // Recursive
"""


def number_of_strings_starting_at_i(i, m, s, dp):
    """
    Return the number of substring divisible by 6
    and starting at index i in s and previous sum
    of digits modulo 3 is m

    :param i:
    :param m:
    :param s:
    :param dp:
    :return:
    """
    if i == len(s):
        return 0

    if dp[i][m] != -1:
        return dp[i][m]

    result = 0

    x = int(s[i])

    if (x + m) % 3 == 0 and x % 2 == 0:
        result = 1

    result += number_of_strings_starting_at_i(i + 1, (x + m) % 3, s, dp)
    dp[i][m] = result

    return result


def number_of_strings_div_by_6(num):
    n = len(num)
    dp = [[-1 for i in range(3)] for j in num]

    ans = 0

    for i in range(n):
        x = int(num[i])

        if x == 0:
            ans += 1

        else:
            ans += number_of_strings_starting_at_i(i, 0, num, dp)

    return ans


if __name__ == '__main__':
    print number_of_strings_div_by_6('4806')
