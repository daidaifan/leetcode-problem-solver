"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def back_tracking(index, nums, target, _solution, solution):
            if index == len(nums):
                return
            val = nums[index]
            if val == target:
                _solution.append(val)
                solution.append(list(_solution))
                del _solution[-1]
                return
            elif val < target:
                _solution.append(val)
                back_tracking(index+1, nums, target - val, _solution, solution)
                del _solution[-1]
            back_tracking(index+1, nums, target, _solution, solution)

        candidates = sorted(candidates)
        solution = []
        back_tracking(0, candidates, target, [], solution)
        solution = [tuple(s) for s in solution]
        solution = list(set(solution))
        return solution


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
r = s.combinationSum2(candidates, target)
print(r)
