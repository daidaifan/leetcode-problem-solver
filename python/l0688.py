class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def check(N, r, c):
            if r >= 0 and r <= N-1 and c >= 0 and c <= N-1:
                return True
            return False
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        dp = []
        for i in range(N):
            dp.append([1] * N)
        for l in range(K):
            s_dp = []
            for i in range(N):
                s_dp.append([0] * N)
            for i in range(N):
                for j in range(N):
                    for m in moves:
                        row = i + m[0]
                        col = j + m[1]
                        if check(N, row, col):
                            s_dp[row][col] += dp[i][j]
            dp = s_dp
        return dp[r][c] / float(8 ** K)
