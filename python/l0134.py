class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        end, start = 0, len(gas) - 1
        acc_sum = gas[start] - cost[start]
        while end < start:
            if acc_sum >= 0:
                acc_sum += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                acc_sum += gas[start] - cost[start]
        if acc_sum < 0:
            return -1
        return start

