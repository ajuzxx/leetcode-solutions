class Solution:
    def dfs(self,i,j,grid):
        if i<0 or i>=len(grid) or j <0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] ='0'

        self.dfs(i+1,j,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i,j-1,grid)
        self.dfs(i,j+1,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        size = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='1':
                    size +=1
                    self.dfs(i,j,grid)
        return size
         
        