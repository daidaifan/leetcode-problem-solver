class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[-1-i]:
                    return False
            return True
        def dfs(index, s, _solution, solution):
            if index == len(s):
                solution.append(list(_solution))
                return
            for j in range(index, len(s)):
                candidate = s[index:j+1]
                if not isPalindrome(candidate):
                    continue
                _solution.append(candidate)
                dfs(j+1, s, _solution, solution)
                del _solution[-1]

        solution = []
        dfs(0, s, [], solution)
        return solution

string = 'aab'
s = Solution()
r = s.partition(string)
print(r)
