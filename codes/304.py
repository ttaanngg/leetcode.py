class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        self.cache = {}
        self.matrix = matrix

    def calc(self, p):
        if not (0 <= p[0] < len(self.matrix) and 0 <= p[1] < len(self.matrix[0])):
            return 0
        if p not in self.cache:
            self.cache[p] = self.matrix[p[0]][p[1]] \
                            + self.calc((p[0] - 1, p[1],)) \
                            + self.calc((p[0], p[1] - 1,)) \
                            - self.calc((p[0] - 1, p[1] - 1,))
        return self.cache[p]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.calc((row2, col2,)) \
               - self.calc((row2, col1 - 1)) \
               - self.calc((row1 - 1, col2)) \
               + self.calc((row1 - 1, col1 - 1))


matrix = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])

print matrix.sumRegion(2, 1, 4, 3)
print matrix.sumRegion(1, 1, 2, 2)
print matrix.sumRegion(1, 2, 2, 4)
