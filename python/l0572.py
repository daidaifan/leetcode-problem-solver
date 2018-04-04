# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(s, t):
            if s is None and t is None:
                return True
            elif s is None or t is None:
                return False
            if s.val != t.val:
                return False
            return isSame(s.left, t.left) & isSame(s.right, t.right)
        
        def travel(s, t):
            if s is None and t is None:
                return True
            elif s is None or t is None:
                return False
            return isSame(s, t) | travel(s.left, t) | travel(s.right, t)
        return travel(s, t)
