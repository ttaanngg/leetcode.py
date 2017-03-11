class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(seq):
            pi, seq = seq[0], seq[1:]
            lo = [x for x in seq if x <= pi]
            hi = [x for x in seq if x > pi]
            return lo, pi, hi

        def select(seq, i):
            if len(seq) < 1000:
                return sorted(nums)[-k]

            lo, pi, hi = partition(seq)
            m = len(lo)
            if m == i:
                return pi
            elif m < i:
                return select(hi, i - m - 1)
            else:
                return select(lo, i)

        return select(nums, len(nums) - k)


solution = Solution()