class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j] = the minimum money to guarantee win in subproblem (i, j)
        # target: dp[1][n]
        # dp[i][j] = min_k ( max(k + dp[i, k-1], dp[k+1, j]) )
        import sys
        def DP(dp, start, end):
            if start >= end:
                return 0
            if dp[start][end] != 0:
                return dp[start][end]
            min_k = sys.maxint
            for k in range(start, end+1):
                result = k + max(DP(dp, start, k-1), DP(dp, k+1, end))
                min_k = min(min_k, result)
            dp[start][end] = min_k
            return dp[start][end]
            
        dp = []
        for i in range(n+1):
            dp.append([0] * (n+1))
        return DP(dp, 1, n)
        
