# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def rec(t, s=0):
            if t is None:
                return 0
            if t.right:
                s = rec(t.right, s)
            t.val += s
            s = t.val
            if t.left:
                return rec(t.left, s)
            return t.val

        if root == None:
            return root
        rec(root, 0)
        return root


t = TreeNode(5)
t.left = TreeNode(2)
t.right = TreeNode(13)

solution = Solution()
gt = solution.convertBST(t)
print gt.val
print gt.left.val
print gt.right.val
