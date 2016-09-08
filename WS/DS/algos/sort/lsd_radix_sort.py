"""
LSD radix sort for constant length strings
"""
from copy import copy


class LSDRadixSort(object):
    def __init__(self, strings, length):
        self.strings = strings
        self.length = length
        self.radix = 256
        self.array_len = len(self.strings)
        self.aux = copy(self.strings)

    def pre_process(self):
        current_char = self.length - 1

        while current_char >= 0:
            count = [0 for i in range(257)]

            for string in self.strings:
                char = string[current_char]
                index = ord(char) + 1
                count[index] += 1

            for i in range(256):
                count[i + 1] += count[i]

            for string in self.strings:
                char = string[current_char]
                index = ord(char)
                pos = count[index]
                self.aux[pos] = string
                count[index] += 1

            self.strings = copy(self.aux)

            current_char -= 1

    def sort(self):
        self.pre_process()
        return self.aux
