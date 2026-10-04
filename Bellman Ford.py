class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        #code here
        inf = 10**8
        dist = [inf]*V
        dist[src] = 0
        
        for _ in range(V-1):
            for u,v,w in edges:
                if dist[u] != inf and dist[u] + w <dist[v]:
                    dist[v]= dist[u]+w
        
        for u,v,w in edges:
                if dist[u] != inf and dist[u] + w <dist[v]:
                    return [-1]
        return dist
        