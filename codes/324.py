import random


def quick_select(nums, o):
    p = random.randint(0, len(nums) - 1)
    l, r = [], []
    for i in range(len(nums)):
        if nums[i] < nums[p]:
            l.append(nums[i])
        elif nums[i] > nums[p]:
            r.append(nums[i])
        elif i != p:
            l.append(nums[i])

    if o < len(l):
        return quick_select(l, o)
    elif o == len(l):
        return nums[p]
    return quick_select(r, o - len(l) - 1)


class Solution(object):
    def wiggleSort(self, nums):
        n = len(nums)
        mid = quick_select(nums, n / 2)
        tmp = [num for num in nums if num < mid] + [mid] + [num for num in nums if num > mid]
        print tmp


solution = Solution()

a = [1, 5, 1, 1, 6, 4]
solution.wiggleSort(a)
# print a

a = [1, 3, 2, 2, 3, 1]
solution.wiggleSort(a)
# print a
a = [1, 1, 2, 1, 2, 2, 1]
solution.wiggleSort(a)
# print a
