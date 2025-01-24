class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        hashMap = {}

        def DFS(node):
            if node in hashMap:
                return hashMap[node]
            hashMap[node] = False
            
            for nextNode in graph[node]:
                if not DFS(nextNode):
                    return False

            hashMap[node] = True
            return hashMap[node]

        res = []
        for i in range(n):
            if DFS(i):
                res.append(i)

        return res