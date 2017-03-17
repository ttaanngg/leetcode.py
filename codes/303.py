class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # todo: empty nums
        self.cache = [0]
        for i in range(0, len(nums)):
            self.cache.append(self.cache[-1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cache[j + 1] - self.cache[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print obj.sumRange(0, 2)
print obj.sumRange(2, 5)
print obj.sumRange(0, 5)

