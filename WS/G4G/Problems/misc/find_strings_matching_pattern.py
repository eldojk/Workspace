"""
msft

http://www.geeksforgeeks.org/find-all-strings-that-match-specific-pattern-in-a-dictionary/
"""


def generate_pattern_signature(string):
    i = 0
    hm = {}
    result = []

    for s in string:
        if s in hm:
            result.append(hm[s])

        else:
            hm[s] = i
            result.append(i)
            i += 1

    return result


def compare_signatures(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    if n1 != n2:
        return False

    for i in xrange(n1):
        if s1[i] != s2[i]:
            return False

    return True


def find_matching_strings(strings, pattern):
    pattern_signature = generate_pattern_signature(pattern)
    result = []

    for s in strings:
        string_signature = generate_pattern_signature(s)

        if compare_signatures(string_signature, pattern_signature):
            result.append(s)

    return result


if __name__ == '__main__':
    print find_matching_strings(["abb", "abc", "xyz", "xyy"], 'foo')
    print find_matching_strings(["abb", "abc", "xyz", "xyy"], 'mno')
    print find_matching_strings(["abb", "abc", "xyz", "xyy"], 'aba')
    print find_matching_strings(["abab", "aba", "xyz", "xyx"], 'aba')
