class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower > upper:
            return []

        if not nums:
            if lower == upper:
                return ['{}'.format(lower)]
            return ['{}->{}'.format(lower, upper)]

        pre = lower
        result = []
        for i in range(len(nums)):
            if i == 0:
                if nums[i] - pre == 1:
                    result.append(str(pre))
                elif nums[i] - pre > 1:
                    result.append('{}->{}'.format(pre, nums[i] - 1))
            else:
                if nums[i] - pre == 2:
                    result.append(str(pre + 1))
                elif nums[i] - pre > 2:
                    result.append("{}->{}".format(pre + 1, nums[i] - 1))
            pre = nums[i]

        if upper - pre == 1:
            result.append(str(pre + 1))
        elif upper - pre > 1:
            result.append("{}->{}".format(pre + 1, upper))

        return result


solution = Solution()
print solution.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
print solution.findMissingRanges([], 0, 0)
print solution.findMissingRanges([-2], -3, -1)
