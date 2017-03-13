from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        stack = []
        ptr = root
        pop = False
        while ptr or stack:
            print [item.val for item in stack]
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                while not ptr:
                    ptr = stack.pop()
                if pop:
                    return ptr
                if ptr.val == p.val:
                    pop = True
                ptr = ptr.right

        return None


solution = Solution()
t = TreeNode(5)
t.left = TreeNode(3)
# t.left.right = TreeNode(4)
# t.left.left = TreeNode(2)
# t.right = TreeNode(8)
# t.right.right = TreeNode(9)
# t.right.left = TreeNode(6)
print solution.inorderSuccessor(t, TreeNode(3)).val
