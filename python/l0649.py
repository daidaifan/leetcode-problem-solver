class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        from collections import deque
        senate = list(senate)
        n = len(senate)
        R, D = deque(), deque()
        for index, c in enumerate(senate):
            if c == 'R':
                R.append(index)
            else:
                D.append(index)
        while len(R) != 0 and len(D) != 0:
            r, d = R.popleft(), D.popleft()
            if r < d:
                R.append(r+n)
            else:
                D.append(d+n)
        answer = 'Dire'
        if len(R) > len(D):
            answer = 'Radiant'
        return answer
