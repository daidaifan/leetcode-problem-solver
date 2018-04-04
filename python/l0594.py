class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num2freq = {}
        for num in nums:
            num2freq[num] = num2freq.get(num, 0) + 1
        solution = 0
        for num, freq in num2freq.items():
            sub_solution1 = freq + num2freq.get(num + 1, 0) if num2freq.get(num + 1, 0) != 0 else 0
            sub_solution2 = freq + num2freq.get(num - 1, 0) if num2freq.get(num - 1, 0) != 0 else 0
            solution = max(solution, sub_solution1, sub_solution2)
        return solution
        
