class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for j in range((len(nums) - i - 1) / 2):
                    nums[i + j], nums[len(nums) - j] = nums[len(nums) - 1 - j], nums[i + j]


solution = Solution()

nums = [1, 2, 3, 4]

for _ in range(6):
    solution.nextPermutation(nums)
    print nums
