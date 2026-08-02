class Solution(object):
    def ispossible(self,weights,mid,days):
        cap = 0
        daysformove = 1
        for weight in weights:
            cap +=weight
            if cap > mid:
                daysformove +=1
                cap = weight
        if daysformove > days:
            return False
        return True


    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        best = left

        while left <= right:
            mid = left +(right-left)//2

            if self.ispossible(weights,mid,days):
                best = mid
                right = mid - 1
            else:
                left= mid +1
        return best

        
        
        
        