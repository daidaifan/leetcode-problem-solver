class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_row, num_column = len(grid), len(grid[0])
        max_row, max_column = [0] * num_row, [0] * num_column
        solution = 0
        for i in range(num_row):
            for j in range(num_column):
                max_row[i] = max(max_row[i], grid[i][j])
                max_column[j] = max(max_column[j], grid[i][j])
        for i in range(num_row):
            for j in range(num_column):
                solution += min(max_row[i], max_column[j]) - grid[i][j]
        return solution

s = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
r = s.maxIncreaseKeepingSkyline(grid)
print(r)
