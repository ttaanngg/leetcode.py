# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = [1, root]
        result = []
        while queue:
            assert len(queue) < 10
            current = queue.pop(0)
            if current == 1:
                if queue:
                    queue.append(1)
                else:
                    break
            else:
                if current:
                    result.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    result.append(None)

        return ','.join(str(i) for i in result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data:
            nodes = [TreeNode(v) if v != 'None' else None for v in data.split(',')]
            i = 0
            for j in range(1, len(nodes)):
                node = nodes[j]
                if i % 2 == 0:
                    nodes[i / 2].left = node
                    i += 1
                else:
                    nodes[i / 2].right = node
                    i += 1
                    while i < 2 * len(nodes) and nodes[i / 2] is None:
                        i += 2
            return nodes[0]
        return None


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.right.left = TreeNode(4)
r.right.right = TreeNode(5)

codec = Codec()
print codec.serialize(r)
print codec.serialize(codec.deserialize(codec.serialize(r)))

print codec.deserialize(codec.serialize(None))
