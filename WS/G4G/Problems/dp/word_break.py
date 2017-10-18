"""
amzn, goog

(better approach down)
http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".

The idea is simple, we consider each prefix and search it in dictionary. If the prefix is present in dictionary, we
recur for rest of the string (or suffix). If the recursive call for suffix returns true, we return true, otherwise we
try next prefix. If we have tried all prefixes and none of them resulted in a solution, we return false.
"""

DICT = {
    "i": True,
    "like": True,
    "sam": True,
    "sung": True,
    "samsung": True,
    "mobile": True,
    "ice": True,
    "cream": True,
    "icecream": True,
    "man": True,
    "go": True,
    "mango": True
}


def is_present(word):
    global DICT
    return True if DICT.get(word) is not None else False


def can_word_break(string):
    dp = [False for i in range(len(string))] + [True]
    dp[len(string) - 1] = is_present(string[len(string) - 1])

    for i in reversed(range(len(string) - 1)):
        can_splice = False
        for j in range(i + 1, len(string) + 1):
            if can_splice:
                # if can splice is already true, no need to check any more as we are or'ing again and again on
                # can_splice - my lil optimization :)
                break

            can_splice = can_splice or (is_present(string[i:j]) and dp[j])

        dp[i] = can_splice

    # print dp

    return dp[0]


if __name__ == '__main__':
    print can_word_break("ilike")
    print can_word_break("ilikesamsung")


def can_break(word):
    """
    Different approach. Starting at end and adding chars till an actual
    word comes. If this happens, we move on to the next.. Finally, the last
    one should add char

    :param word:
    :return:
    """
    n = len(word)
    i = n - 1
    j = n
    dp = [False for w in word]

    while i >= 0:
        if is_present(word[i: j]):
            dp[i] = True
            j = i

        i -= 1

    print dp
    return dp[0]


if __name__ == '__main__':
    print can_break("ilike")
    print can_break("ilikesamsung")
