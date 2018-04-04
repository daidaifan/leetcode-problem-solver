"""
boundary case bug: input 2
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        table = [1] * n
        table[0] = table[1] = 0
        for i in range(2, n):
            c = i
            if table[c] == 0:
                continue
            c += i
            while c < n:
                table[c] = 0
                c += i
        print(table)
        return sum(table)

s = Solution()
print(s.countPrimes(2))
print(s.countPrimes(10))
