class Solution(object):
    def convertToTitle(self, n):
        alphabat = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        num2alphabat = {}
        for index, a in enumerate(alphabat):
            num2alphabat[index+1] = a
        solution = []
        while n > 0:
            res = n % 26
            n //= 26
            solution.append(num2alphabat[res])
        result = ''.join(reversed(solution))
        return result


s = Solution()
print(s.convertToTitle(3))
print(s.convertToTitle(26))
print(s.convertToTitle(27))
print(s.convertToTitle(52))
print(s.convertToTitle(53))
print(s.convertToTitle(1000))

