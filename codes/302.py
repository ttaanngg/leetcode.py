class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        group = set()

        def dfs(p):
            valid = lambda o: 0 <= o[0] < len(image) and 0 <= o[1] < len(image[0])
            stack = [p]
            while stack:
                top = stack.pop()
                if not valid(top) or top in group or image[top[0]][top[1]] == '0':
                    continue
                group.add(top)
                stack.append((top[0] - 1, top[1],))
                stack.append((top[0] + 1, top[1],))
                stack.append((top[0], top[1] - 1,))
                stack.append((top[0], top[1] + 1,))

        dfs((x, y,))

        min_x, min_y, max_x, max_y = len(image) - 1, len(image[0]) - 1, 0, 0
        for p in group:
            c_x, c_y = p
            min_x = min(min_x, c_x)
            min_y = min(min_y, c_y)
            max_x = max(max_x, c_x)
            max_y = max(max_y, c_y)

        height = max_x - min_x + 1
        width = max_y - min_y + 1
        return height * width


solution = Solution()
print solution.minArea(["0010", "0110", "0100"], 0, 2)
