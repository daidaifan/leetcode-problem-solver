"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

- 057
    - Time Complexity:
        -- Scan intervals: O(n)
    - Space Complexity:
        -- result storage: O(n)
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# Wrong Implementation

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def reduce_intervals(intervals, mid):
            start, end = intervals[mid].start, intervals[mid].end
            target_index = mid
            while target_index < len(intervals) - 1:
                target_index += 1
                print('end', end, intervals[target_index].start)
                if end >= intervals[target_index].start:
                    end = max(intervals[target_index].end, end)
                else:
                    for i in range(target_index - mid - 1, -1, -1):
                        del intervals[mid+i]
                    intervals.insert(mid, Interval(start, end))
                    return

        low, high = 0, len(intervals)-1
        while low < high:
            print(low, high)
            mid = low + (high - low) // 2
            if intervals[mid].start < newInterval.start:
                if mid == len(intervals)-1:
                    intervals.append(newInterval)
                    reduce_intervals(intervals, mid-1)
                    return intervals
                print('compare', intervals[mid].start, newInterval.start, intervals[mid+1].start)
                if newInterval.start < intervals[mid+1].start:
                    # insert here
                    intervals.insert(mid + 1, newInterval)
                    for r in intervals:
                        print(r.start, r.end)

                    reduce_intervals(intervals, mid)
                    return intervals
                else:
                    low = mid + 1
            else:
                if mid == 0:
                    intervals.insert(0, newInterval)
                    reduce_intervals(intervals, 0)
                    return
                else:
                    high = mid

# Time O(n) Space O(n)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        index = 0
        while index < len(intervals) and intervals[index].end < newInterval.start:
            result.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index].start <= newInterval.end:
            newInterval = Interval(min(newInterval.start, intervals[index].start), max(newInterval.end, intervals[index].end))
            index += 1
        result.append(newInterval)
        while index < len(intervals):
            result.append(intervals[index])
            index += 1
        return result

# Time O(n) Space O(1)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        index = 0
        while index < len(intervals) and intervals[index].end < newInterval.start:
            index += 1
        while index < len(intervals) and intervals[index].start <= newInterval.end:
            newInterval = Interval(min(newInterval.start, intervals[index].start), max(newInterval.end, intervals[index].end))
            del intervals[index]
        intervals.insert(index, newInterval)
        return intervals


s = Solution()
result = s.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(4, 9))
for r in result:
    print(r.start, r.end)

result = s.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(13, 17))
for r in result:
    print(r.start, r.end)

result = s.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(-8, 1))
for r in result:
    print(r.start, r.end)




"""
public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
    List<Interval> result = new LinkedList<>();
    int i = 0;
    // add all the intervals ending before newInterval starts
    while (i < intervals.size() && intervals.get(i).end < newInterval.start)
        result.add(intervals.get(i++));
    // merge all overlapping intervals to one considering newInterval
    while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
        newInterval = new Interval( // we could mutate newInterval here also
                Math.min(newInterval.start, intervals.get(i).start),
                Math.max(newInterval.end, intervals.get(i).end));
        i++;
    }
    result.add(newInterval); // add the union of intervals we got
    // add all the rest
    while (i < intervals.size()) result.add(intervals.get(i++));
    return result;
}
"""
