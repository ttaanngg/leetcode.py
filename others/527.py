import collections


class Solution(object):
    def wordsAbbreviation(self, A):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        groups = collections.defaultdict(list)
        for ix, word in enumerate(A):
            groups[len(word), word[0], word[-1]].append((word, ix))

        def longest_prefix(x, y):
            i = 0
            while i < len(x) and i < len(y) and x[i] == y[i]:
                i += 1
            return i

        mini = collections.defaultdict(int)
        for (size, first, last), tups in groups.iteritems():
            B = sorted(tups)
            for i in xrange(len(B) - 1):
                j = i + 1
                u, idu = B[i]
                v, idv = B[j]
                k = longest_prefix(u, v)
                # u[:k] shared with v[:k]
                mini[idu] = max(mini[idu], k)
                mini[idv] = max(mini[idv], k)

        def abbrev(word, lim):
            lim += 1
            delta = len(word) - 1 - lim
            if delta <= 1: return word
            cand = word[:lim] + str(delta) + word[-1]
            if len(cand) >= len(word): return word
            return cand

        return [abbrev(word, mini[ix]) for ix, word in enumerate(A)]
