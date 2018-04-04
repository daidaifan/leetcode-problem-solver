class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def is_win(desiredTotal, length, state):
            if desiredTotal <= 0:
                return False
            if state not in self.used2solution:
                for i in range(1, length+1):
                    if (1 << i & state) == 0:
                        if not is_win(desiredTotal-i, length, 1 << i | state):
                            self.used2solution[state] = True
                            return True
                self.used2solution[state] = False
            return self.used2solution[state]
                    
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        self.used2solution = {}
        return is_win(desiredTotal, maxChoosableInteger, 0)
