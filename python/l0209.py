"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 and s != 0:
            return 0
        if sum(nums) < s:
            return 0
        import sys
        start, end = 0, -1
        current_sum = 0
        min_length = sys.maxint
        while end < len(nums):
            if current_sum < s:
                end += 1
                if end == len(nums):
                    break
                current_sum += nums[end]
            else:
                if min_length > end - start + 1:
                    min_length = end - start + 1
                current_sum -= nums[start]
                start += 1
        return min_length

s = Solution()
s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
