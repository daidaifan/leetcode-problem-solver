"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.



Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.leads = []
        self.times = times
        person2times = {}
        lead = None
        for p, t in zip(persons, times):
            person2times[p] = person2times.get(p, 0) + 1
            if person2times[p] >= person2times.get(lead, 0):
                lead = p
            self.leads.append(lead)

    def q(self, t):
        if t >= self.times[-1]:
            return self.leads[-1]
        head, tail = 0, len(self.times) - 2
        while head < tail:
            mid = head + (tail - head) // 2
            t1 = self.times[mid]
            t2 = self.times[mid+1]
            if t1 <= t < t2:
                return self.leads[mid]
            elif t < t1:
                tail = mid - 1
            else:
                head = mid + 1
        return self.leads[head]


s = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])

print(s.q(3))
print(s.q(12))
print(s.q(25))

print(s.q(15))
print(s.q(24))
print(s.q(8))
