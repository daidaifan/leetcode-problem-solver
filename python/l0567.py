"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c2f = {}
        for _s in s1:
            c2f[_s] = c2f.get(_s, 0) + 1
        for i, _s in enumerate(s2):
            if i - len(s1) >= 0:
                c = s2[i-len(s1)]
                c2f[c] = c2f.get(c, 0) + 1
                if c2f[c] == 0:
                    del c2f[c]
            c2f[_s] = c2f.get(_s, 0) - 1
            if c2f[_s] == 0:
                del c2f[_s]
            if len(c2f) == 0:
                return True
        return False

s = Solution()
print(s.checkInclusion('ab', 'eidbaooo'))
print(s.checkInclusion('ab', 'eidboaoo'))
