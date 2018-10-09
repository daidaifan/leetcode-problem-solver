"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        S = list(S)
        head, tail = 0, len(S)-1
        while head < tail:
            while head < tail and not S[head].isalpha():
                head += 1
            while head < tail and not S[tail].isalpha():
                tail -= 1
            if head < tail:
                S[head], S[tail] = S[tail], S[head]
            head, tail = head + 1, tail - 1
        return ''.join(S)

s = Solution()
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
