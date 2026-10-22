class Solution(object):
    def lcs_rec(self,s1,s2,s1i,s2j,dp):
        if s1i < 0 or s2j < 0:
            return 0
        if dp[s1i][s2j] != -1:
            return dp[s1i][s2j]
        if s1[s1i]==s2[s2j]:
             
            dp[s1i][s2j]=self.lcs_rec(s1,s2,s1i-1,s2j-1,dp) + 1
            return dp[s1i][s2j]
        else:
            r1 = self.lcs_rec(s1,s2,s1i-1,s2j,dp)
            r2 = self.lcs_rec(s1,s2,s1i,s2j-1,dp)
            dp[s1i][s2j]= max(r1,r2)
            return dp[s1i][s2j]
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m  = len(text2)
        dp = [[-1]*m for _ in range(n)]
        return self.lcs_rec(text1,text2,len(text1)-1,len(text2)-1,dp)
        