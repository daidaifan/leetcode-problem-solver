class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        person_positions = []
        for index, seat in enumerate(seats):
            if seat == 1:
                person_positions.append(index)
        answer = 0
        current_person_index = 0
        head_index = tail_index = person_positions[current_person_index]
        for index, seat in enumerate(seats):
            if seat == 1 and current_person_index < len(person_positions) - 1:
                head_index = tail_index
                current_person_index += 1
                tail_index = person_positions[current_person_index]
            this_distance = min(abs(head_index - index), abs(tail_index - index))
            if this_distance > answer:
                answer = this_distance
        return answer

s = Solution()

r = s.maxDistToClosest([1,0,0,0,1,0,1])
print(r)

r = s.maxDistToClosest([1, 0, 0, 0])
print(r)

"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
"""
