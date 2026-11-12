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
        

        # second clean approach -----------------------------------


class Solution(object):
    def searchRange(self, nums, target):
        def binarysearch(firstsearch):

            start,end = 0,len(nums) - 1
            result = -1

            while start<= end :
                mid = (start + end) // 2 
                if nums[mid] == target:
                    result =  mid
                    if firstsearch:
                        end = mid-1
                    else:
                        start = mid+1
                elif nums[mid] > target:
                    end = mid -1
                else:
                    start = mid + 1
            return result
        firstOurrents = binarysearch(True)
        if firstOurrents == -1:
            return [-1,-1]
        return[firstOurrents,binarysearch(False)]
            



                    
        