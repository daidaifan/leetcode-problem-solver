"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.

"""
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import queue
        q = queue.PriorityQueue()
        for i in range(1, len(A)):
            q.put((A[i], i))

        left_max_val = A[0]
        left_max_idx = 0
        left_len = 1

        while not q.empty():
            right_min_val, right_idx = q.get()
            if left_max_val <= right_min_val and left_max_idx + 1 == left_len:
                break
            left_max_val = max(left_max_val, right_min_val)
            left_max_idx = max(left_max_idx, right_idx)
            left_len += 1
        return left_len


s = Solution()
A = [1,1,1,0,6,12]
print(s.partitionDisjoint(A))

A = [5,0,3,8,6]
print(s.partitionDisjoint(A))
