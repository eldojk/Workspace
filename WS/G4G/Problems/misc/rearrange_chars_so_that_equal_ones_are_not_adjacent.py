"""
https://www.careercup.com/question?id=5693863291256832

Rearrange characters in a string so that no character repeats twice.

Input: aaabc
Output: abaca

Input: aa
Output: No valid output

Input: aaaabc
Output: No valid output
"""


def cmpr(tup1, tup2):
    if tup1[1] < tup2[1]:
        return 1
    elif tup1[1] > tup2[1]:
        return -1
    else:
        return 0


def get_count_dict(string):
    d = {}
    for c in string:
        if d.get(c) is not None:
            d[c] += 1

        else:
            d[c] = 1

    return d


def generate_char_count_tuples_from_dict(di):
    tups = []
    for key in di.keys():
        tups.append((key, di[key]))

    return tups


def re_arrange(string):
    dic = get_count_dict(string)
    tups = generate_char_count_tuples_from_dict(dic)

    tups.sort(cmp=cmpr)

    li = [None for i in string]
    n = len(string)

    even = 0
    odd = 1
    for tup in tups:
        cnt = tup[1]

        while cnt > 0 and even <= n - 1:
            li[even] = tup[0]
            even += 2
            cnt -= 1

        while cnt > 0 and odd <= n - 1:
            li[odd] = tup[0]

            if li[odd] == li[odd - 1]:
                return 'Not possible!'

            odd += 2
            cnt -= 1

    return ''.join(li)


if __name__ == '__main__':
    print re_arrange('aaabc')
    print re_arrange('bcaaa')
    print re_arrange('aa')
    print re_arrange('aaaabc')
    print re_arrange('aaaabcb')
