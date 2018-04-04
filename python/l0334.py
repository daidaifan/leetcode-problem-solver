class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sequence = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]
                num_sequence += 1
            else:
                num_sequence = 1
            if num_sequence == 3:
                return True
        return False

