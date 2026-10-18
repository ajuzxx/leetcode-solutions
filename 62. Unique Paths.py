class Solution:
    def up_rec(self,sr,sc,dr,dc,dp):
        if sr==dr and sc == dc:
            return 1
        if sr > dr or sc > dc:
            return 0
        if dp[sr][sc]!= -1:
            return dp[sr][sc]
        leftway = self.up_rec(sr,sc+1,dr,dc,dp)
        downway = self.up_rec(sr+1,sc,dr,dc,dp)
        dp[sr][sc]= leftway+downway
        return dp[sr][sc]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        return self.up_rec(0,0,m-1,n-1,dp)
        