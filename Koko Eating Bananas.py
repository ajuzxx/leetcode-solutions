class Solution(object):
    def isPossibleToEat(self,piles,k,h):
        total_time = 0
        for pile in piles:
            total_time += (pile + k - 1) // k
        if total_time>h:
            return False
        return True

    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        possible_ans = right

        while left <= right:
            mid = (left+right)//2

            if self.isPossibleToEat(piles,mid,h):
                possible_ans = mid
                right = mid-1
            else:
                left = mid+1
        return possible_ans 

        