class Solution:

    def numDecodings(self, s: str) -> int:
        memo ={}
        return self.dfs(0,s,memo)

    def dfs(self,i,s,memo):
        if i in memo:
            return memo[i]
        if i == len(s):
            return 1
        if s[i] == '0' :
            return 0
        ways = self.dfs(i+1,s,memo)

        if i+1<len(s) and (s[i] == '1' or (s[i]=='2' and s[i+1] in '0123456')):
            ways +=self.dfs(i+2,s,memo)
        memo[i] = ways
        return ways

        