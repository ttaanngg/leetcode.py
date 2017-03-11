import math


class Solution(object):
    def numSquares(self, n):
        def core(i):
            diff = i - int(math.sqrt(i)) ** 2
            if diff == 0:
                return 1
            return 1 + core(diff)
        r = core(n)
        return r if r else 1


solution = Solution()

print solution.numSquares(12)
print solution.numSquares(2)
print solution.numSquares(4)
print solution.numSquares(13)
