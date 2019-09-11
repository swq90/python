# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]
        self.traversal(root, res)
        return res

    def traversal(self,root,res):
        if root:
            self.traversal(root.left, res)
            res.append(root.val)
            self.traversal(root.right, res)


        # return [] if root is None else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
