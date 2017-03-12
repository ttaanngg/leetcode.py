class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.vec2d.reverse()

    def clean(self):
        while self.vec2d and not self.vec2d[-1]:
            self.vec2d.pop()

    def next(self):
        """
        :rtype: int
        """
        r = self.vec2d[-1].pop(0)
        self.clean()
        return r

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.vec2d) != 0



        # Your Vector2D object will be instantiated and called as such:
        # i, v = Vector2D(vec2d), []
        # while i.hasNext(): v.append(i.next())
