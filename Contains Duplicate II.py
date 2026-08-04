class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
       


        window = set()
        for i in range(len(nums)):
            nu = nums[i]
            if nu in window:
                return True
            else :
                window.add(nu)
                if len(window)>k:
                    window.remove(nums[i-k])
        return False

