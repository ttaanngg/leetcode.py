class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()

        def valid_pos(p):
            return 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])

        def on_island(p):
            return grid[p[0]][p[1]] == '1'

        def marker(p):
            visited.add(p)
            generate = lambda x: [(x[0] - 1, x[1],), (x[0] + 1, x[1],), (x[0], x[1] - 1,), (x[0], x[1] + 1,), ]
            trace = generate(p)
            while trace:
                t = trace.pop(0)
                if t in visited or not valid_pos(t) or not on_island(t):
                    continue
                visited.add(t)
                trace.extend(generate(t))

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                p = (i, j,)
                if grid[i][j] == '1' and p not in visited:
                    counter += 1
                    marker(p)

        return counter
