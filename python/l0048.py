class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        Lx = len(matrix)
        Ly = len(matrix[0])
        for x in range((Lx + 1) // 2):
            for y in range((Ly + 0) // 2):
                tmp = matrix[x][y]
                matrix[x][y] = matrix[Lx - 1 - y][x]
                matrix[Lx - 1 -y][x] = matrix[Lx - 1 - x][Ly - 1 - y]
                matrix[Lx - 1 - x][Ly - 1 - y] = matrix[y][Ly - 1 - x]
                matrix[y][Ly - 1 - x] = tmp
        return

s = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mat)
s.rotate(mat)
print(mat)

mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(mat)
s.rotate(mat)
print(mat)

"""
    - Note
        -- 4 points exchange: (x, y), (L-1-y, x), (y, L-1-x), (L-1-x, L-1-y)
        -- skip the last y
        -- index boundary: (Lx + 1) // 2 and (Ly + 0) // 2
"""

# [
#       [7,8,1],
#       [6,5,4],
#       [9,2,3]
# ]
# [
#       [5,1,9,11],
#       [2,4,8,10],
#       [13,3,6,7],
#       [15,14,12,16]
# ]
