'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def sumBT(self, root):
        if root is None:
            return 0
        #code here
        lsum = self.sumBT(root.left)
        rsum = self.sumBT(root.right)
        
        return lsum + rsum +root.data