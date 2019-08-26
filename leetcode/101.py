# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pa = pb = root
        if pa.left == pb.right and pa.right == pb.left:
            return self.isSymmetric(p.right) and self.isSymmetric(p.left)
        return False