''' Structure of binary tree node
class Node: 
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def findMax(self, root):
        if root is None :
            return float('-inf')
            
        lmax = self.findMax(root.left)
        rmax = self.findMax(root.right)
        
        return max(lmax,rmax,root.data)
    def findMin(self, root):
        
        if root is None :
            return float('inf')
            
        lmax = self.findMin(root.left)
        rmax = self.findMin(root.right)
        
        return min(lmax,rmax,root.data)
        
        
        
        #code here