# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Data:
    def __init__(self):
        self.mini = float('inf')
        self.maxi = float('-inf')
        self.bts = True
class Solution(object):
    def checkBST(self,root):
        if root is None:
            return Data()

        current = Data()

        left = self.checkBST(root.left)
        right = self.checkBST(root.right)

        current.mini = min(left.mini,root.val,right.mini)
        current.maxi = max(left.maxi,root.val,right.maxi)

        current.bts = (
            left.bts
            and right.bts
            and root.val > left.maxi
            and root.val < right.mini
        )

        return current


    def isValidBST(self, root):
        result = self.checkBST(root)
        return result.bts

        