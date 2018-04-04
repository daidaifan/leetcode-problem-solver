class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        import heapq
        courses = sorted(courses, key=lambda x: (x[1], x[0]))
        pq = []
        start = 0
        for time, due in courses:
            start += time
            heapq.heappush(pq, -time)
            while start > due:
                start += heapq.heappop(pq)
        return len(pq)
