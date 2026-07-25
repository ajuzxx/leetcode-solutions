class Solution(object):
    

        
    def reverseArray(self, arr,li,ri):
        # code here
        left = li
        right = ri
        
        while left< right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
        return arr


    def rotate(self, nums, k):

        n = len(nums)
        if k % n ==0:
            return nums
        else :
            k %= n
 
            self.reverseArray(nums,0,n-1)
            self.reverseArray(nums,0,k-1)
            self.reverseArray(nums,k,n-1)
                



        