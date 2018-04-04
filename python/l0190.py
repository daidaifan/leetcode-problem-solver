class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = 0
        c = 32
        while c > 0:
            s = (s << 1) + (n & 1)
            n = n >> 1
            c = c - 1
        return s

s = Solution()
print(s.reverseBits(43261596))
