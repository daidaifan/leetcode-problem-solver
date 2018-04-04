# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def travel(node):
            if node is None:
                return
            travel(node.left)
            if self.prev is not None and self.min > node.val - self.prev:
                self.min = node.val - self.prev
            self.prev = node.val
            travel(node.right)
            
        import sys
        self.min = sys.maxint
        self.prev = None
        travel(root)
        return self.min
