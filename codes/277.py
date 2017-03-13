# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    return True


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        u, v = 0, 1
        for c in range(2, n + 1):
            if knows(u, v):
                u = c
            else:
                v = c
        if u == n:
            c = v
        else:
            c = u
        for v in range(n):
            if c == v: continue
            if knows(c, v): break
            if not knows(v, c): break
        else:
            return c
        return None
