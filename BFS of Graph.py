from collections import deque

class Solution:
    def bfs(self, adj):
        # code here
        vis = [False]*len(adj)
        q = deque()
        q.append(0)
        ans = []
        
        while len(q)>0:
           fnt = q.popleft()
           
           if vis[fnt]:
               continue
           vis[fnt]= True
           ans.append(fnt)
           for nbr in adj[fnt]:
               if vis[nbr]==False:
                   q.append(nbr)
        return ans