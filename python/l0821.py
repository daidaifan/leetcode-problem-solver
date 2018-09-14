class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        candidate = []
        for index, s in enumerate(S):
            if s == C:
                candidate.append(index)
        solution = []
        cur_candidate_index = 0
        head_index = tail_index = candidate[cur_candidate_index]
        for index, s in enumerate(S):
            if cur_candidate_index < len(candidate) - 1 and index == candidate[cur_candidate_index]:
                cur_candidate_index += 1
                head_index = tail_index
                tail_index = candidate[cur_candidate_index]
            solution.append(min(abs(head_index - index), abs(tail_index - index)))
        return solution

s = Solution()
r = s.shortestToChar(S = "loveleetcode", C = 'e')
# [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
print(r)
