# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [1]
        if root:
            stack.append(root)
        result = []
        while stack:
            top = stack.pop(0)
            if top == 1:
                if stack:
                    stack.append(1)
                    result.append([])
            else:
                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)
                result[-1].append(top.val)

        return result


solution = Solution()
print solution.levelOrder(None)
