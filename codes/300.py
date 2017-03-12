import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        length = 0
        for num in nums:
            p = bisect.bisect(dp, num, 0, length)
            if dp[p-1] != num:
                dp[p] = num
                if p == length:
                    length += 1
        print dp
        return length


solution = Solution()
print solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
print solution.lengthOfLIS([2, 2])
print solution.lengthOfLIS([])
print solution.lengthOfLIS([2])
