class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        used = set()
        while n != 1:
            if n in used:
                return False
            used.add(n)
            new_n = 0
            while n != 0:
                new_n += (n % 10) ** 2
                n /= 10
            n = new_n
        return True
