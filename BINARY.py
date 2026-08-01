class Solution:
    def binarySearch(self, arr, k):
        s= 0
        e = len(arr)-1
        while s<=e:
            m = s+(e-s)//2
            if arr[m]==k:
                return True
            elif arr[m]<k:
                s= m+1
            elif arr[m]>k:
                e=m-1
        return False
        