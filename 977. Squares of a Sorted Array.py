class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        i = right
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[i] = nums[left]**2
                i -=1
                left += 1
            else:
                result[i] = nums[right]**2
                i -=1
                right -=1
        return result
        