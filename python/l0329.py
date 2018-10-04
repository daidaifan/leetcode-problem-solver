"""
To get max length of increasing sequences:

Do DFS from every cell
Compare every 4 direction and skip cells that are out of boundary or smaller
Get matrix max from every cell's max
Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
The key is to cache the distance because it's highly possible to revisit a cell
Hope it helps!

public static final int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

public int longestIncreasingPath(int[][] matrix) {
    if(matrix.length == 0) return 0;
    int m = matrix.length, n = matrix[0].length;
    int[][] cache = new int[m][n];
    int max = 1;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            int len = dfs(matrix, i, j, m, n, cache);
            max = Math.max(max, len);
        }
    }
    return max;
}

public int dfs(int[][] matrix, int i, int j, int m, int n, int[][] cache) {
    if(cache[i][j] != 0) return cache[i][j];
    int max = 1;
    for(int[] dir: dirs) {
        int x = i + dir[0], y = j + dir[1];
        if(x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] <= matrix[i][j]) continue;
        int len = 1 + dfs(matrix, x, y, m, n, cache);
        max = Math.max(max, len);
    }
    cache[i][j] = max;
    return max;
}
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        def dfs(i, j, m, n, matrix, cache):
            if cache[i][j] != 0:
                return cache[i][j]
            max_distance = 1
            for d1, d2 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x = i + d1
                y = j + d2
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                    continue
                distance = dfs(x, y, m, n, matrix, cache) + 1
                max_distance = max(max_distance, distance)
            cache[i][j] = max_distance
            return max_distance

        m, n = len(matrix), len(matrix[0])
        cache = [[0 for i in range(n)] for j in range(m)]
        max_distance = 1
        for i in range(m):
            for j in range(n):
                distance = dfs(i, j, m, n, matrix, cache)
                max_distance = max(max_distance, distance)
        return max_distance

s = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
r = s.longestIncreasingPath(matrix)
print(r)
