# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def isSubTreeHasOne(node):
            if node is None:
                return False
            elif node.left is None and node.right is None:
                if node.val == 1:
                    return True
                else:
                    return False
            result_left = isSubTreeHasOne(node.left)
            result_right = isSubTreeHasOne(node.right)
            if not result_left:
                node.left = None
            if not result_right:
                node.right = None
            if node.val == 1:
                return True
            return result_left or result_right
        isSubTreeHasOne(root)
        return root
