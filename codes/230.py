# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    counter = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def rec(r):
            if r.left:
                r_l = rec(r.left)
                if r_l[0]:
                    return r_l

            self.counter += 1
            if self.counter == k:
                return True, r.val

            if r.right:
                r_r = rec(r.right)
                if r_r[0]:
                    return r_r

            return False, r.val

        return rec(root)[1] if root else 0


r = TreeNode(2)
r.left = TreeNode(1)

s = Solution()

print s.kthSmallest(r, 2)
