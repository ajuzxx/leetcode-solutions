"""
Definition for Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def getSize(self, root):
                      
        if root is None :
            return 0
        lsize = self.getSize(root.left)
        rsize = self.getSize(root.right)

        return lsize + rsize + 1
                  
        