class Solution:
    def mcm(self,s,e,arr,dp):
        if e ==s+1:
            return 0
        if dp[s][e] != -1:
            return dp[s][e]
        ans = float('inf')
        for cut in range(s+1,e):
            lc = self.mcm(s, cut, arr, dp)
            rc = self.mcm(cut, e, arr, dp)
            sc = arr[s]*arr[cut]*arr[e]
            tc = lc+rc+sc
            ans = min(ans,tc)
        dp[s][e] = ans
        return ans
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1]*n for _ in range(n)]
        return self.mcm(0,n-1,arr,dp)
        
        