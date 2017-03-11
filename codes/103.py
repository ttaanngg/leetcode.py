# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [1]
        if root:
            queue.append(root)
        result = []
        while queue:
            c = queue.pop(0)
            if c == 1:
                if queue:
                    result.append([])
                    queue.append(1)
            else:
                result[-1].append(c.val)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)

        for i in range(len(result)):
            if (i + 1) % 2 == 0:
                result[i].reverse()

        return result


solution = Solution()
print solution.zigzagLevelOrder(None)
