import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []

        for row in matrix:
            for cell in row:
                heapq.heappush(heap, cell)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)