"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num2index = {}
        for index, num in enumerate(nums):
            if num in num2index and abs(num2index[num] - index) <= k:
                return True
            num2index[num] = index
        return False

