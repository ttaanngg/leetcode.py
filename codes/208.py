class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                tmp = TreeNode(c)
                cur.children[c] = tmp
            cur = cur.children[c]
        cur.children[1] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return 1 in cur.children

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


trie = Trie()
trie.insert("abc")
print trie.startsWith("abc")
print trie.search("ab")
print trie.search("ab")
trie.insert("ab")
print trie.search("ab")
trie.insert("ab")
print trie.search("ab")
