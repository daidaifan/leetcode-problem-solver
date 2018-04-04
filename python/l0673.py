class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        size = [0] * len(nums)
        max_size = 0
        for num in nums:
            low, high = 0, max_size
            while low < high:
                mid = low + (high - low) / 2
                if nums[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            dp[low] = num
            size[low] += 1
            max_size = max(max_size, low + 1)
        solution = 1
        for i in range(max_size):
            solution *= size[i]
        return solution
