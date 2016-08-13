"""
R-way trie

This implementation does a soft delete.
"""


class TrieNode(object):
    def __init__(self, r):
        self.value = None
        self.nxt = [None for i in range(r)]


class TrieDS(object):
    def __init__(self):
        self.root = TrieNode(256)

    def _put(self, node, key, val, n):
        if not node:
            node = TrieNode(256)

        if n == len(key):
            node.value = val
            return node

        char = key[n]
        pos = ord(char)
        node.nxt[pos] = self._put(node.nxt[pos], key, val, n + 1)
        return node

    def _get(self, node, key, n):
        if not node:
            return None

        if n == len(key):
            return node

        char = key[n]
        pos = ord(char)
        return self._get(node.nxt[pos], key, n + 1)

    def _delete(self, node, key, n):
        if not node:
            return None

        if n == len(key):
            node.value = None
            return node

        char = key[n]
        pos = ord(char)
        node.nxt[pos] = self._delete(node.nxt[pos], key, n + 1)
        return node

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def get(self, key):
        node = self._get(self.root, key, 0)
        return node.value if node else None

    def delete(self, key):
        self._delete(self.root, key, 0)
