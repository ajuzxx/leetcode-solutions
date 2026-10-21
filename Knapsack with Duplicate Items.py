class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(wt)
        dp = [[-1] * (W + 1) for _ in range(n)]
        return self.ks_rec(0,W,val,wt,dp)
    def ks_rec(self,idx,W,val,wt,dp):

        if idx == len(wt):
            return 0

        if dp[idx][W] != -1:
            return dp[idx][W]

        op1 = self.ks_rec(idx+1,W,val,wt,dp)

        op2 = 0
        if wt[idx] <= W:
            op2 = val[idx] + self.ks_rec(idx,W-wt[idx],val,wt,dp)
        dp[idx][W] = max(op1, op2)

        return dp[idx][W]