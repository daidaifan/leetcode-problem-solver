# TLE version
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length2sequence = {}
        for num in nums:
            for length, sequence in length2sequence.items():
                if sequence[-1] < num:
                    new_sequence = sequence + [num]
                    new_length = len(new_sequence)
                    if new_length not in length2sequence or new_sequence[-1] < length2sequence[new_length][-1]:
                        length2sequence[new_length] = new_sequence
            if 1 not in length2sequence or num < length2sequence[1][0]:
                length2sequence[1] = [num]
            
        return max(length2sequence.keys())
"""
