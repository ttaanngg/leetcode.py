class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        def do(i, j):
            cur = pre = 0
            for k in range(i, j):
                tmp = max(pre + nums[k], cur)
                pre = cur
                cur = tmp
            return cur

        return max(
            do(0, len(nums) - 1),
            do(1, len(nums)),
        )


solution = Solution()
print solution.rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
