"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            if i == 1:
                dp[i] = nums[0]
            else:
                dp[i] = dp[i-1]
            if i-2 >= 0:
                dp[i] = max(dp[i], dp[i-2] + nums[i-1])
        return dp[len(nums)]

class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        history_max = 0
        last_one = 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = history_max + nums[i]
            history_max = max(history_max, last_one)
            last_one = dp[i]
        print(dp)
        return max(dp)


s = Solution()
print(s.rob([1, 2, 3, 4, 55, 6, 7, 8]))
