

class Solution:
    def minValue(self, root):
        if root is None:
            return
        while root.left is not None:
            root = root.left
        return root.data
        # code here
        