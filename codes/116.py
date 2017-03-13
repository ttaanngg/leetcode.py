# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stack = [1, root]
        if not root:
            return
        while stack:
            item = stack.pop(0)
            if item == 1:
                if stack:
                    stack.append(1)
            else:
                if stack[0] == 1:
                    item.next = None
                else:
                    item.next = stack[0]
                if item.left:
                    stack.append(item.left)
                if item.right:
                    stack.append(item.right)
