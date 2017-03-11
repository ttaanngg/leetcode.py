class Solution(object):
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]

        return results


solution = Solution()
for i in solution.grayCode(4):
    print '%04s' % bin(i)[2:]
