# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        length = len(intervals)
        if length <= 1:
            return length
        intervals = [(interval.start, interval.end,) for interval in intervals]
        intervals.sort()

        buckets = [intervals[0][1]]

        for i in range(1, length):
            for j in range(len(buckets)):
                if buckets[j] <= intervals[i][0]:
                    buckets[j] = intervals[i][1]
                    break
            else:
                buckets.append(intervals[i][1])
            sorted(buckets)
        return len(buckets)


solution = Solution()
generator = lambda xl: [Interval(*x) for x in xl]
print solution.minMeetingRooms(generator([[7, 10], [2, 4], ]))
