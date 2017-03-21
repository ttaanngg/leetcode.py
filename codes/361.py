class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0

        counter_rows = [[0] * width for _ in range(height)]
        counter_cols = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 'W':
                    counter_rows[i][j] = 0
                else:
                    counter_rows[i][j] = 1 if grid[i][j] == 'E' else 0
                    if j != 0:
                        counter_rows[i][j] += counter_rows[i][j - 1]
            for j in range(width - 2, -1, -1):
                if grid[i][j] != 'W':
                    counter_rows[i][j] = max(counter_rows[i][j], counter_rows[i][j + 1])

        for j in range(width):
            for i in range(height):
                if grid[i][j] == 'W':
                    counter_cols[i][j] = 0
                else:
                    counter_cols[i][j] = 1 if grid[i][j] == 'E' else 0
                    if i != 0:
                        counter_cols[i][j] += counter_cols[i - 1][j]
            for i in range(height - 2, -1, -1):
                if grid[i][j] != 'W':
                    counter_cols[i][j] = max(counter_cols[i][j], counter_cols[i + 1][j])
        score = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '0':
                    v = counter_cols[i][j] + counter_rows[i][j]
                    if v > score:
                        score = v

        return score
