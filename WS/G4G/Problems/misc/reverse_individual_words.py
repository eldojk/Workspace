"""
amzn

http://www.geeksforgeeks.org/reverse-words-in-a-given-string/
"""


def reverse(li,  start, end):
    while start < end:
        tmp = li[start]
        li[start] = li[end]
        li[end] = tmp

        start += 1
        end -= 1


def reverse_individual_words(li):
    start = 0
    end = 0
    n = len(li)
    last_space = 0

    while end < n:
        if li[end] != ' ':
            end += 1

        else:
            last_space = end
            reverse(li, start, end - 1)
            start = end + 1
            end += 1

    reverse(li, last_space + 1, n - 1)

    return li


def reverse_words(string):
    li = list(string)

    reverse_individual_words(li)
    reverse(li, 0, len(li) - 1)

    return ''.join(li)


if __name__ == '__main__':
    print reverse_words('i like this program very much')