def build_trie(words):
    trie = {}
    for word in words:
        insert_word(trie, word)
    return trie


def insert_word(trie, word):
    cur = trie
    for c in word:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
    cur[-1] = True


def with_prefix(trie, prefix):
    cur = trie
    for c in prefix:
        if c not in cur:
            return []
        cur = cur[c]
    cur.pop(-1)
    return cur


def has(trie, word):
    cur = trie
    for c in word:
        if c not in cur:
            return False
    return -1 in cur


class Solution(object):
    def wordSquareCheck(self, square):
        col_words = [[] * len(square)]
        for offset in range(len(square)):
            for c in range(len(square[offset])):
                col_words[c].append(square[offset][c])
        col_words = [''.join(x) for x in col_words]
        for i in range(len(square)):
            if col_words != square[i]:
                return False
        return True

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = build_trie(words)
        result = []


a = ['vczv', 'vfae', 'hghg', 'bvcz']
trie = build_trie(a)
print trie.keys()
