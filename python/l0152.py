class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        min_val, max_val, global_max_val = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_val, max_val = max_val, min_val
            min_val = min(nums[i], min_val * nums[i])
            max_val = max(nums[i], max_val * nums[i])
            global_max_val = max(global_max_val, max_val)
        return global_max_val
