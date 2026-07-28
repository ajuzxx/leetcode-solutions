class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        reader = 0 
        writer = 0
        while reader < len(nums):
            if nums[reader] != 0:
                nums[writer],nums[reader] = nums[reader],nums[writer]
                reader+=1
                writer+=1
            else :
                reader+=1
        return nums
            


       
       

    
        