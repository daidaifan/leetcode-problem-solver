class Solution(object):
    def findTheDifference(self, s, t):
        c2n = {}
        for _s in s:
            c2n[_s] = c2n.get(_s, 0) + 1
        for _t in t:
            if _t not in c2n:
                return _t
            c2n[_t] -= 1
        for c, n in c2n.items():
            if n != 0:
                return c
