"""
msft

http://www.geeksforgeeks.org/longest-even-length-substring-sum-first-second-half/

The idea is to consider all possible mid points (of even length substrings) and
keep expanding on both sides to get and update optimal length as the sum of
two sides become equal
"""


def get_max_length_substring(string, i, j, m, n):
    a = i
    b = j
    m_l = l = 0

    l_sum = 0
    r_sum = 0
    while i >= m and j <= n:
        l_sum += int(string[i])
        r_sum += int(string[j])
        l += 2

        if l_sum == r_sum and l > m_l:
            m_l = l
            a = i
            b = j

        i -= 1
        j += 1

    return string[a:b + 1]


def max_length_substr_with_even_length_and_desired_sums(string):
    m = 0
    n = len(string) - 1
    i = 0
    result = ''

    while i < len(string) - 1:
        j = i + 1
        res = get_max_length_substring(string, i, j, m, n)

        if len(res) > len(result):
            result = res

        i += 1

    return result


if __name__ == '__main__':
    print max_length_substr_with_even_length_and_desired_sums('123123')
    print max_length_substr_with_even_length_and_desired_sums('1538023')