class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(val):
            strs = str(val)
            for s in strs:
                if s == '0':
                    return False
                if val % int(s) != 0:
                    return False
            return True
        solution = []
        for val in range(left, right + 1):
            if check(val):
                solution.append(val)
        return solution

s = Solution()
r = s.selfDividingNumbers(1, 22)
print(r)
