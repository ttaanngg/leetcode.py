# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rec(node, parent=None):
            if not node:
                return 0, True

            consecutive = 0
            if parent and node.val - parent.val == 1:
                consecutive = 1
            r, c_r = rec(node.right, node)
            l, c_l = rec(node.left)

            r = r + consecutive if c_r else r
            if r > l:
                return r, True
            return l, False

        return rec(root)


r = TreeNode(1)
r.right = TreeNode(3)
r.right.right = TreeNode(4)
r.right.right.right = TreeNode(5)
r.right.left = TreeNode(2)

solution = Solution()
print solution.longestConsecutive(r)
