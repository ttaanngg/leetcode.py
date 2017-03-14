from heapq import heappop, heappush
from string import ascii_lowercase as chars


def a_star(G, s, t, h):
    P, Q = {}, [(h(s), None, s)]
    while Q:
        d, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        if u == t: return d - h(t), P
        for v in G[u]:
            w = G[u][v] - h(u) + h(v)
            heappush(Q, (d + w, u, v))
    return float('inf'), None


class WordSpace:
    def __init__(self, words):
        self.words = words
        self.M = {}

    def variants(self, wd, words):
        wasl = list(wd)
        for i, c in enumerate(wasl):
            for oc in chars:
                if c == oc: continue
                wasl[i] = oc
                ow = ''.join(wasl)
                if ow in words:
                    yield ow
            wasl[i] = c

    def __getitem__(self, wd):
        if wd not in self.M:
            self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
        return self.M[wd]

    def heuristic(self, u, v):
        return sum(a != b for a, b in zip(u, v))

    def ladder(self, s, t, h=None):
        if h is None:
            def h(v):
                return self.heuristic(v, t)

        _, P = a_star(self, s, t, h)
        if P is None:
            return [s, None, t]

        u, p = t, []
        while u is not None:
            p.append(u)
            u = P[u]

        p.reverse()
        return p


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        result = WordSpace(set(wordList)).ladder(beginWord, endWord)
        length = len(result)
        if length == 3 and result[1] == None:
            return 0
        return length


solution = Solution()
print solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
