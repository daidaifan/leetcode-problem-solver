class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        sign = '' if num >= 0 else '-'
        num = abs(num)
        bits = []
        while num > 0:
            bits.append(num%7)
            num /= 7
        return sign + ''.join(map(str, reversed(bits)))
