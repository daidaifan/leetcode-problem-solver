"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

- 101. Symmetric Tree
	- Time Complexity:
		- Recursive version:
			-- Tree Travel O(n)
		- Iterative version:
			-- 
	- Space Complexity:
		- Recursive version:
			-- O(1)
		- Iterative version:
			-- 
		
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetricRecursive(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return isSymmetricRecursive(left.right, right.left) and isSymmetricRecursive(left.left, right.right)
        
        if root is None:
            return True
        return isSymmetricRecursive(root.left, root.right)

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		queue = [root]
		while len(queue) != 0:
			new_queue = []
			vals = []
			for i in range(len(queue)):
				if queue[i] is not None:
					vals.append(queue[i].val)
					new_queue.append(queue[i].left)
					new_queue.append(queue[i].right)
				else:
					vals.append(None)
			for i in range(len(vals) / 2):
				if vals[i] != vals[-1-i]:
					return False
			queue = new_queue
		return True
