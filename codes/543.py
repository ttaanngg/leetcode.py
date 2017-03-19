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

        def rec(t):
            if not t:
                return (-1, 0)
            l = rec(t.left)
            r = rec(t.right)

            return max(1 + l[0], 1 + r[0]), max(l[1], r[1], 2 + l[0] + r[0])

        return rec(root)[1]


t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right = TreeNode(3)

solution = Solution()
print solution.diameterOfBinaryTree(t)

t = TreeNode(2)
t.left = TreeNode(5)
t.left.left = TreeNode(3)
t.left.left.left = TreeNode(1)
t.left.left.right = TreeNode(4)
print solution.diameterOfBinaryTree(t)
