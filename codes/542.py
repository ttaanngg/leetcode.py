import copy


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        mirror_matrix = copy.copy(matrix)
        validate_pos = lambda p: 0 <= p[0] < len(matrix) and 0 <= p[1] < len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    queue = [1]
                    queue.extend(p for p in [(i - 1, j),
                                             (i + 1, j),
                                             (i, j - 1),
                                             (i, j + 1)] if validate_pos(p))
                    connected = 0
                    while queue:
                        top = queue.pop(0)
                        if isinstance(top, int):
                            if queue and connected:
                                queue.append(top + 1)
                            else:
                                hiaejria
                        else:
                            a, b = top
