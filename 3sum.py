class Solution(object):
    def threeSum(self, nums):
        n = len(nums) - 1
        nums.sort()
        result= []

        for i in range(0,n-1):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -=1
                elif total < 0:
                    left +=1
                elif total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left  + 1]:
                        left+=1
                    left+=1
                    while left < right and nums[right] == nums[right - 1] :
                        right -=1
                    right -=1
        return result



        