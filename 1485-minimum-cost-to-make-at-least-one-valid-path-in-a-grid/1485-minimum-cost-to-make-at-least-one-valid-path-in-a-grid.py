class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def inBounds(r, c, cost):
            return r >= 0 and r < n and c >= 0 and c < m and cost < visited.get((r, c), float("inf"))
            


        n, m = len(grid), len(grid[0])
        moves = {1 : [0, 1], 2 : [0, -1], 3 : [1, 0], 4 : [-1, 0]}
        queue = deque([(0, 0, 0)])
        visited = {(0, 0) : 0}

        while queue:
            print(1)
            r, c, cost = queue.popleft()
            if (r, c) == (n - 1, m - 1):
                return cost

            for move in moves:
                print(2)
                x, y = moves[move]
                newR, newC = r + x, c + y
                newCost = cost if grid[r][c] == move else cost + 1
                if inBounds(newR, newC, newCost):
                    print(3)
                    visited[(newR, newC)] = newCost

                    if grid[r][c] == move:
                        queue.appendleft((newR, newC, newCost))
                    else:
                        queue.append((newR, newC, newCost))
        