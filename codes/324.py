import copy


class Solution(object):
    def wiggleSort(self, nums):
        tmp = copy.copy(nums)
        tmp.sort()
        j = 0
        mid = (len(nums)+1) // 2
        r = len(nums) - 1
        print nums
        print tmp[mid], mid
        nums[mid] = tmp[mid]

        for i in range(0, len(nums)):
            if i == mid:
                continue
            if i % 2 == 0:
                p = j
                if j != mid:
                    j += 1
            else:
                p = r
                if r != mid:
                    r -= 1

            nums[i] = tmp[p]


solution = Solution()

a = [1, 5, 1, 1, 6, 4]
solution.wiggleSort(a)
print a

a = [1, 3, 2, 2, 3, 1]
solution.wiggleSort(a)
print a
