class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) < 1:
            return 0
        trace = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        history = set()

        def dfs(x, y, pre=None):
            if (x, y,) in history:
                return 0
            history.add((x, y,))
            if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                if pre == None or pre < matrix[y][x]:
                    if trace[y][x] != 0:
                        return trace[y][x]
                    return 1 + max(
                        dfs(x - 1, y, matrix[y][x]),
                        dfs(x + 1, y, matrix[y][x]),
                        dfs(x, y - 1, matrix[y][x]),
                        dfs(x, y + 1, matrix[y][x]),
                    )
            return 0

        longest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if trace[i][j] == 0:
                    history = set()
                    longest = max(dfs(j, i), longest)
        return longest


solution = Solution()
assert solution.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
assert solution.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
assert solution.longestIncreasingPath([[1], ]) == 1
assert solution.longestIncreasingPath([[[7, 8, 9], [9, 7, 6], [7, 2, 3]], ]) == 6
