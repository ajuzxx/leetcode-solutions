# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rootToNode(self, root,val,path):
        if root is None:
            return False

        me_ans = root.val == val
        lans = self. rootToNode(root. left, val, path)
        rans = self. rootToNode(root. right, val,path)

        if lans or rans or me_ans:
            path. append(root)
            return True
        return False

    def solve(self, root, target):
        path = []
        self.rootToNode(root, target, path)
        path. reverse()
        return path
    def lowestCommonAncestor(self, root, p, q):
        ppath = self.solve(root,p.val)
        qpath = self.solve(root,q.val)

        i = 0
        lca = None
        while i < len(ppath) and i < len(qpath):
            if ppath[i] == qpath[i]:
                lca = ppath[i]
            else:
                return lca
            i+=1
        return lca
        