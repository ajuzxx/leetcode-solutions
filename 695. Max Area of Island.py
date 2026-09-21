class Solution:
    def dfs(self,i,j,grid):
        if i<0 or i>=len(grid) or j <0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0

        da = self.dfs(i+1,j,grid)
        ua =self.dfs(i-1,j,grid)
        la =self.dfs(i,j-1,grid)
        ra =self.dfs(i,j+1,grid)
        return da+ua+la+ra+1

    
        
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area =self.dfs(i,j,grid)
                    maxArea = max(area,maxArea)
        return maxArea