# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def driver(r, pre=0, cur=0):
            if not r:
                return 0 + pre
            print r.val, pre, cur

            return driver(r.left, cur, pre + r.val) + driver(r.right, cur, pre + r.val),

        return driver(root)


solution = Solution()
r = TreeNode(4)
r.left = TreeNode(1)
r.left.left = TreeNode(2)
r.left.left.left = TreeNode(3)

print solution.rob(r)
