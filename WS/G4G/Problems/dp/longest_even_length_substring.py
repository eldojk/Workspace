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


"""
better approach
consider every midpoint and check
"""


def max_len_substr_ev_len(string):
    mx_len = 0
    start = 0

    for i in range(len(string) - 1):
        l = i
        r = i + 1
        l_sum = r_sum = 0
        curr_len = 0

        while l >= 0 and r < len(string):

            l_sum += int(string[l])
            r_sum += int(string[r])
            curr_len += 2

            if l_sum == r_sum:
                mx_len = curr_len
                start = l

            l -= 1
            r += 1

    return string[start: start + mx_len]


if __name__== '__main__':
    print max_len_substr_ev_len('123123')
    print max_len_substr_ev_len('1538023')
