import math


def log2(a):
    return int(math.log(a, 2))


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        if m == n:
            return m
        l_m = log2(m)
        l_n = log2(n)

        if l_m == l_n:
            a = m
            for i in range(m + 1, n + 1):
                a &= i
            return a
        return 0


solution = Solution()

print solution.rangeBitwiseAnd(0, 1)
print solution.rangeBitwiseAnd(1, 3)
print solution.rangeBitwiseAnd(2, 3)
print solution.rangeBitwiseAnd(6, 7)
