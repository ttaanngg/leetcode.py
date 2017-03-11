import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0] * (n + 1)
        sqrt = lambda x: int(round(math.sqrt(x)))
        perfect = set()

        for i in range(1, n + 1):
            s = sqrt(i)
            if s * s == i:
                perfect.add(i)
                result[i] = 1
            else:
                result[i] = 1 + min(result[j] for j in range(i) if (i - j) in perfect)
        return result[n]


solution = Solution()
print solution.numSquares(7217)
