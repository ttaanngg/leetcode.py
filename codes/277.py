# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    # if a == 0 and b == 1:
    #     return True
    # return False
    return True


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return False
        elif n == 1:
            return 1 if knows(0, 0) else 0

        celebrities = dict((i, 0) for i in range(n))
        normal = set()
        for i in range(n):
            for may_celebrity in range(n):
                if knows(i, may_celebrity):
                    normal.add(i)
                    celebrities[may_celebrity] += 1

        for i in normal:
            celebrities.pop(i)

        if celebrities:
            may_celebrity, fans = celebrities.popitem()
            return may_celebrity if fans == n - 1 else -1
        return -1


solution = Solution()
print solution.findCelebrity(2)
