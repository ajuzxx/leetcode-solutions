class Solution(object):
    def searchRange(self, nums, target):
        def first(nums,target):
            s= 0
            e = len(nums)-1
            result = -1
            while s<=e:
                m = s+(e-s)//2
                if nums[m]==target:
                    result = m
                    e = m-1
                elif nums[m] >= target:
                    e = m-1
                else :
                    s = m+1
            return result

        def last(nums,target):
            s= 0
            e = len(nums)-1
            result = -1
            while s<=e:
                m = s+(e-s)//2
                if nums[m]==target:
                    result = m
                    s = m+1
                elif nums[m] >= target:
                    e = m-1
                else :
                    s = m+1
            return result

        return [first(nums,target),last(nums,target)]
        

                    
        