class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.memo(n,dp)
    
    def memo(self,n,dp):
        if n == 0 or n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        ra1 = self.memo(n-1,dp)
        ra2 = self.memo(n-2,dp)
        m = ra1 + ra2
        dp[n] = m
        return m
        

        