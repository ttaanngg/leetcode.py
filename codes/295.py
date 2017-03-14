import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.b = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.a) == len(self.b):
            heapq.heappush(self.b, -heapq.heappushpop(self.a, -num))
        else:
            heapq.heappush(self.a, -heapq.heappushpop(self.b, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.a) == len(self.b):
            return float(-self.a[0] + self.b[0]) / 2.0
        return float(self.b[0])
