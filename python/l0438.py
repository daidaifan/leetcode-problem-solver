class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(s) < len(p):
            return []

        c2f = {}
        for _p in p:
            c2f[_p] = c2f.get(_p, 0) + 1
        solution = []
        for i, _s in enumerate(s):
            if i - len(p) >= 0:
                c = s[i - len(p)]
                c2f[c] = c2f.get(c, 0) + 1
                if c2f[c] == 0:
                    del c2f[c]
            c2f[_s] = c2f.get(_s, 0) - 1
            if c2f[_s] == 0:
                del c2f[_s]
            if len(c2f) == 0:
                solution.append(i - len(p) + 1)
        return solution

s = Solution()
print(s.findAnagrams('cbaebabacd', 'abc'))
