class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        node2others = {}
        for a, b in edges:
            if a not in node2others:
                node2others[a] = []
            if b not in node2others:
                node2others[b] = []
            node2others[a].append(b)
            node2others[b].append(a)
        while len(node2others.keys()) != 0:
            if len(node2others.keys()) <= 2:
                return node2others.keys()
            remove_nodes = [node for node, others in node2others.items() if len(others) == 1]
            for remove_node in remove_nodes:
                target = node2others[remove_node][0]
                node2others[target].remove(remove_node)
                del node2others[remove_node]
        return [0]
