class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        solution = ''
        parse_mode = False
        cur_parsed = ''
        times = 1
        for _s in s:
            if '1' <= _s <= '9':
                times = int(_s)
            elif _s == '[':
                parse_mode = True
            elif _s == ']':
                solution += cur_parsed * times
                times = 1
                parse_mode = False
                cur_parsed = ''
            elif parse_mode:
                cur_parsed += _s
            else:
                solution += _s
        return solution

s = Solution()
# abc abc cd cd cd ef
print(s.decodeString('2[abc]3[cd]ef'))
# acc acc acc
print(s.decodeString('3[a2[c]]'))
