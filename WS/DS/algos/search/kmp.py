"""
KMP Algorithm.
DFA generation: https://www.youtube.com/watch?v=KG44VoDtsAA
Pattern matching: https://youtu.be/GTJr8OvyEVQ?t=632
"""


class KMP(object):
    def __init__(self, string):
        self.string = string
        self.pattern = None
        self.dfa = []

    def _compute_index(self, i, j):
        if self.pattern[i] == self.pattern[j]:
            # If match, increment i and j, dfa_val[i] = j+1
            self.dfa[i] = j + 1
            i += 1
            j += 1
        else:
            # If Mismatch
            if j == 0:
                # if j=0, increment i, j stays same
                self.dfa[i] = 0
                i += 1
            else:
                # set j to dfa_val of previous, recursively reduce j until match occurs or j becomes 0
                j = self.dfa[j - 1]
                self._compute_index(i, j)

        return i, j

    def compute_dfa(self, pattern):
        if self.pattern == pattern:
            return

        self.pattern = pattern
        self.dfa = [None for _i in range(len(self.pattern))]
        self.dfa[0] = 0
        i = 1
        j = 0

        while i < len(self.pattern):
            i, j = self._compute_index(i, j)

    def _search_substring(self, str_index, pat_index):
        if self.string[str_index] == self.pattern[pat_index]:
            # If match look for next characters in string and pattern
            str_index += 1
            pat_index += 1
        else:
            # If mismatch
            if pat_index == 0:
                # If pattern beginning has not yet reached, just keep iterating over the string
                str_index += 1
            else:
                # If portion of pattern is already matched, start checking again from dfa_val of previous
                pat_index = self.dfa[pat_index - 1]
                self._search_substring(str_index, pat_index)

        return str_index, pat_index

    def search_substring(self, pattern):
        self.compute_dfa(pattern)
        str_index = 0
        pat_index = 0

        while str_index < len(self.string) and pat_index < len(self.pattern):
            str_index, pat_index = self._search_substring(str_index, pat_index)

        if pat_index < len(self.pattern) - 1:
            return False

        return True
