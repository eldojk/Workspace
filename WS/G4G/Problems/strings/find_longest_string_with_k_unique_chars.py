"""
amzn

http://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message.
"""


def count_unique_chars(string):
    uc = 0
    cnt = [0 for i in range(26)]

    for s in string:
        if cnt[ord(s) - ord('a')] != 0:
            uc += 1

        cnt[ord(s) - ord('a')] += 1

    return uc


def is_there_less_than_k_unique_chars(count, k):
    u = 0

    for c in count:
        if c > 0:
            u += 1

    return u <= k


def longest_substr(string, k):
    uc = count_unique_chars(string)

    if uc < k:
        print 'Not possible'
        return

    start = 0
    end = 0

    m_size = 1
    m_start = 0

    count = [0 for i in range(len(string))]
    count[ord(string[0]) - ord('a')] += 1

    for i in range(1, len(string)):
        idx = ord(string[i]) - ord('a')
        count[idx] += 1
        end += 1

        while not is_there_less_than_k_unique_chars(count, k):
            idx = ord(string[start]) - ord('a')
            count[idx] -= 1
            start += 1

        if end - start + 1 > m_size:
            m_size = end - start + 1
            m_start = start

    print string[m_start: m_start + m_size]


if __name__ == '__main__':
    longest_substr('aabacbebebe', 3)

