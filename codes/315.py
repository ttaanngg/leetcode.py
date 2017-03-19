from collections import defaultdict


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        record = defaultdict(lambda: 0)

