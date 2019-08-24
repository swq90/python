from

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find(root):
            if root:
                if root.val in res:
                    return True
                res.append(k - root.val)
                return find(root.left) or find(root.right)
            return False

        res = []
        return find(root)


