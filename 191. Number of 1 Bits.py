class Solution(object):    
    def checkKthBit(self, n, k):
        # code here
    
        
        return (n | (1 << k)) == n

    def hammingWeight(self, n):
        count = 0
        for i in range(31):
            if self.checkKthBit(n,i):
                count+=1
        return count
        