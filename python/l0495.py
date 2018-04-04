class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        time = 0
        start, end = None, None
        for t in timeSeries:
            if start is None:
                start = t
                end = start + duration
                continue
            if end < t:
                time += end - start
                start = t
                end = start + duration
            else:
                end = t + duration
        if start is not None and end is not None:
            time += end - start
        return time
