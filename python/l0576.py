class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        def check(m, n, row, col):
            return row >= 0 and row <= m-1 and col >= 0 and col <= n-1
        
        solution = 0
        dp = []
        for a in range(m):
            dp.append([0] * n)
        dp[i][j] = 1
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        MOD = 10**9 + 7
        for l in range(N):
            s_dp = []
            for a in range(m):
                s_dp.append([0] * n)
            for a in range(m):
                for b in range(n):
                    if dp[a][b] == 0:
                        continue
                    for move in moves:
                        row = a + move[0]
                        col = b + move[1]
                        if check(m, n, row, col):
                            s_dp[row][col] += dp[a][b]
                            s_dp[row][col] %= MOD
                        else:
                            solution += dp[a][b]
                            solution %= MOD
            dp = s_dp
        return solution
