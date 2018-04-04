# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        def travel(node, tiles):
            if node is None:
                return 0
            sum_left = travel(node.left, tiles)
            sum_right = travel(node.right, tiles)
            diff = abs(sum_left - sum_right)
            tiles.append(diff)
            sum_all = node.val + sum_left + sum_right
            return sum_all
        
        tiles = []
        travel(root, tiles)
        return sum(tiles)
