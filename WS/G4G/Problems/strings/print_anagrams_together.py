"""
amzn

http://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/

keep index array, and a copy. sort each word first, then sort the copy array.
now take each one and find index and print
"""


class Word(object):
    def __init__(self, string, index):
        self.string = string
        self.index = index


def copy(words):
    arr = []
    for i in range(len(words)):
        arr.append(Word(words[i], i))

    return arr


def comparator(w1, w2):
    if w1.string == w2.string:
        return 0
    elif w1.string < w2.string:
        return -1
    else:
        return 1


def print_anagrams_together(words):
    copy_words = copy(words)

    for w in copy_words:
        w.string = ''.join(sorted(w.string))

    copy_words = sorted(copy_words, cmp=comparator)

    for w in copy_words:
        idx = w.index
        print words[idx],


if __name__ == '__main__':
    print_anagrams_together(["cat", "dog", "tac", "god", "act"])
