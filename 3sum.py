class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        current =0

        while current<= right:
            if nums[current]==0:

                nums[left],nums[current] = nums[current],nums[left]
                current+=1
                left+=1
            elif nums[current]==2:
                nums[right],nums[current] = nums[current],nums[right]
                right-=1
            else :
                current+=1
        return nums

        
        

