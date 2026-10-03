class Solution:
    def checkithBit(self,n,k):
        ans = n & (1<<k)
        if ans == 0:
            return False
        return True
    def singleNumber(self, nums: list[int]) -> list[int]:

        # step1--->XOR all the element
        a = 0 
        for i in nums:
            a = a ^ i
        # Step2--> Find the first Set Bit
        id = -1
        for i in range(32):
            if self.checkithBit(a,i):
                id = i
                break
        

        bag1= 0
        bag2 = 0

        # Step3--> Divide into 2 Different Bags
        for n in nums:
            if self.checkithBit(n,id):
                bag1 = bag1^n
            else:
                bag2 = bag2^n
        return [bag1,bag2]