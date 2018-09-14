class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def search(cur_point, target, graph, candidate, solution):
            if cur_point == target:
                solution.append(list(candidate))
                return
            for point in graph[cur_point]:
                candidate.append(point)
                search(point, target, graph, candidate, solution)
                del candidate[-1]
        target = len(graph) - 1
        solution = []
        search(0, target, graph, [], solution)
        return solution

s = Solution()
graph = [[1,2], [3], [3], []]

r = s.allPathsSourceTarget(graph)
print(r)
