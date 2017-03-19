def build_trie(words):
    root = {}
    for word in words:
        insert(root, word)
    return root


def insert(trie, word):
    cur = trie
    for c in word:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
    cur[-1] = True


def search(trie, word):
    return prefix(trie, word).get(-1, False)


def prefix(trie, prefix):
    cur = trie
    for c in prefix:
        if c not in cur:
            return None
        cur = cur[c]
    return cur


def delete(trie, word):
    def rec(t, w):
        if w:
            if delete(t[w[0]], w[1:]):
                t.pop(t[w[0]])
                return True if len(t) == 1 else False
        if t is None or -1 in t:
            return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        trace = set()

        height = len(board)
        width = len(board[0])

        if isinstance(board[0], str):
            for i in range(len(board)):
                board[i] = list(board[i])

        def is_validate(p):
            return 0 <= p[0] < height and 0 <= p[1] < width

        def dfs(tt, pos):
            r = []
            if tt and pos not in trace:
                a, b = pos
                pre = board[a][b]
                board[a][b] = '#'
                if -1 in tt:
                    r.append(pre)
                for p in filter(is_validate, [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]):
                    r += [pre + (v if v != -1 else '')
                          for v in dfs(tt.get(board[p[0]][p[1]], None), p)]
                board[a][b] = pre
            return r

        result = set()
        trie = build_trie(words)
        for i in range(height):
            for j in range(width):
                p = trie.get(board[i][j], None)
                result |= set(dfs(p, (i, j,)))
                for w in result:
                    delete(trie, w)
        return list(result)


solution = Solution()
print solution.findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"])

import a

print Solution().findWords(a.a, a.b)
