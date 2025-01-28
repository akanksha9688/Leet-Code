class Solution:
    def __init__(self):
        self.d = [0, 1, 0, -1, 0]
        self.r = 0
        self.c = 0

    def DFS(self, i, j, grid):
            fish = grid[i][j]
            grid[i][j] = 0
            for a in range(4):
                row = i + self.d[a]
                col = j + self.d[a + 1]
                if row < 0 or row >= self.r or col < 0 or col >= self.c or grid[row][col] == 0:
                    continue
                fish += self.DFS(row, col, grid)
            return fish
            
    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.r = len(grid)
        self.c = len(grid[0])
        ans = 0
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] > 0:
                    ans = max(ans, self.DFS(i, j, grid))

        return ans
        