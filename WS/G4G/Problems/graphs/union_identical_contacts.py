"""
amzn

https://www.careercup.com/question?id=5181387768332288
"""


def is_same(c1, c2):
    return c1[0] == c2[0] \
           or c1[0] == c2[1] \
           or c1[0] == c2[2] \
           or c1[1] == c2[0] \
           or c1[1] == c2[1] \
           or c1[1] == c2[2] \
           or c1[2] == c2[0] \
           or c1[2] == c2[1] \
           or c1[2] == c2[2]


def get_common_contacts(contacts):
    cc = range(len(contacts))  # for connected components

    for i in range(len(contacts)):
        for j in range(i + 1, len(contacts)):

            c1 = contacts[i]
            c2 = contacts[j]

            if is_same(c1, c2):
                cc[j] = cc[i]

    # aggregating values in connected components
    di = {}
    for i in range(len(cc)):
        c = cc[i]
        if di.get(c) is None:
            di[c] = []

        di[c].append(i)

    return di.values()


if __name__ == '__main__':
    ccc = [["John", "john@gmail.com", "john@fb.com"],
           ["Dan", "dan@gmail.com", "+1234567"],
           ["John", "+5412312", "john123@skype.com"],
           ["john1985", "+5412312", "john@fb.com"]]

    print get_common_contacts(ccc)
