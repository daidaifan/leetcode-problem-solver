class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = set()
        for num in nums:
            for s in list(solution):
                if s[-1] <= num:
                    solution.add(s + (num,))
            solution.add((num,))
        return [s for s in solution if len(s) >= 2]
