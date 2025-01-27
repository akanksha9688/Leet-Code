class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Mark direct prerequisites as reachable
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # Floyd-Warshall algorithm to compute transitive closure
        for k in range(numCourses):  # via node
            for i in range(numCourses):  # Starting node
                for j in range(numCourses):  # Ending node
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        res = []
        for a, b in queries:
            res.append(reachable[a][b])
        
        return res

        