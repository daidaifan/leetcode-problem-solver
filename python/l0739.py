# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        solution = []
        for index, value in enumerate(reversed(temperatures)):
            while len(stack) != 0 and stack[-1][1] <= value:
                del stack[-1]
            if len(stack) == 0:
                stack.append((index, value))
                solution.append(0)
                continue
            solution.append(index - stack[-1][0])
            stack.append((index, value))
        return list(reversed(solution))


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
r = s.dailyTemperatures(temperatures)
print(r)
