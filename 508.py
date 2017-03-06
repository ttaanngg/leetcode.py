# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = defaultdict(lambda: 0)

        def travel(node):
            if node is None:
                return 0
            v = node.val + travel(node.left) + travel(node.right)
            counter[v] += 1
            return v

        travel(root)
        if len(counter) == 0:
            return []
        elif len(counter) == 1:
            return counter.keys()

        seq = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        result = [seq[0][0]]
        return result + [v[0] for v in seq[1:] if v[1] == seq[0][1]]


r = TreeNode(5)
# r.left = TreeNode(2)
# r.right = TreeNode(-5)

solution = Solution()
print solution.findFrequentTreeSum(r)
