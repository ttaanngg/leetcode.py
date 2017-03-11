import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []

        container = []
        for i in range(k):
            heapq.heappush(container, (-nums[i], i,))

        result = [-container[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(container, (-nums[i], i,))
            while container and container[0][1] <= i - k:
                heapq.heappop(container)
            result.append(-container[0][0])

        return result


solution = Solution()
print solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print solution.maxSlidingWindow([], 0)
print solution.maxSlidingWindow([0], 1)
