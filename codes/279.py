import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        perfect = []
        i = 1
        while i * i <= n:
            perfect.append(i)
            i += 1

        toCheck = {n}
        cnt = 0
        while toCheck:
            cnt += 1
            tmp = set()
            for x in toCheck:
                for y in perfect:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    tmp.add(x - y)
            toCheck = tmp
        return cnt


solution = Solution()
print solution.numSquares(7217)
