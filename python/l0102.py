# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        solution = []
        while len(queue) != 0:
            new_queue = []
            sub_solution = []
            for node in queue:
                if node is not None:
                    sub_solution.append(node.val)
                    if node.left is not None:
                        new_queue.append(node.left)
                    if node.right is not None:
                        new_queue.append(node.right)
            solution.append(sub_solution)
            queue = new_queue
        return solution


