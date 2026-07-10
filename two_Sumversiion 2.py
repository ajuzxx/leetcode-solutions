
class Solution(object):
    def twoSum(self, nums, target):
        previous = {}
        for i,num in enumerate(nums):
            goal = target- num
            if goal in previous:
                return[previous[goal],i]
            previous[num]=i