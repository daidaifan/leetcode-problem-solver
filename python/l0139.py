class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
    
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        solution = [False] * (len(s) + 1)
        solution[0] = True
        for i in range(1, len(s) + 1):
            for j in range(1, i + 1):
                if solution[i-j] is True and s[i-j:i] in wordDict:
                    solution[i] = True
                    break
        return solution[len(s)]
