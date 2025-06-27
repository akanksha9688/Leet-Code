from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n = len(grid[0])
        queue=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append([i,j,0])
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        time=0
        while(len(queue)!=0):
            Pair=queue.popleft()
            curr_x=Pair[0]
            curr_y=Pair[1]
            curr_step=Pair[2]
            # time=curr_step
            for d in dir:
                new_x=curr_x + d[0]
                new_y=curr_y + d[1]
                if new_x >=0 and new_x < m and new_y >=0 and new_y < n and grid[new_x][new_y]==1:
                    # queue.append((new_x,new_y,curr_step+1))
                    #  grid[new_x][new_y]=1
                    if grid[new_x][new_y]==1:
                        time=curr_step+1
                        grid[new_x][new_y]=2
                        queue.append((new_x,new_y,curr_step+1))
        for i in grid:
            if 1 in i:
                return -1
        return time
        