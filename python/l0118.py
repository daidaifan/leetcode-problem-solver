"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        solution = []
        for i in range(1, numRows + 1):
            _solution = [1 for j in range(i)]
            for j in range(1, i-1):
                _solution[j] = solution[-1][j-1] + solution[-1][j]
            solution.append(_solution)
        return solution

s = Solution()
r = s.generate(10)
print(r)
