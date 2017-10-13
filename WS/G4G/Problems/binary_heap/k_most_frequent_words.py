"""
msft amzn

http://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/
"""
from DS.algos.graphs.r_way_trie import TrieDS
from DS.algos.binary_heap.priority_queue import PriorityQueue, MIN_PQ
"""
add each word into a trie to keep count. get a k size min heap and add each word with
frequency. get the k word with max frequency
"""


class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __repr__(self):
        return self.word


class KMostFrequentWords:
    def __init__(self, words, k):
        self.words = words
        self.trie = TrieDS()
        self.min_heap = PriorityQueue(k, MIN_PQ)
        self.k = k
        self.pre_process()

    def pre_process(self):
        # inserting first k words
        li = []
        for i in range(self.k):
            w = self.words[i]
            if self.trie.get(w) is None:
                obj = WordFreq(w, 0)
                self.trie.put(w, obj)
                li.append(obj)

            obj = self.trie.get(w)
            obj.freq += 1

        for ob in li:
            self.min_heap.insert(ob)

        # adding remaining items
        for i in range(self.k, len(self.words)):
            w = self.words[i]
            obj = self.trie.get(w)

            if obj is None:
                obj = WordFreq(w, 1)
                self.trie.put(obj)

            if obj.freq <= self.min_heap.get_top().freq:
                continue

            else:
                self.min_heap.delete_top()
                self.min_heap.insert(obj)

    def get_k_most_freq(self):
        return self.min_heap.array
