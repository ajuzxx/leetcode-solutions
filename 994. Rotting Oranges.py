from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        time = 0
        direction =[
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]

        while q:
            i,j,current_time = q.popleft()
            time = max(current_time,time)
            for di,dj in direction:
                ni = i +di
                nj = j +dj

                if (0 <= ni <row and
                    0 <= nj <col and
                    grid[ni][nj] == 1):

                    grid[ni][nj] =2
                    fresh -=1

                    q.append((ni,nj,current_time+1))
        if fresh > 0:
            return -1
        return time

            