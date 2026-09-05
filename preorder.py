# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        self.preorder(root)
        return self.ans
    def __init__(self):
        self.ans =[]

    def preorder(self,root,):
        if root == None:
            return
        self.ans.append(root.val)

        self.preorder(root.left)
        self.preorder(root.right)



        