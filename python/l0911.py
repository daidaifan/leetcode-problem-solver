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
        self.persons = persons
        self.times = times
        self.cache = {}

    def q(self, t):
        if t in self.cache:
            return self.cache[t]
        person2num_last = {}
        for person, time in zip(self.persons, self.times):
            if time > t:
                break
            if person not in person2num_last:
                person2num_last[person] = [0, None]
            person2num_last[person][0] += 1
            person2num_last[person][1] = time
        sort = sorted([(person, num, time) for person, (num, time) in person2num_last.items()], key=lambda x: (x[1], x[2]), reverse=True)
        win_person = sort[0][0]
        self.cache[t] = win_person
        return win_person


s = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])

print(s.q(3))
print(s.q(12))
print(s.q(25))

print(s.q(15))
print(s.q(24))
print(s.q(8))
