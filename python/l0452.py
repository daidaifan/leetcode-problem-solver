"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points = sorted(points, key=lambda x: x[1])
        shotPos = points[0][1]
        solution = 1
        for p in points:
            if shotPos >= p[0]:
                continue
            shotPos = p[1]
            solution += 1
        return solution

"""
Share my explained Greedy solution as the highest voted java solution right now is not ideal
No offense but the currently highest voted java solution is not ideal, the sorting can be adjusted so that there's no need to check again in the for loop.

Idea:
We know that eventually we have to shoot down every balloon, so for each ballon there must be an arrow whose position is between balloon[0] and balloon[1]. Given that, we can sort the array of balloons by their ending position. Then we make sure that while we take care of each balloon from the beginning, we can shoot as many following balloons as possible.

So what position should we pick? We should shoot as right as possible, because all balloons' end position is to the right of the current one. Therefore the position should be currentBalloon[1], because we still need to shoot down the current one.

This is exactly what I do in the for loop: check how many balloons I can shoot down with one shot aiming at the ending position of the current balloon. Then I skip all these balloons and start again from the next one (or the leftmost remaining one) that needs another arrow.

Example:

balloons = [[7,10], [1,5], [3,6], [2,4], [1,4]]
After sorting, it becomes:

balloons = [[2,4], [1,4], [1,5], [3,6], [7,10]]
So first of all, we shoot at position 4, we go through the array and see that all first 4 balloons can be taken care of by this single shot. Then we need another shot for one last balloon. So the result should be 2.


Code:

public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }
        Arrays.sort(points, (a, b) -> a[1] - b[1]);
        int arrowPos = points[0][1];
        int arrowCnt = 1;
        for (int i = 1; i < points.length; i++) {
            if (arrowPos >= points[i][0]) {
                continue;
            }
            arrowCnt++;
            arrowPos = points[i][1];
        }
        return arrowCnt;
    }
"""
