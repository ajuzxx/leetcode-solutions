class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        r = k
        best = 0
        curr_sum = 0

        curr_sum = sum(nums[:k])
            
        best = curr_sum

        for r in range(k, len(nums)):
            
            curr_sum = curr_sum - nums[r - k] + nums[r]
            best = max(best,curr_sum)

        return float(best)/k


            


        