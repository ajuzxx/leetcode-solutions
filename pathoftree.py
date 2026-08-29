# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
# @param A : root node of tree
# @param B : integer
# @return a list of integers
    def rootToNode(self, root,val,path):
        if root is None:
            return False

        me_ans = root.val == val
        lans = self. rootToNode(root. left, val, path)
        rans = self. rootToNode(root. right, val,path)

        if lans or rans or me_ans:
            path. append(root.val)
            return True
        return False

    def solve(self, root, target):
        path = []
        self.rootToNode(root, target, path)
        path. reverse()
        return path
        
            
