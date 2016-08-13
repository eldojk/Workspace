from unittest import TestCase

from DS.algos.graphs.r_way_trie import TrieDS


class TrieTestCase(TestCase):
    def setUp(self):
        self.trie = TrieDS()

    def test_put_values(self):
        self.trie.put("star", 8)
        self.trie.put("start", 83)
        self.trie.put("state", 99)
        self.assertEqual(self.trie.get("star"), 8)
        self.assertEqual(self.trie.get("start"), 83)
        self.assertEqual(self.trie.get("state"), 99)

    def test_delete_values(self):
        self.trie.put("star", 8)
        self.trie.put("start", 83)
        self.trie.put("state", 99)
        self.trie.put("rrrr", 33)

        self.assertEqual(self.trie.get("rrrr"), 33)
        self.trie.delete("rrrr")
        self.assertEqual(self.trie.get("rrrr"), None)

        self.trie.delete("star")
        self.assertEqual(self.trie.get("star"), None)
        self.assertEqual(self.trie.get("start"), 83)
