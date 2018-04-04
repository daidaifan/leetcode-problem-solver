"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
	
	- Time Complexity:
		Travel the tree O(n)
	- Space Complexity:
		The tree node O(n)
	- Key Point:
		BFS travel
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        solution = []
        queue = [root]
        while len(queue) != 0:
            new_queue = []
            sub_solution = []
            for i in range(len(queue)):
                if queue[i] is not None:
                    sub_solution.append(queue[i].val)
                    new_queue.append(queue[i].left)
                    new_queue.append(queue[i].right)
            if len(sub_solution) == 0:
                return solution[::-1]
            solution.append(sub_solution)
            queue = new_queue
        
        return solution[::-1]
