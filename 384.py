import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.shuffle_result = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.shuffle_result = self.nums[:]
        return self.shuffle_result

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.shuffle_result)):
            j = random.randint(0, len(self.shuffle_result) - 1)
            self.shuffle_result[i], self.shuffle_result[j] = self.shuffle_result[j], self.shuffle_result[i]

