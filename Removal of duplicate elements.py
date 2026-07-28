class Solution(object):
    def removeDuplicates(self, nums):
        reader = 0
        writer = 0
        while reader < len(nums):
            if reader == len(nums)-1:
                nums[writer]= nums[reader]
            

                return writer+1
            if nums[reader]!=nums[reader+1]:
                nums[writer]= nums[reader]
                reader+=1
                writer+=1
            else:
                reader+=1