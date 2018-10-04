"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest_sum = sum(nums[-3:])
        for i in range(len(nums)):
            head, tail = i + 1, len(nums) - 1
            while head < tail:
                total = nums[i] + nums[head] + nums[tail]
                if abs(closest_sum - target) > abs(total - target):
                    closest_sum = total
                if total > target:
                    tail -= 1
                else:
                    head += 1
        return closest_sum

nums = [-1, 2, 1, -4]
target = 1
s = Solution()
r = s.threeSumClosest(nums, target)
print(r)

nums = [0, 0, 0]
target = 1
s = Solution()
r = s.threeSumClosest(nums, target)
print(r)

