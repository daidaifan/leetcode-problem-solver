class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        c2f = {}
        for t in T:
            c2f[t] = c2f.get(t, 0) + 1
        solution = []
        for s in S:
            if s in c2f and c2f[s] > 0:
                solution.append(s * c2f[s])
                c2f[s] = 0
        for t in c2f:
            if c2f[t] != 0:
                solution.append(t * c2f[t])
        return ''.join(solution)

s = Solution()
S = "cba"
T = "abcd"
r = s.customSortString(S, T)
print(r)
S = "kqep"
T = "pekeq"
r = s.customSortString(S, T)
print(r)

