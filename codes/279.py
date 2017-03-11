class Solution(object):
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            tmp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    tmp.add(x - y)
            toCheck = tmp


solution = Solution()
print solution.numSquares(7217)
