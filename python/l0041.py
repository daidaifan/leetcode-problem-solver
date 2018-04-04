"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

# Correct if the nums does not contain duplicated numbers
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        s = 0
        m = 0
        for n in nums:
            if n > 0:
                s += n
                m = max(m, n)
        total = (m + 1) * (m) // 2
        if s == total:
            return m + 1
        return total - s

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                swap(nums, i, nums[i] - 1)
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


s = Solution()
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([1, 0]))
