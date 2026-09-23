from collections import deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        size = [[] for _ in range(n)]

        for s, v in edges:
            size[s].append(v)
            size[v].append(s)

        vis = [False] * n

        q = deque()
        q.append(source)

        while len(q) > 0:
            fnt = q.popleft()

            if fnt == destination:
                return True

            if vis[fnt]:
                continue

            vis[fnt] = True

            for nbr in size[fnt]:
                if vis[nbr] == False:
                    q.append(nbr)

        return False