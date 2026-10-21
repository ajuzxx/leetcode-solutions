class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp =[0]*len(nums)
        dp[0] =1
        lis =1

        for i in range(1,len(nums)):
            possible =0
            for j in range(i):
                if nums[i]>nums[j]:
                    possible = max(possible,dp[j])
            dp[i] = possible +1
            lis = max(lis,dp[i])
        return lis