# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rec(r):
            if not r:
                return -1, 0
            l = rec(r.left)
            r = rec(r.right)
            return 1 + max(l[0], r[0]), max(l[1], r[1], 2 + l[0] + r[0])

        return max(rec(root))
