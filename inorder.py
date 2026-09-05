# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        self.inorder(root)
        return self.ans
    def __init__(self):
        self.ans = []
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)


        