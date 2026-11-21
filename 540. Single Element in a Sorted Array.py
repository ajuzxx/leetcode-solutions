class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1
        while L < R:
            M = (L+R)//2
            if M % 2 == 0:
                if nums[M] == nums[M+1]:
                    L = M+2
                else :
                    R= M
            else :
                if nums[M] == nums[M-1]:
                    L = M+1
                else :
                    R = M
        return nums[L]

        