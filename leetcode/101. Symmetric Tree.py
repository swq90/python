# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True
        def helper(l,r):
            if l and r and l.val==r.val:
                return helper(l.left,r.right) and helper(l.right,r.left)
            return l==r
        return helper(root.left,root.right)

