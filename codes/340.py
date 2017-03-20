

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        left = 0
        c = {}
        for i in range(len(s)):
            c[s[i]] = c.setdefault(s[i], 0) + 1
            while len(c) > k:
                v = c[s[left]]
                if v == 1:
                    c.pop(s[left])
                else:
                    c[s[left]] = v - 1
                left += 1
            max_length = max(i - left + 1, max_length)

        return max_length


import a

solution = Solution()
print solution.lengthOfLongestSubstringKDistinct(a.a, a.b)
