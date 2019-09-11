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
        res =[]
        if root:
            res.append(root.val)
            res.append(self.zigzagLevelOrder(root.left))
            res.append(self.zigzagLevelOrder(root.right))
            return res
        return