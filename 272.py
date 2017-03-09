import heapq
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        heap = []
        mapper = defaultdict(lambda: [])

        def rec(r):
            if r:
                diff = abs(root.val - target)
                heapq.heappush(heap, -diff)
                mapper[diff].append(root.val)
                if len(heap) > k:
                    diff = -heapq.heappop(heap)
                    if len(mapper[diff]) == 2:
                        mapper[diff].pop()
                    else:
                        mapper.pop(-diff)
                rec(r.left)
                rec(r.right)

        rec(root)

        result = []
        [result.extend(v) for v in mapper.values()]

        return result


r = TreeNode(2)
r.left = TreeNode(1)
r.right = TreeNode(3)
solution = Solution()
print solution.closestKValues(r, 5.571429, 5)
