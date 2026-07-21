class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        prefix= [0]*n
        prefix[0]= nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i]
        if prefix[len(nums)-1] - prefix[0] == 0:
            return 0
        for k in range(1,n):
            left = prefix[k-1]
            right = prefix[n-1] - prefix[k]

            if left == right:
                return k
        return -1
        