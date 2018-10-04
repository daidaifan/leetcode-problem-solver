class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board
        m, n = len(board), len(board[0])
        answer = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                num_live = 0
                for a in (-1, 0, 1):
                    for b in (-1, 0, 1):
                        if a == 0 and b == 0:
                            continue
                        x = i + a
                        y = j + b
                        if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                            num_live += 1
                answer[i][j] = num_live
        print(answer)
        for i in range(m):
            for j in range(n):
                if ((answer[i][j] == 2 or answer[i][j] == 3) and board[i][j] == 1) or (answer[i][j] == 3 and board[i][j] == 0):
                    answer[i][j] = 1
                else:
                    answer[i][j] = 0
        return answer

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(board)
s = Solution()
r = s.gameOfLife(board)
print(r)
