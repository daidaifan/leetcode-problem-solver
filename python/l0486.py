class Solution(object):
    def PredictTheWinner(self, nums):
        dp = []
        # initial 2 dimensions list
        for i in range(len(nums)):
            dp.append([0] * len(nums))
        # initial diagonal
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        # fill up
        for dis in range(1, len(nums)):
            for i in range(0, len(nums) - dis):
                j = i + dis
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][len(nums)-1] >= 0
        
