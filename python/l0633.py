class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        square_candidates = set()
        a = 0
        while a * a <= c:
            square_candidates.add(a * a)
            a += 1
        for a2 in square_candidates:
            if a2 > c / 2:
                continue
            b2 = c - a2
            if b2 in square_candidates:
                return True
        return False
