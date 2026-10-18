class Solution:
    def memo(self,sr,sc,dr,dc,arr,dp,vis):
        if sc<0 or sc>dc:
            return float('inf')
        if vis[sr][sc] == True:
            return dp[sr][sc]
        if sr == dr:
            return arr[sr][sc]
        
        l1 = self.memo(sr+1,sc-1,dr,dc,arr,dp,vis)
        c1 = self.memo(sr+1,sc,dr,dc,arr,dp,vis)
        r1 = self.memo(sr+1,sc+1,dr,dc,arr,dp,vis)
        ma = min(l1,c1,r1)+arr[sr][sc]
        dp[sr][sc] = ma
        vis[sr][sc] = True
        return ma
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        noc = len(matrix[0])
        nor = len(matrix)
        dp = [[-1]*noc for _ in range(nor)]
        vis = [[False]*noc for _ in range(nor)]
        fans = float('inf')
        for i in range(0,noc):
            ans = self.memo(0,i,nor-1,noc-1,matrix,dp,vis)
            fans = min(fans,ans)
        return fans


        