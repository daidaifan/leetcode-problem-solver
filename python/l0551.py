class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        accumulated_A = 0
        continuous_L = 0
        for _s in list(s):
            if _s == 'L':
                continuous_L += 1
            else:
                continuous_L = 0
                if _s == 'A':
                    accumulated_A += 1
            if continuous_L == 3 or accumulated_A == 2:
                return False
        return True
