class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            M = (L + R)//2

            if nums[M]  < nums[M+1]:
                L = M +1
            else:
                R = M
        return L
        