class Solution:
    def dfs(self, node, parent, visited, adj):
        """
        Depth-First Search (DFS) function to detect cycles in the graph.
        """
        visited[node] = True  # Mark the current node as visited

        for neighbor in adj[node]:  # Traverse all adjacent nodes
            if not visited[neighbor]:  # If the neighbor is not visited
                if self.dfs(neighbor, node, visited, adj):  # Recursive DFS call
                    return True
            elif neighbor != parent:  
                # If we visit a node that is not the parent, it means a cycle is detected
                print(neighbor, parent)  # Print the cycle for debugging
                return True
        return False  # No cycle found
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = len(edges)
        adj = [[] for _ in range(m + 1)]  # Adjacency list for the graph
        visited = [False] * (m + 1)  # Visited array to track nodes

        for u, v in edges:  # Iterate over all edges
            visited = [False] * (m + 1)  # Reset visited array before checking for cycles
            adj[u].append(v)  # Add edge (u, v)
            adj[v].append(u)  # Add edge (v, u) since it’s an undirected graph

            if self.dfs(u, -1, visited, adj):  # Check if adding this edge forms a cycle
                return [u, v]  # Return the redundant edge that creates the cycle
        return []  # Return an empty list if no redundant edge is found
        