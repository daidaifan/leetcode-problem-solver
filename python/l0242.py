"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # solution 1
        # return ''.join(sorted(s)) == ''.join(sorted(t))
        # solution 2
        c2f = {}
        for _s in s:
            c2f[_s] = c2f.get(_s, 0) + 1
        for _t in t:
            c2f[_t] = c2f.get(_t, 0) - 1
        for c, f in c2f.items():
            if f != 0:
                return False
        return True

s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
