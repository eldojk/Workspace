"""
amzn, msft

(more done down)
http://www.geeksforgeeks.org/run-length-encoding/
"""


def run_length_encoding(string):
    i = 0
    destination = []

    while i < len(string):
        destination.append(string[i])
        cnt = 1

        while i + 1 < len(string) and string[i] == string[i + 1]:
            cnt += 1
            i += 1

        destination.append(str(cnt))
        i += 1

    return ''.join(destination)


if __name__ == '__main__':
    print run_length_encoding('geeksforgeeks')


"""
amzn

#tricky
wo extra space
"""


def is_compressible(string):
    result_count = 0
    i = 1
    n = len(string)

    if n == 1:
        return False

    while i < n:
        if string[i - 1] != string[i]:
            result_count += 2
            i += 1

        else:
            curr_count = 1
            while i < n and string[i] == string[i - 1]:
                curr_count += 1
                i += 1

            result_count += len(str(curr_count)) + 1

    return result_count <= n


def compress_adjacent_duplicates(string):
    i = 1
    n = len(string)

    while i < n:
        if string[i - 1] != string[i]:
            i += 1

        else:
            curr_count = 1
            start = i - 1
            while i < n and string[i] == string[i - 1]:
                curr_count += 1
                i += 1

            result_string = string[start] + str(curr_count)
            res_len = len(result_string)
            length_to_replace = curr_count
            j = 0

            while length_to_replace > 0:
                if res_len > 0:
                    string[start] = result_string[j]
                    j += 1
                    res_len -= 1
                else:
                    string[start] = None

                start += 1
                length_to_replace -= 1


def shift_chars_right(s):
    n = len(s)
    i = n - 1
    j = n - 1

    while i >= 0:
        if s[i] is not None:
            s[j] = s[i]
            j -= 1

        i -= 1

    while j >= 0:
        s[j] = None
        j -= 1


def get_non_null_start(s):
    i = 0
    n = len(s)

    while i < n:
        if s[i] is not None:
            return i

        i += 1

    return i


def get_chr_and_length(s, j, n):
    c = s[j]
    nums = map(str, range(10))

    if j + 1 < n:
        if s[j + 1] not in nums:
            return c, 1, j + 1

        i = j + 1
        l = i
        while l < n and s[l] in nums:
            l += 1

        count = int(''.join(s[i:l]))
        return c, count, l

    return c, 1, j + 1


def write_chr_and_count(s, i, c, k):
    cnt = str(k)
    n = len(cnt)
    s[i] = c
    i += 1
    j = 0

    while n > 0:
        s[i] = cnt[j]
        i += 1
        j += 1
        n -= 1

    return i


def encode_from_start(s):
    n = len(s)
    i = 0

    j = get_non_null_start(s)

    while j < n:
        c, k, j = get_chr_and_length(s, j, n)
        i = write_chr_and_count(s, i, c, k)


def compress_wo_space(string):
    if not is_compressible(string):
        return string

    s = list(string)
    compress_adjacent_duplicates(s)
    shift_chars_right(s)
    encode_from_start(s)
    return ''.join(s)


if __name__ == '__main__':
    print compress_wo_space('aaaabc')
    print compress_wo_space('abcdeeeeee')
    print compress_wo_space('ancb')
