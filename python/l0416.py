class Solution(object):
    def canPartition(self, nums):
        if len(nums) == 0:
            return True
        elif sum(nums) & 1 == 1:
            return False
        target = sum(nums) >> 1
        dp = []
        for i in range(len(nums) + 1):
            dp.append([False] * (target + 1))
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(nums[i-1], target+1):
                dp[i][j] = (dp[i-1][j]) or (dp[i-1][j-nums[i-1]])
                
        return dp[len(nums)][target]

"""
# DFS solution
class Solution(object):
    def canPartition(self, nums):
        if len(nums) == 0:
            return True
        if sum(nums) & 1 != 0:
            return False
        def dfs(target, cur_sum, nums):
            if target == cur_sum:
                if len(nums) == 0:
                    return True
                return dfs(target, nums[-1], nums[:-1])
            for i in range(len(nums)):
                tried_val = nums[i]
                if cur_sum + tried_val <= target:
                    nums[-1], nums[i] = nums[i], nums[-1]
                    if dfs(target, tried_val + cur_sum, nums[:-1]):
                        return True
                    nums[i], nums[-1] = nums[-1], nums[i]
            return False
                    
        nums.sort()
        return dfs(sum(nums)//2, nums[-1], nums[:-1])
"""
