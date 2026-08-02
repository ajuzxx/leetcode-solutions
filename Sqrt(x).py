class Solution(object):
    def mySqrt(self, x):
        s= 1
        e = x
        if x==0:
            return 0

        while s<= e:
            m = s+(e-s)//2
            if m*m == x:
                return m
            elif m*m > x:
                e=m-1
            else:
                s=m+1
        return e


        