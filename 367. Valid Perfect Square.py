class Solution(object):
    def isPerfectSquare(self, num):
        s = 1
        e = num/2

        if num == 1:
            return True

        while s <= e:
            mid = (s+e)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                s = mid+1
            else:
                e = mid-1
        return False
        