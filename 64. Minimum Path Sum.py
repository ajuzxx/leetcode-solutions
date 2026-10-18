class Solution:
    def memo(self,sr,sc,dr,dc,arr,dp):
        if sr ==dr and sc == dc:
            return arr[sr][sc]
        if sr>dr or sc > dc:
            return float('inf')
        if dp[sr][sc] != -1:
            return dp[sr][sc]
        rightway = self.memo(sr,sc+1,dr,dc,arr,dp)
        downway = self.memo(sr+1,sc,dr,dc,arr,dp)
        dp[sr][sc] = min(rightway,downway)+arr[sr][sc]
        return dp[sr][sc]
    def tab(self,m,n,arr,):
        dp = [[0]*n for _ in range(m)]
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c == n-1:
                    dp[r][c]=arr[r][c]
                elif r == m-1:
                    dp[r][c] = arr[r][c]+dp[r][c+1]
                elif c == n-1:
                    dp[r][c] = arr[r][c]+dp[r+1][c]
                else:
                    ra1= dp[r][c+1]
                    ra2 = dp[r+1][c]
                    dp[r][c] = min(ra1,ra2) + arr[r][c]
        return dp[0][0]



    def minPathSum(self, grid: list[list[int]]) -> int:
        nor = len(grid)
        noc = len(grid[0])
        dp = [[-1]*noc for _ in range(nor)]
        return self.memo(0,0,nor-1,noc-1,grid,dp)
        