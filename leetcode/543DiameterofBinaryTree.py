Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def test(self,root,pre):
            left,right=0,0
            if root.left is not None:
                left+= self.test(root.left,1)
            if root.right is not None:
                right+= self.test(root.right,1)
            if pre:
                return max(left,right)
        left=test(root.left,1)
        right=test(root.right,1)
        return left+right