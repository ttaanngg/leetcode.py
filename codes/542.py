from pprint import pprint

from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        results = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def is_valid(p):
            return 0 <= p[0] < len(matrix) and 0 <= p[1] < len(matrix[0])

        def adjcent(p):
            a, b = p
            return filter(is_valid, [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1), ])

        def bfs(p):
            step = 0
            queue = deque()
            queue.append(1)
            queue.extend(adjcent(p))
            result = []

            visited = set()
            while queue:
                top = queue.popleft()
                if top == 1:
                    if result:
                        return min(result)
                    elif queue:
                        step += 1
                        queue.append(1)
                else:
                    if top in visited:
                        continue
                    visited.add(top)
                    a, b = top
                    if matrix[a][b] == 0:
                        result.append(step)
                    else:
                        queue.extend(adjcent(top))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    results[i][j] = bfs((i, j,))

        return results


solution = Solution()

pprint(solution.updateMatrix([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
]))