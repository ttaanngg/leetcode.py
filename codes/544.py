
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = map(str, range(1, n + 1))
        while n > 1:
            res = ['(' + res[i] + ',' + res[n - i - 1] + ')' for i in range(n >> 1)]
            n >>= 1
        return res[0]


solution = Solution()
print solution.findContestMatch(4)
print solution.findContestMatch(8)
print solution.findContestMatch(16)
print solution.findContestMatch(32)
print solution.findContestMatch(64)
print solution.findContestMatch(2 ** 12)
