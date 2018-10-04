class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        solution = [1 for i in range(rowIndex + 1)]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                solution[j] = solution[j-1] + solution[j]
        return solution

s = Solution()
r = s.getRow(5)
print(r)
