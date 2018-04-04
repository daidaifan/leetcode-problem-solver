class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c2f = {}
        for _s in s:
            c2f[_s] = c2f.get(_s, 0) + 1
        candidates = set([c for c, f in c2f.items() if f == 1])
        for i, _s in enumerate(s):
            if _s in candidates:
                return i
        return -1
