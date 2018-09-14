class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if len(dp) > c:
                dp[c] = 1
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1
s = Solution()

r = s.coinChange([1, 2, 5], 11)
print(r)

r = s.coinChange([1], 0)
print(r)
