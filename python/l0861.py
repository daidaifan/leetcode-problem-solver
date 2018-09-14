class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        num_row, num_column = len(A), len(A[0])
        for i in range(num_row):
            if A[i][0] == 0:
                for j in range(num_column):
                    if A[i][j] == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0
        sum_row = [0] * num_column
        for i in range(num_row):
            for j in range(num_column):
                sum_row[j] += A[i][j]
        matrix_score = 0
        base = 1
        print(sum_row)
        for s in reversed(sum_row):
            point = max(s, num_row - s)
            print(point)
            matrix_score += point * base
            base *= 2
        return matrix_score

s = Solution()
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(A)
r = s.matrixScore(A)
print(r)
