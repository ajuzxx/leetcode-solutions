class Solution:
    def memo(self,idx,arr,sumi,dp):
        if sumi == 0:
            return True
        if sumi < 0:
            return False
        if idx == len(arr):
            return False
        
        if dp[sumi][idx] != -1:
            return dp[sumi][idx] == 1
        r1 = self.memo(idx+1,arr,sumi-arr[idx],dp)
        r2 = self.memo(idx+1,arr,sumi,dp)
        m = r1 or r2
        if m:
            dp[sumi][idx] = 1
        else:
            dp[sumi][idx] = 0
        return m
            
    def isSubsetSum(self, arr: list[int], sumi: int) -> bool:
        dp = [[-1]*len(arr) for _ in range(sumi + 1)]
        return self.memo(0,arr,sumi,dp)
        