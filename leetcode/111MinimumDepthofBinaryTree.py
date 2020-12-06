# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        depth = {1: [root]}
        i = 1
        while i:
            for node in depth[i]:
                if not node.left and not node.right:
                    return i
                if i + 1 not in depth:
                    depth[i + 1] = []
                if node.left:
                    depth[i + 1].append(node.left)
                if node.right:
                    depth[i + 1].append(node.right)
            i += 1
