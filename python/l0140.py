"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        is_composition = [False] * (len(s) + 1)
        is_composition[0] = True
        dp = [[]]
        for i in range(1, len(s) + 1):
            dp.append([])
            # version 1
			#for j in range(0, i):
			#    if is_composition[j] is True and s[j:i] in wordDict:
			#        is_composition[i] = True
			#        if j == 0:
			#            dp[i].append([s[j:i]])
			#        else:
			#            for k in range(len(dp[j])):
			#                dp[i].append(dp[j][k] + [s[j:i]])
            # version 2
            for w in wordDict:
                j = i - len(w)
                if j < 0:
                    continue
                if is_composition[j] is True and s[j:i] == w:
                    is_composition[i] = True
                    if i - len(w) == 0:
                        dp[i].append([w])
                    else:
                        for k in range(len(dp[j])):
                            dp[i].append(dp[j][k] + [w])
        solution = [' '.join(vals) for vals in dp[len(s)]]
        return solution
"""
# version 3
class Solution(object):
    def wordBreak(self, s, wordDict):
		def DFS(s, wordDict, tail2composition):
			if s in tail2composition:
				return tail2composition[s]
			res = []
			if len(s) == 0:
				res.append('')
				return res
			for w in wordDict:
				if w == s[:len(w)]:
					sub_list = DFS(s[len(w):], wordDict, tail2composition)
					for sub in sub_list:
						if len(sub) == 0:
							res.append(w)
						else:
							res.append(w + ' ' + sub)
			tail2composition[s] = res
			return res

		return DFS(s, wordDict, {})

s = Solution()
print(s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
