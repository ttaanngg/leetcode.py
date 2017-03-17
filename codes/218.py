class Solution(object):
    def getSkyline(self, buildings):
        if not buildings:
            return []

        buildings.sort(key=lambda x: x[0])

        def dc(buildings):
            length = len(buildings)
            if len(buildings) == 0:
                return []
            elif length == 1:
                return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
            left = dc(buildings[:length / 2])
            right = dc(buildings[length / 2:])
            h1, h2 = -1, -1
            i, j = 0, 0
            result = []

            def appender(x):
                if not result or result[-1][1] != x[1]:
                    result.append(x)

            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    h1 = left[i][1]
                    x = left[i][0]
                    i += 1
                elif left[i][0] > right[j][0]:
                    h2 = right[j][1]
                    x = right[j][0]
                    j += 1
                else:
                    h1 = left[i][1]
                    h2 = right[j][1]
                    x = right[j][0]
                    i += 1
                    j += 1
                p = [x, max(h1, h2)]
                appender(p)

            while i < len(left):
                appender(left[i])
                i += 1
            while j < len(right):
                appender(right[j])
                j += 1
            return result

        return dc(buildings)


solution = Solution()
print solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
print solution.getSkyline([[2, 9, 10], [19, 24, 8]])
print solution.getSkyline([[0, 2, 3], [2, 5, 3]])
print solution.getSkyline([[2, 9, 10]])
