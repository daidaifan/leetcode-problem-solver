class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0 or str[0] not in list('+- 0123456789') or '+-' in str or '-+' in str:
            return 0
        sign = 1

        answer = []
        for i, s in enumerate(str):
            print(s)
            if len(answer) == 0 and s == '-':
                sign = -1
            elif len(answer) == 0 and s == '+':
                sign = +1
            elif s =='.':
                break
            elif s in list('0123456789'):
                if len(answer) == 0 and i >= 1 and str[i-1] not in ('+', '-'):
                    return 0
                if len(answer) == 0 and s == '0':
                    return 0
                answer.append(s)
            elif len(answer) > 0 and s not in list('0123456789'):
                break
        if len(answer) == 0:
            return 0
        print(answer)
        answer = int(''.join(answer)) * (sign if sign is not None else +1)
        if answer < - 2 ** 31:
            answer = - 2 ** 31
        elif answer > 2 ** 31 - 1:
            answer = 2 ** 31 -1
        return answer



s = Solution()

r = s.myAtoi("   -42")
print(r)

r = s.myAtoi("    +0a32")
print(r)

r = s.myAtoi("  0000000000012345678")
print(r)
