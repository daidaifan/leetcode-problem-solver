"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""

class Solution:
    def possibleBipartition(self, N, dislikes):
        def dfs(n, groups, n2dis_ns, g):
            groups[n] = g
            for dis_n in n2dis_ns[n]:
                if groups[dis_n] == g:
                    return False
                if groups[dis_n] == 0 and not dfs(dis_n, groups, n2dis_ns, -g):
                    return False
            return True

        dislikes = sorted(dislikes, key=lambda x: (x[0], x[1]))
        n2dis_ns = {}
        for n1, n2 in dislikes:
            if n1 not in n2dis_ns:
                n2dis_ns[n1] = []
            if n2 not in n2dis_ns:
                n2dis_ns[n2] = []
            n2dis_ns[n1].append(n2)
            n2dis_ns[n2].append(n1)
        groups = [0] * (N + 1)
        for n in n2dis_ns.keys():
            if groups[n] == 0 and not dfs(n, groups, n2dis_ns, 1):
                return False
        return True




s = Solution()
print(s.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
print(s.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
print(s.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))



"""
Notes:
group[i] = 0 means node i hasn't been visited.
group[i] = 1 means node i has been grouped to 1.
group[i] = -1 means node i has been grouped to -1.

class Solution {
    public boolean possibleBipartition(int N, int[][] dislikes) {
        int[][] graph = new int[N][N];
        for (int[] d : dislikes) {
            graph[d[0] - 1][d[1] - 1] = 1;
            graph[d[1] - 1][d[0] - 1] = 1;
        }
        int[] group = new int[N];
        for (int i = 0; i < N; i++) {
            if (group[i] == 0 && !dfs(graph, group, i, 1)) {
                return false;
            }
        }
        return true;
    }
    private boolean dfs(int[][] graph, int[] group, int index, int g) {
        group[index] = g;
        for (int i = 0; i < graph.length; i++) {
            if (graph[index][i] == 1) {
                if (group[i] == g) {
                    return false;
                }
                if (group[i] == 0 && !dfs(graph, group, i, -g)) {
                    return false;
                }
            }
        }
        return true;
    }
}
"""
