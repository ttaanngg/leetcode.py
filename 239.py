import random


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        y = 0
        z = 1
        cy = 0
        cz = 0

        for i in range(len(nums)):
            if nums[i] == nums[y]:
                cy += 1
            elif nums[i] == nums[z]:
                cz += 1
            elif cy == 0:
                y, cy = i, 1
            elif cz == 0:
                z, cz = i, 1
            else:
                cz -= 1
                cy -= 1
        cz = cy = 0
        result = []
        for num in nums:
            if num == nums[y]:
                cy += 1
            elif num == nums[z]:
                cz += 1
        if cy > (len(nums) // 3): result.append(nums[y])
        if cz > (len(nums) // 3): result.append(nums[z])
        return result


solution = Solution()

nums = [1] * 31 + [2] * 29 + [3] * 30
ans = set()

random.shuffle(nums)
print solution.majorityElement(nums)
print solution.majorityElement([1, 2])
