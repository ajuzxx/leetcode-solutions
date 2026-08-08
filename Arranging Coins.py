class Solution(object):
    def arrangeCoins(self, n):
        s= 1
        e = n

        while s<=e:
            m = s+(e-s)//2
            k = m*(m+1)/2
            if k == n:
                return m
            if k > n:
                e = m-1
            else :
                s = m+1
        return e

    

        