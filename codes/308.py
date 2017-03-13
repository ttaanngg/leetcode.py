class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.changes = {}
        self.matrix = matrix
        self.cache = [[0] * len(row) for row in matrix]
        try:
            self.cache[0][0] = matrix[0][0]
        except IndexError:
            return

        def getter(r, c):
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                return self.cache[r][c]
            return 0

        for r_offset in range(len(matrix)):
            for c_offset in range(len(matrix[r_offset])):
                self.cache[r_offset][c_offset] = \
                    self.matrix[r_offset][c_offset] \
                    + self.getter(r_offset - 1, c_offset) \
                    + self.getter(r_offset, c_offset - 1) \
                    - self.getter(r_offset - 1, c_offset - 1)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.changes[(row, col,)] = val - self.matrix[row][col]

    def getter(self, r, c):
        if 0 <= r < len(self.matrix) and 0 <= c < len(self.matrix[0]):
            return self.cache[r][c]
        return 0

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = self.getter(row2, col2) \
                 - self.getter(row1 - 1, col2) \
                 - self.getter(row2, col1 - 1) \
                 + self.getter(row1 - 1, col1 - 1)

        for change, v in self.changes.iteritems():
            if row1 <= change[0] <= row2 and col1 <= change[1] <= col2:
                result += v
        return result


solution = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])
print solution.sumRegion(2, 1, 4, 3)
solution.update(3, 2, 2)
print solution.sumRegion(2, 1, 4, 3)

nm = NumMatrix([[]])
