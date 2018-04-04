"""
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of
people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) == 0 or len(people[0]) == 0:
            return people

        people = sorted(people, key=lambda x: (x[1], x[0]))
        print(people)
        solution = []
        for h, k in people:
            if k == 0:
                solution.append([h, k])
                continue
            num_greater = 0
            for index, (s_h, s_k) in enumerate(solution):
                if s_h >= h:
                    num_greater += 1
                if num_greater == k and ((index == len(solution) - 1) or (solution[index+1][0] > h)):
                    solution.insert(index+1, [h, k])
                    break
            print(solution)
        return solution


s = Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
s.reconstructQueue([])
s.reconstructQueue([[0, 0]])
s.reconstructQueue([[1, 1], [0, 0]])

"""
Easy concept with Python/C++/Java Solution
Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
...

It's not the most concise code, but I think it well explained the concept.

"""


class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        print(peopledct)
        print(height)

        height.sort(reverse=True)      # here are different heights we have

        # sort from the tallest group
        for h in height:
            peopledct[h].sort()
            for k, i in peopledct[h]:
                print(k, i)
                res.insert(k, people[i])
                #res.insert(p[0], h)

        print(res)

        return res

s = Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
"""
EDIT:
Please also check:
@tlhuang 's concise Python code.
@wsurvi 's 4 lines Python code.
@tonygogogo 's 8 lines C++ solution.
@zeller2 's Java version.
@hotpro 's Java 8 solution.
"""

# My solution
class Solution(object):
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        solution = []
        for h, i in people:
            solution.insert(i, [h, i])
        return solution

s = Solution()
print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))


