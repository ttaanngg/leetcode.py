# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        inf = float('inf')

        def rec(r):
            if not r:
                return inf, 0xffffffff
            return min(
                (abs(target - r.val), r.val),
                rec(r.left),
                rec(r.right),
                key=lambda x: x[0],
            )

        return rec(root)[1]


solution = Solution()
r = TreeNode(2)
r.left = TreeNode(1)
print solution.closestValue(r, -2)
