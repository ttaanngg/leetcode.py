from collections import Counter

from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        @memo
        def rec(a, b):
            if a == b:
                return 1
            l = [(b - i + 1) for i in range(a, b) if set(s[i:b]) < k]
            if l:
                return max(l)
            return 1

        return max(rec(0, i) for i in range(len(s)))


solution = Solution()
print solution.lengthOfLongestSubstringKDistinct("eceba", 2)
