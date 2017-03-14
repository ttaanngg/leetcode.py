# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right


def tree_from_array(seq):
    tree = [TreeNode(i) if i else None for i in seq]

    for i in range(len(seq) - 1, 0, -1):
        if tree[i] and tree[i // 2]:
            if i % 2 == 0:
                tree[i // 2 - 1].right = tree[i]
            else:
                tree[i // 2].left = tree[i]

    return tree[0]


t = tree_from_array(
    [37, -34, -48, None, -100, -100, 48, None, None, None, None, -54, None, -71, -22, None, None, None, 8])

solution = Solution()
print solution.lowestCommonAncestor(t, TreeNode(-100), TreeNode(-71)).val
